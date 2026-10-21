#!/usr/bin/env python3
"""commons.py — find openly licensed, high-resolution photos on Wikimedia Commons and look at them before use.

    python3 -I commons.py search <outdir> "<query>" [--min-h 1600]   # list + thumbnails + a sheet to LOOK at
    python3 -I commons.py get <outdir> "<File:Title.jpg>" <name>      # download the original + record its credit

Only licences that allow commercial reuse without share-alike are kept: CC0, Public domain, CC BY 2.0/2.5/3.0/4.0.
Credits (title, author, licence, source page) go to <outdir>/credits.json.
"""
import json, os, re, sys, time, urllib.error, urllib.parse, urllib.request

API = "https://commons.wikimedia.org/w/api.php"
UA = {"User-Agent": "MS_SE-content-machine/1.0 (example video research; https://github.com/TayoAki/MS_SE)"}
OK = re.compile(r"^(CC0|Public domain|PD|CC BY [234]\.[05])", re.I)


def polite(url, tries=5):
    """Wikimedia rate-limits bursts (HTTP 429 + Retry-After): wait as asked, then retry."""
    for k in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90).read()
        except urllib.error.HTTPError as e:
            if e.code != 429 or k == tries - 1:
                raise
            wait = int(e.headers.get("Retry-After") or 30) + 2
            print(f"  (rate-limited, waiting {wait}s)", file=sys.stderr)
            time.sleep(wait)


def api(params):
    return json.loads(polite(API + "?" + urllib.parse.urlencode({**params, "format": "json"})))


def info(pages):
    out = []
    for p in sorted(pages.values(), key=lambda p: p.get("index", 0)):
        ii = (p.get("imageinfo") or [{}])[0]; m = ii.get("extmetadata", {})
        lic = m.get("LicenseShortName", {}).get("value", "")
        art = re.sub(r"<[^>]+>", "", m.get("Artist", {}).get("value", "")).strip()
        out.append(dict(title=p["title"], w=ii.get("width", 0), h=ii.get("height", 0), lic=lic, artist=art,
                        url=ii.get("url", ""), thumb=ii.get("thumburl", ""), page=ii.get("descriptionurl", "")))
    return out


def fetch(url, path):
    open(path, "wb").write(polite(url))
    time.sleep(1.5)


def search(outdir, q, min_h=1600):
    d = api(dict(action="query", generator="search", gsrsearch=f"{q} filetype:bitmap", gsrnamespace=6, gsrlimit=40,
                 prop="imageinfo", iiprop="url|size|extmetadata", iiurlwidth=360,
                 iiextmetadatafilter="LicenseShortName|Artist"))
    rows = [r for r in info(d.get("query", {}).get("pages", {})) if OK.match(r["lic"]) and r["h"] >= min_h]
    slug = re.sub(r"[^a-z0-9]+", "-", q.lower()).strip("-")
    tdir = os.path.join(outdir, "thumbs", slug); os.makedirs(tdir, exist_ok=True)
    keep = []
    for i, r in enumerate(rows[:10]):
        p = os.path.join(tdir, f"{i:02d}.jpg")
        try:
            fetch(r["thumb"], p); keep.append((i, r, p))
        except Exception as e:
            print(f"  ! thumb {i}: {e}", file=sys.stderr)
    for i, r, _ in keep:
        print(f"{i:02d} | {r['w']}x{r['h']} | {r['lic']:14} | {r['artist'][:30]:30} | {r['title'][:80]}")
    try:
        from PIL import Image, ImageDraw
        ims = [(i, Image.open(p).convert("RGB")) for i, _, p in keep]
        if ims:
            cw, ch, cols = 360, 270, 5
            sheet = Image.new("RGB", (cw * cols, ch * ((len(ims) + cols - 1) // cols)), "black")
            for k, (i, im) in enumerate(ims):
                im.thumbnail((cw, ch)); x, y = (k % cols) * cw, (k // cols) * ch
                sheet.paste(im, (x, y)); ImageDraw.Draw(sheet).text((x + 6, y + 6), f"{i:02d}", fill="yellow")
            sheet.save(os.path.join(outdir, f"sheet-{slug}.jpg"), quality=82)
            print("sheet:", os.path.join(outdir, f"sheet-{slug}.jpg"))
    except ImportError:
        pass
    json.dump([r for _, r, _ in keep], open(os.path.join(tdir, "rows.json"), "w"), indent=1)


def get(outdir, title, name):
    # Wikimedia's own 3000 px rendition: sharper than a 1080x1920 frame needs, and the route it prefers for scripts
    d = api(dict(action="query", titles=title, prop="imageinfo", iiprop="url|size|extmetadata", iiurlwidth=3000,
                 iiextmetadatafilter="LicenseShortName|Artist"))
    r = info(d["query"]["pages"])[0]
    if not OK.match(r["lic"]):
        sys.exit(f"refusing {title}: licence {r['lic']!r}")
    src = (r["thumb"] or r["url"]).split("?")[0]
    ext = os.path.splitext(src)[1].lower() or ".jpg"
    path = os.path.join(outdir, name + ext); fetch(src, path)
    cf = os.path.join(outdir, "credits.json")
    credits = json.load(open(cf)) if os.path.exists(cf) else []
    credits = [c for c in credits if c["file"] != os.path.basename(path)] + [dict(file=os.path.basename(path), title=title,
               author=r["artist"], licence=r["lic"], source=r["page"], size=f"{r['w']}x{r['h']}")]
    json.dump(credits, open(cf, "w"), indent=1)
    print(f"saved {path} ({r['w']}x{r['h']}, {r['lic']}, {r['artist']})")


if __name__ == "__main__":
    cmd, outdir = sys.argv[1], sys.argv[2]
    os.makedirs(outdir, exist_ok=True)
    if cmd == "search":
        search(outdir, sys.argv[3], int(sys.argv[5]) if len(sys.argv) > 5 and sys.argv[4] == "--min-h" else 1600)
    elif cmd == "get":
        get(outdir, sys.argv[3], sys.argv[4])
