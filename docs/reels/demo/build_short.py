#!/usr/bin/env python3
"""build_short.py — turn a beat spec (JSON) into a Persa Shorts composition, before anything is recorded.

    python3 -I docs/reels/demo/build_short.py docs/reels/demo/rc1.json --out ~/persa-shorts/rc1-fabric-apps
    npx --yes hyperframes check <out> && npx --yes hyperframes render <out> -o <out>/<name>.mp4 -q draft

The spec lists the script's spoken lines; each line is one beat:
  {"say": "...", "kind": "face"}                         the creator (a silhouette until the take is recorded)
  {"say": "...", "kind": "page", "src": "assets/pages/x.png", "hl": true, "annot": "TEXT"}
                                                         a real 9:16 page shot owns the frame (shoot-page-9x16.py);
                                                         hl draws the marker over the phrase rects in x.json
  {"say": "...", "kind": "shot", "src": "assets/shots/x.png", "crop": [x, y, w, h], "box": [[x, y, w, h]], "annot": "TEXT"}
                                                         a screenshot or diagram (learn_media.py) shown whole in a window
                                                         over the ground; crop and box are in the image's own pixels;
                                                         the credit line above it comes from "credit" or the spec's
                                                         "shot_credit"
  {"say": "...", "kind": "clip", "src": "assets/clips/x.mp4", "box": [[x, y, w, h]], "fill": false, "media_start": 0}
                                                         a video cut by yt_clips.py (licence checked, cropped, no audio)
                                                         playing in the picture area, or the whole frame with "fill";
                                                         its credit comes from the cut's sidecar x.json
  {"say": "...", "kind": "cta", "keyword": "WORD"}       the call to action; captions drop
optional on any line: "emph": ["WORD", "w"|"a"] (hollow, on the spoken word), "payoff": "WORD" (filled, on the word),
"hook": ["LINE 1", "LINE 2"] (big first-frame words: the thumbnail on LinkedIn), "card": {"tag": "#1", "text": "WORDS",
"on": "word"} (a numbered card that pops in on the word), "key": ["word", ...] (caption words drawn in the accent).
optional on the spec: "header": "LINE 1\nLINE 2" (the promise, held on screen from the first frame to the call to
action: muted viewers always know what they're watching), "pace" (words per second, default 2.75).
Images are paths inside <out>. Brand tokens come from the nextphase-persa-shorts skill.
"""
import argparse, html, json, os, pathlib, shutil, struct, sys

SKILL = pathlib.Path(os.path.expanduser("~/.claude/skills/nextphase-persa-shorts"))
PACE, GAP = 2.75, 0.25          # words per second, breath between lines
SHOT_W, SHOT_H, SHOT_TOP = 1000, 880, 170   # the picture area above the camera card


def img_size(path):
    """(width, height) of a PNG or JPEG, from its header (no Pillow needed)."""
    b = pathlib.Path(path).read_bytes()
    if b[:8] == b"\x89PNG\r\n\x1a\n":
        return struct.unpack(">II", b[16:24])
    i = 2
    while i < len(b):
        if b[i] != 0xFF:
            i += 1
            continue
        m = b[i + 1]
        if m in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
            h, w = struct.unpack(">HH", b[i + 5:i + 9])
            return w, h
        i += 2 + struct.unpack(">H", b[i + 2:i + 4])[0]
    sys.exit(f"build_short: can't read the size of {path}")


def esc(s):
    return html.escape(str(s), quote=True)


