#!/usr/bin/env python3
"""learn_media.py — collect the real product screenshots on a Microsoft Learn section, to use as b-roll.

    python3 -I docs/reels/demo/learn_media.py fabric/iq <outdir> [--max 40]                 # a whole docs section
    python3 -I docs/reels/demo/learn_media.py fabric/fundamentals/direct-lake-overview <outdir>   # one page
    python3 -I docs/reels/demo/learn_media.py "search:direct lake" <outdir> [--pages 8]   # the Fabric pages whose
                                                                    # title names a script line's topic

The Fabric docs (github.com/MicrosoftDocs/fabric-docs) are licensed CC BY 4.0, so their screenshots can be reused with a
credit ("Image: Microsoft, CC BY 4.0, Microsoft Learn"); the licence covers copyright, not Microsoft's trademarks or
logos. Only pages under learn.microsoft.com/<locale>/fabric/ are used: that is the docs set with the checked
CC BY 4.0 licence (Power BI's own docs pages are skipped until their licence is checked). SVG diagrams are rendered to
PNG in the preinstalled Chromium. Writes <outdir>/<n>.png|jpg, <outdir>/media.json (page, alt text, image URL, size,
credit) and <outdir>/sheet-*.jpg contact sheets to LOOK at before choosing. Screenshots are often landscape: crop the part that
matters into the 9:16 frame, or float it as a "window" beat over the take.
"""
import argparse, json, os, pathlib, re, sys, time, urllib.parse, urllib.request

BASE = "https://learn.microsoft.com/en-us/"
UA = {"User-Agent": "MS_SE-content-machine/1.0 (b-roll research)"}
CREDIT = "Image: Microsoft, CC BY 4.0, via Microsoft Learn (MicrosoftDocs/fabric-docs)"
FABRIC = re.compile(r"^https://learn\.microsoft\.com/[a-z-]+/fabric/")


def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()


SECTIONS = ("fundamentals iq onelake data-warehouse data-engineering data-factory real-time-intelligence governance "
            "security admin enterprise database apps data-science mirroring cicd").split()


def toc(section):
    """[(title, url)] for every page in a docs section's table of contents."""
    out = []
    def walk(items):
        for it in items:
            h = it.get("href", "")
            if h and not h.startswith(("/", "http")):
                out.append((it.get("toc_title", ""), urllib.parse.urljoin(BASE + section.rstrip("/") + "/", h)))
            walk(it.get("children", []))
    walk(json.loads(get(BASE + section.rstrip("/") + "/toc.json")).get("items", []))
    return out


def search(q, n):
    """The Fabric doc pages whose contents title has every word of the query (most specific first); none -> Learn's
    own search API (it ranks loosely, so the title match comes first)."""
    words = q.lower().split()
    hits = []
    for sec in SECTIONS:
        try:
            hits += [(len(t), u) for t, u in toc("fabric/" + sec) if all(w in t.lower() for w in words)]
        except Exception:
            pass
    urls = list(dict.fromkeys(u for _, u in sorted(hits)))
    if not urls:
        api = "https://learn.microsoft.com/api/search?" + urllib.parse.urlencode({"search": q, "locale": "en-us", "$top": 25})
        urls = [r["url"] for r in json.loads(get(api)).get("results", [])]
    return [u for u in urls if FABRIC.match(u)][:n]


def pages(section, n):
    """A section (fabric/iq) -> every page in its table of contents; a page path -> just that page; search:<q> -> top hits."""
    if section.startswith("search:"):
        return search(section[7:], n)
    try:
        return list(dict.fromkeys(u for _, u in toc(section)))
    except Exception:
        return [BASE + section]


def images(page):
    t = get(page).decode("utf-8", "ignore")
    m = re.search(r"<main.*?</main>", t, re.S)
    main = m.group(0) if m else t
    for tag in re.findall(r"<img[^>]+>", main):
        src = re.search(r'src="([^"]+)"', tag); alt = re.search(r'alt="([^"]*)"', tag)
        if src and "media/" in src.group(1) and alt and alt.group(1).strip():   # no alt text = an icon or decoration
            yield urllib.parse.urljoin(page, src.group(1)), (alt.group(1) if alt else "")


def svg_to_png(svg_path):
    """Learn draws its diagrams as SVG: render one at 3x in the preinstalled Chromium so it can be used as a picture."""
    from playwright.sync_api import sync_playwright
    png = os.path.splitext(svg_path)[0] + ".png"
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page(device_scale_factor=3)
        pg.goto(pathlib.Path(svg_path).resolve().as_uri())
        box = pg.evaluate("(() => { const r = document.documentElement.getBoundingClientRect(); return [r.width, r.height]; })()")
        pg.set_viewport_size({"width": max(1, int(box[0])), "height": max(1, int(box[1]))})
        pg.screenshot(path=png, omit_background=False)
        b.close()
    return png


def too_small(path, short=300, long=600):
    """Icons and inline glyphs are no use on a 1080x1920 frame."""
    try:
        from PIL import Image
        with Image.open(path) as im:
            return min(im.size) < short or max(im.size) < long
    except Exception:
        return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("section"); ap.add_argument("out"); ap.add_argument("--max", type=int, default=40)
    ap.add_argument("--pages", type=int, default=8, help="search: how many result pages to open")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    rows, seen = [], set()
    for pg in pages(a.section, a.pages):
        if not FABRIC.match(pg):
            print(f"  - skipped (not a Fabric docs page): {pg}", file=sys.stderr)
            continue
        try:
            for url, alt in images(pg):
                if url in seen or len(rows) >= a.max:
                    continue
                seen.add(url)
                ext = os.path.splitext(urllib.parse.urlparse(url).path)[1].lower() or ".png"
                path = os.path.join(a.out, f"{len(rows):02d}{ext}")
                open(path, "wb").write(get(url))
                if ext == ".svg":
                    try:
                        path = svg_to_png(path)
                    except Exception as e:
                        print(f"  ! could not render {url}: {e}", file=sys.stderr)
                        continue
                if too_small(path):
                    os.remove(path)
                    continue
                rows.append(dict(file=os.path.basename(path), page=pg, alt=alt, url=url, credit=CREDIT))
                time.sleep(0.2)
        except Exception as e:
            print(f"  ! {pg}: {e}", file=sys.stderr)
        if len(rows) >= a.max:
            break
    try:
        from PIL import Image, ImageDraw
        for r in list(rows):
            try:
                with Image.open(os.path.join(a.out, r["file"])) as im:
                    r["size"] = f"{im.width}x{im.height}"
            except Exception:
                rows.remove(r)   # not a picture Pillow can read (left on disk, not listed)
        cw, ch, cols = 360, 230, 4
        for k in range(0, len(rows), 16):
            chunk = rows[k:k + 16]
            sheet = Image.new("RGB", (cw * cols, ch * ((len(chunk) + cols - 1) // cols)), "white")
            for j, r in enumerate(chunk):
                im = Image.open(os.path.join(a.out, r["file"])).convert("RGB"); im.thumbnail((cw - 8, ch - 26))
                x, y = (j % cols) * cw, (j // cols) * ch
                sheet.paste(im, (x + 4, y + 22)); ImageDraw.Draw(sheet).text((x + 6, y + 4), f"{r['file']} {r.get('size', '')}", fill="black")
            sheet.save(os.path.join(a.out, f"sheet-{k // 16}.jpg"), quality=82)
    except ImportError:
        pass
    json.dump(rows, open(os.path.join(a.out, "media.json"), "w"), indent=1)
    print(f"{len(rows)} screenshots -> {a.out} (media.json, sheet-*.jpg)")


if __name__ == "__main__":
    main()