def build(spec, out):
    brand = json.loads((SKILL / "brand/brand.json").read_text())
    adv = 0.5
    for ln in (SKILL / "assets/tokens.css").read_text().splitlines():
        if "--display-advance:" in ln:
            adv = float(ln.split(":")[1].split(";")[0])
    fit = lambda w, cap=290, box=940: max(60, min(cap, int(box / (adv * max(1, len(w))))))
    g = ' class="graded"' if brand.get("grade", "film") == "film" else ""
    gcls = " graded" if g else ""

    pace = spec.get("pace", PACE)
    header = spec.get("header")
    shot_top, shot_h = (330, 740) if header else (SHOT_TOP, SHOT_H)
    disp_top = 380 if header else 300
    tr = [20]
    def clip(cls, s, d, inner="", style=""):
        tr[0] += 1
        st = f' style="{style}"' if style else ""
        return f'<div class="clip {cls}" data-start="{s:.2f}" data-duration="{d:.2f}" data-track-index="{tr[0]}"{st}>{inner}</div>'

    def sil(gid):
        return (f'<svg viewBox="0 0 1080 1920" width="1080" height="1920" aria-hidden="true"><defs><linearGradient id="{gid}" '
                f'x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2B221D"/><stop offset="1" stop-color="#0F0B09"/>'
                f'</linearGradient></defs><path fill="url(#{gid})" d="M540 600 C640 600 705 680 705 795 C705 895 668 975 612 1018 '
                f'L612 1092 C790 1125 930 1210 975 1360 L1020 1920 L60 1920 L105 1360 C150 1210 290 1125 468 1092 '
                f'L468 1018 C412 975 375 895 375 795 C375 680 440 600 540 600 Z"/></svg>')

    room = f'<div class="room"{g}><i class="win"></i><i class="lamp"></i><i class="shelf"></i></div>'
    body, caps, t = [], [], 0.0
    for k, x in enumerate(spec["lines"]):
        words = x["say"].replace(":", "").split()
        d = max(1.6, len(words) / pace)
        s, e = t, t + d
        per = d / len(words)
        def on_word(w):
            for i, x_ in enumerate(words):
                if x_.strip(".,'?!\"").upper().replace("’", "'") == w.upper():
                    return s + per * i
            sys.exit(f"build_short: '{w}' is not spoken in line {k + 1}: {x['say']}")
        kind = x["kind"]
        if kind not in ("face", "page", "shot", "clip", "cta"):
            sys.exit(f"build_short: line {k + 1} has an unknown kind '{kind}'")
        if kind in ("face", "cta"):
            body.append(clip("vig", s, d))
            body.append(clip("silwrap", s, d, f"<div{g}>{sil(f's{k}')}</div>"))
        if kind == "shot":
            W, H = img_size(out / x["src"])
            cx, cy, cw, ch = x.get("crop") or [0, 0, W, H]
            z = min(SHOT_W / cw, shot_h / ch)
            ww, wh = round(cw * z), round(ch * z)
            left, top = (1080 - ww) // 2, shot_top + (shot_h - wh) // 2
            credit = x.get("credit", spec.get("shot_credit", ""))
            body.append(clip("shotwrap", s, d,
                             f'<div class="shotcredit" style="top:{top - 46}px">{esc(credit)}</div>'
                             f'<div class="shotwin" style="left:{left}px;top:{top}px;width:{ww}px;height:{wh}px">'
                             f'<img src="{esc(x["src"])}" alt="" style="left:{-cx * z:.0f}px;top:{-cy * z:.0f}px;'
                             f'width:{W * z:.0f}px;height:{H * z:.0f}px"></div>'))
            for bx, by, bw, bh in x.get("box", []):
                body.append(clip("shotbox", s + 0.35, d - 0.4, "",
                                 f"left:{left + (bx - cx) * z - 8:.0f}px;top:{top + (by - cy) * z - 8:.0f}px;"
                                 f"width:{bw * z + 16:.0f}px;height:{bh * z + 16:.0f}px"))
        if kind == "clip":   # the <video> is its own timed element: nested in a timed div it renders frozen
            meta = json.loads((out / pathlib.Path(x["src"]).with_suffix(".json")).read_text())
            W, H = meta["width"], meta["height"]
            if meta["duration"] + 0.05 < d:
                print(f"build_short: line {k + 1}: the clip is {meta['duration']:.1f}s, the line {d:.1f}s; it will hold "
                      "its last frame", file=sys.stderr)
            if x.get("fill"):
                z = max(1080 / W, 1920 / H); ww, wh = 1080, 1920; left = top = 0
                cx, cy = (W * z - 1080) / 2 / z, (H * z - 1920) / 2 / z
            else:
                z = min(SHOT_W / W, shot_h / H); ww, wh = round(W * z), round(H * z)
                left, top = (1080 - ww) // 2, shot_top + (shot_h - wh) // 2; cx = cy = 0
            body.append(clip("shotwrap", s, d, "" if x.get("fill") else
                             f'<div class="shotcredit" style="top:{top - 46}px">{esc(x.get("credit", meta["credit"]))}</div>'))
            tr[0] += 1
            body.append(f'<video class="clip shotvid" id="v{tr[0]}" src="{esc(x["src"])}" data-start="{s:.2f}" data-duration="{d:.2f}" '
                        f'data-media-start="{float(x.get("media_start", 0)):.2f}" data-track-index="{tr[0]}" muted playsinline '
                        f'style="left:{left}px;top:{top}px;width:{ww}px;height:{wh}px{";border-radius:0" if x.get("fill") else ""}">'
                        f'</video>')
            if x.get("fill"):
                body.append(clip("shotcredit", s, d, esc(x.get("credit", meta["credit"])), "top:72px;z-index:8"))
            for bx, by, bw, bh in x.get("box", []):
                body.append(clip("shotbox", s + 0.35, d - 0.4, "",
                                 f"left:{left + (bx - cx) * z - 8:.0f}px;top:{top + (by - cy) * z - 8:.0f}px;"
                                 f"width:{bw * z + 16:.0f}px;height:{bh * z + 16:.0f}px"))
        if kind in ("page", "shot", "clip"):
            if kind == "page":
                body.append(clip("uiwrap", s, d, f'<img class="page" src="{esc(x["src"])}" alt="">'))
            if kind == "page" and x.get("hl"):
                rects = json.loads((out / pathlib.Path(x["src"]).with_suffix(".json")).read_text()).get("rects", [])
                for r in [r for r in rects if r["phrase"] == rects[0]["phrase"]][:3]:   # every line of a wrapped phrase
                    body.append(clip("hlbox", s + 0.35, d - 0.4, "",
                                     f"left:{r['left'] * 10.8 - 8:.0f}px;top:{r['top'] * 19.2 - 6:.0f}px;"
                                     f"width:{r['width'] * 10.8 + 16:.0f}px;height:{r['height'] * 19.2 + 12:.0f}px"))
            if x.get("annot"):
                body.append(clip("annot", s + 0.45, d - 0.5, esc(x["annot"]).replace("\n", "<br>"),
                                 "left:70px;top:1010px;font-size:50px"))
            body.append(clip("cardwrap", s, d, f'<div class="cardroom"{g}></div><div class="cardsil"{g}>{sil(f"c{k}")}</div>'))
            body.append(clip("cardhead", s, d, f"<div{g}>{sil(f'h{k}')}</div>"))
        if x.get("hook"):
            a, b = x["hook"]
            body.append(clip("hookwords", s, d, f'<div class="hw1">{esc(a)}</div><div class="hw2">{esc(b)}</div>',
                             f"top:{disp_top - 150 + 30}px" if header else ""))
        if x.get("emph"):
            w, tone = x["emph"]
            at = max(s, on_word(w) - 0.5)
            body.append(clip(f"emph e-{tone}", at, max(1.0, min(1.6, e - at)), esc(w.upper()), f"top:{disp_top}px;font-size:{fit(w)}px"))
        if x.get("payoff"):
            w = x["payoff"]
            at = max(s, on_word(w) - 0.5)
            body.append(clip("payoff", at, max(1.0, e - at), esc(w.upper()), f"top:{disp_top}px;font-size:{fit(w)}px"))
        if x.get("card"):
            c = x["card"]
            at = max(s, on_word(c["on"]) - 0.15) if c.get("on") else s + 0.2
            tag = f'<span class="ctag">{esc(c["tag"])}</span>' if c.get("tag") else ""
            body.append(clip("numcard", at, e - at, f'{tag}<span class="ctext">{esc(c["text"])}</span>',
                             (f"top:{min(top + wh + 24 if wh < 480 else top + wh - 70, 1010)}px"   # below a short picture
                              if kind in ("shot", "clip") and not x.get("fill") else "top:1150px")))
        if kind == "cta":
            kw = x["keyword"].upper()
            size = fit(kw + "  ", 250)
            body.append(clip("cta", s + 0.1, d - 0.1, f'<div class="ctaline">comment</div><div class="tword" '
                                                       f'style="font-size:{size}px">&ldquo;{esc(kw)}&rdquo;</div>'))
            body.append(clip("ctaarrow", s + 0.1, d - 0.1, "<i></i>", f"top:{170 + 82 + 26 + round(size * 0.9) + 30}px"))
        else:   # captions drop on the CTA
            keys = {k.upper() for k in x.get("key", [])}
            for i, w in enumerate(words):
                hot = ";color:var(--emph-accent)" if w.strip(".,'?!\"").upper() in keys else ""
                caps.append(f'<div class="clip cap" data-start="{s + i * per:.2f}" data-duration="{per * 0.92:.2f}" '
                            f'data-track-index="{900 + (len(caps) % 2)}" style="top:1400px{hot}">{esc(w.strip(".,"))}</div>')
        t = e + GAP
    total = round(t - GAP, 2)
    body.insert(0, f'<div class="clip stage" data-start="0" data-duration="{total}" data-track-index="1">{room}</div>')
    body.append(clip("label", 0, total, esc(spec.get("label", "EXAMPLE · THE SILHOUETTE STANDS IN FOR YOU"))))
    if header:
        cta_at = next((round(sum(max(1.6, len(y["say"].replace(":", "").split()) / pace) + GAP for y in spec["lines"][:i]), 2)
                       for i, y in enumerate(spec["lines"]) if y["kind"] == "cta"), total)
        body.append(clip("header", 0, cta_at, esc(header).replace("\n", "<br>")))

    grade_svg = (SKILL / "components/grade-persa.svg").read_text() if g else ""
    card_top = 1143 - 120 - round(600 * 0.81)
    doc = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"/><title>{esc(spec.get("name", "short"))}</title>
<link rel="stylesheet" href="tokens.css"/>
<link rel="stylesheet" href="persa-roles.css"/>
<style>
  .graded{{filter:url(#persa-grade)}}
  .stage{{position:absolute;left:0;top:0;width:1080px;height:1920px;z-index:1}}
  .room{{position:absolute;inset:0;background:
     radial-gradient(60% 40% at 78% 22%, color-mix(in srgb, var(--ground-2) 70%, #ffffff) 0%, transparent 70%),
     radial-gradient(90% 60% at 20% 80%, var(--ground-2) 0%, transparent 75%),
     linear-gradient(180deg, var(--ground) 0%, var(--ground-2) 100%)}}
  .room .win{{position:absolute;left:640px;top:180px;width:330px;height:520px;border-radius:14px;
     background:linear-gradient(180deg,rgba(255,240,215,.55),rgba(255,240,215,.18));filter:blur(18px)}}
  .room .lamp{{position:absolute;left:90px;top:520px;width:220px;height:220px;border-radius:50%;
     background:radial-gradient(circle,rgba(255,196,120,.75) 0%,rgba(255,196,120,0) 70%);filter:blur(6px)}}
  .room .shelf{{position:absolute;left:0;top:980px;width:1080px;height:60px;background:rgba(0,0,0,.18);filter:blur(10px)}}
  .silwrap,.cardhead{{position:absolute;left:0;top:0;width:1080px;height:1920px;z-index:7}}
  .cardhead{{z-index:4}}
  .cardhead>div{{position:absolute;left:107px;top:{card_top}px;width:875px;height:1555px}}
  .cardhead svg,.cardsil svg{{width:100%;height:100%}}
  .uiwrap{{position:absolute;left:0;top:0;width:1080px;height:1920px;z-index:2;background:#FFFFFF}}
  .uiwrap .page{{position:absolute;left:0;top:0;width:1080px;height:1920px;object-fit:cover;display:block}}
  .hlbox{{position:absolute;z-index:2;border-radius:6px;background:color-mix(in srgb, var(--emph-accent) 55%, transparent);
     mix-blend-mode:multiply}}
  .cardwrap{{position:absolute;left:114px;top:1143px;width:861px;height:777px;overflow:hidden;border-radius:var(--r-card);z-index:3}}
  .cardroom{{position:absolute;inset:0;background:linear-gradient(180deg,var(--ground-2),var(--ground))}}
  .cardsil{{position:absolute;left:-7px;top:{card_top - 1143}px;width:875px;height:1555px}}
  .annot{{background:rgba(18,18,18,.86);padding:14px 20px;border-radius:12px}}
  .shotwrap{{position:absolute;left:0;top:0;width:1080px;height:1920px;z-index:2;
     background:linear-gradient(180deg,var(--ground) 0%,var(--ground-2) 100%)}}
  .shotwin{{position:absolute;overflow:hidden;border-radius:18px;background:#fff;
     box-shadow:0 0 0 2px rgba(255,255,255,.14),0 24px 60px rgba(0,0,0,.55)}}
  .shotwin img{{position:absolute;max-width:none;display:block}}
  .shotvid{{position:absolute;z-index:2;object-fit:cover;border-radius:18px;
     box-shadow:0 0 0 2px rgba(255,255,255,.14),0 24px 60px rgba(0,0,0,.55)}}
  .shotcredit{{position:absolute;left:0;width:1080px;text-align:center;font:600 28px var(--font-ui);
     letter-spacing:.06em;color:rgba(255,255,255,.72)}}
  .shotbox{{position:absolute;z-index:2;border:7px solid var(--emph-accent);border-radius:14px;
     box-shadow:0 0 28px color-mix(in srgb, var(--emph-accent) 70%, transparent)}}
  .header{{position:absolute;left:70px;top:96px;width:940px;z-index:8;text-align:center}}
  .header{{font:800 60px/1.1 var(--font-ui);color:#111;letter-spacing:-.01em;text-transform:uppercase;
     background:#fff;border-radius:16px;padding:18px 24px;box-shadow:0 10px 30px rgba(0,0,0,.45)}}
  .numcard{{position:absolute;left:0;width:1080px;z-index:8;text-align:center;white-space:nowrap}}
  .numcard .ctag,.numcard .ctext{{display:inline-block;vertical-align:middle;font-family:var(--font-display);
     font-weight:var(--display-weight);text-transform:uppercase;line-height:1;padding:16px 26px 12px}}
  .numcard .ctag{{font-size:84px;background:var(--emph-accent);color:#111;border-radius:14px 0 0 14px}}
  .numcard .ctext{{font-size:84px;background:#fff;color:#111;border-radius:0 14px 14px 0;
     box-shadow:0 12px 30px rgba(0,0,0,.45)}}
  .numcard .ctext:only-child{{border-radius:14px}}
  .hookwords{{position:absolute;left:0;top:150px;width:1080px;text-align:center;z-index:6;
     font-family:var(--font-display);font-weight:var(--display-weight);line-height:.95;text-transform:uppercase}}
  .hookwords .hw1{{font-size:170px;color:var(--emph-fill);-webkit-text-fill-color:var(--emph-fill);
     -webkit-text-stroke-width:var(--emph-stroke);-webkit-text-stroke-color:var(--emph-white);mix-blend-mode:screen;filter:var(--glow-white)}}
  .hookwords .hw2{{font-size:230px;color:var(--display)}}
  .label{{position:absolute;left:0;top:1846px;width:1080px;text-align:center;z-index:9;
     font:600 24px var(--font-ui);letter-spacing:.08em;color:rgba(255,255,255,.82);filter:drop-shadow(0 2px 6px rgba(0,0,0,.9))}}
</style></head>
<body>
{grade_svg}
<div id="root" data-composition-id="main" data-no-timeline data-start="0" data-duration="{total}"
     data-width="1080" data-height="1920" data-fps="30">
{chr(10).join(body + caps)}
</div>
</body></html>
"""
    out.mkdir(parents=True, exist_ok=True)
    shutil.copy2(SKILL / "assets/tokens.css", out / "tokens.css")
    shutil.copy2(SKILL / "components/persa-roles.css", out / "persa-roles.css")
    shutil.copy2(SKILL / "template/hyperframes.json", out / "hyperframes.json")
    (out / "index.html").write_text(doc)
    mids, t2 = [], 0.0
    for x in spec["lines"]:
        d = max(1.6, len(x["say"].replace(":", "").split()) / pace); mids.append(round(t2 + d / 2, 2)); t2 += d + GAP
    print(json.dumps({"duration": total, "beat_middles": mids}))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("spec"); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    build(json.loads(pathlib.Path(a.spec).read_text()), pathlib.Path(os.path.expanduser(a.out)))
