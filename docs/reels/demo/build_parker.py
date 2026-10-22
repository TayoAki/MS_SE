#!/usr/bin/env python3
"""build_parker.py — a faceless, voiced example cut in the Parker Prompts style (content-machine/formats.md, "House
style"): a dark product world where the picture changes every few seconds, real screens in a glowing window, text
cards with the key words lit, giant outlined numbers, stage words in big yellow caps, small chunked captions.

    PY=~/.cache/persa-shorts/py/bin/python
    $PY -I docs/reels/demo/voice.py spec.json --out OUT          # the AI stand-in voice + line lengths
    python3 -I docs/reels/demo/build_parker.py spec.json --out OUT  # the composition, timed to the voice
    (or docs/reels/demo/make_example.sh spec.json OUT: voice, build, check, render, mux)

Each spoken line is one beat; "say" is spoken and captioned, the rest says what the picture is:
  {"kind": "cover", "big": ["LINE 1", "LINE 2"], "sub": "small line"}     the first frame: LinkedIn's thumbnail
  {"kind": "text", "show": "It's the *wrong question*."}                  a sentence card, *words* lit yellow
  {"kind": "num", "n": "1", "title": "PICK YOUR EXAM", "sub": "DP-700"}   a giant outlined number + its name
  {"kind": "stack", "items": [["GET DATA IN", "getting"], ...]}            stage words in big yellow caps, each on
                                                                          the spoken word it names
  {"kind": "options", "q": "Which storage mode?", "items": [...], "answer": 2, "reveal": true}
  {"kind": "chart", "title": "...", "bars": [["Illegal parking", 611282], ...], "note": "source"}
  {"kind": "shot", "src": "assets/x.png", "crop": [x, y, w, h], "box": [[x, y, w, h]], "credit": "..."}
  {"kind": "clip", "src": "assets/clips/x.mp4"}                           a cut from yt_clips.py (credit in its .json)
  {"kind": "cta", "keyword": "WORD"} or {"kind": "cta", "text": "FOLLOW"}
optional on any line: "pill": "STEP 1" (a tag above the picture), "key": ["word", ...] (caption words lit),
"tts": "how to say it". On the spec: "label" (bottom line), "pace" (words a second when there is no voice yet).
"""
import argparse, html, json, os, pathlib, re, shutil, sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from build_short import img_size, SKILL   # noqa: E402

GAP = 0.25
ZONE_TOP, ZONE_H, ZONE_W = 300, 1080, 1000     # where pictures live; captions sit below at 1560


def esc(s):
    return html.escape(str(s), quote=True)


def lit(s):
    """*word* -> lit span (yellow)."""
    return re.sub(r"\*(.+?)\*", r'<span class="lit">\1</span>', esc(s))


def norm(w):
    return re.sub(r"[^\w%$'-]", "", w).upper().replace("’", "'")


def fit(text, cap, width=960, em=0.72):
    """A font size that keeps one line of capitals inside the width (~0.72em a capital in Montserrat 900)."""
    return min(cap, int(width / (em * max(1, len(text)))))


def build(spec, out):
    vj = out / "voice.json"
    durs = json.loads(vj.read_text())["durations"] if vj.exists() else None
    pace = spec.get("pace", 2.9)
    tr = [20]
    body, caps = [], []

    def clip(cls, s, d, inner="", style="", extra=""):
        tr[0] += 1
        st = f' style="{style}"' if style else ""
        return (f'<div class="clip {cls}" data-start="{s:.2f}" data-duration="{max(0.1, d):.2f}" '
                f'data-track-index="{tr[0]}"{extra}{st}>{inner}</div>')

    t = 0.0
    for k, x in enumerate(spec["lines"]):
        words = x["say"].split()
        d = durs[k] if durs else max(1.6, len(words) / pace)
        s, e = t, t + d
        wts = [len(re.sub(r"\W", "", w)) + 2 for w in words]          # word onsets, spread by length
        on = [s + d * sum(wts[:i]) / sum(wts) for i in range(len(words))]

        def at_word(w):
            for i, x_ in enumerate(words):
                if norm(x_) == norm(w):
                    return on[i]
            sys.exit(f"build_parker: '{w}' is not spoken in line {k + 1}: {x['say']}")

        kind = x["kind"]
        if k:   # the flash cut between beats
            body.append(clip("flash", s - 0.06, 0.22))
        if x.get("pill"):
            body.append(clip("pill", s + 0.05, d - 0.05, f'<span>{esc(x["pill"])}</span>'))
        if kind == "cover":
            a, b = (x["big"] + [""])[:2]
            body.append(clip("cover", s, d, f'<div class="c1" style="font-size:{fit(a, 132)}px">{esc(a)}</div>'
                                            f'<div class="c2" style="font-size:{fit(b, 132)}px">{esc(b)}</div>'
                                            + (f'<div class="csub">{esc(x["sub"])}</div>' if x.get("sub") else "")))
        elif kind == "text":
            body.append(clip("card", s, d, f'<div>{lit(x["show"])}</div>'))
        elif kind == "num":
            body.append(clip("num", s, d, f'<div class="n" style="font-size:{fit(x["n"], 560, 980, 0.52)}px">{esc(x["n"])}</div><div class="nt">{esc(x.get("title", ""))}</div>'
                                          + (f'<div class="ns">{esc(x["sub"])}</div>' if x.get("sub") else "")))
        elif kind == "stack":
            n = len(x["items"])
            for j, (label, w) in enumerate(x["items"]):
                a0 = max(s, at_word(w) - 0.15) if w else s + 0.2 + j * 0.3
                top = 960 - n * 75 + j * 150
                body.append(clip("stackw", a0, e - a0, esc(label), f"top:{top}px;font-size:{fit(label, 112, 1000)}px"))
        elif kind == "options":
            rows = []
            for j, it in enumerate(x["items"]):
                cls = "opt" + (" win" if x.get("reveal") and j == x.get("answer") else " dim" if x.get("reveal") else "")
                rows.append(f'<div class="{cls}"><span class="ol">{"ABCD"[j]}</span><span>{esc(it)}</span></div>')
            body.append(clip("options", s, d, f'<div class="oq">{esc(x.get("q", ""))}</div>' + "".join(rows)))
        elif kind == "chart":
            mx = max(v for _, v in x["bars"])
            rows = "".join(
                f'<div class="bar"><div class="bl">{esc(lb)}</div><div class="bt"><i style="width:{max(3, v / mx * 100):.1f}%"'
                f'{" class=top" if j == 0 else ""}></i></div><div class="bv">{v:,}</div></div>'
                for j, (lb, v) in enumerate(x["bars"]))
            body.append(clip("chart", s, d, f'<div class="ct">{esc(x.get("title", ""))}</div>{rows}'
                                            + (f'<div class="cn">{esc(x["note"])}</div>' if x.get("note") else "")))
        elif kind in ("shot", "clip"):
            if kind == "shot":
                W, H = img_size(out / x["src"])
                credit = x.get("credit", spec.get("shot_credit", ""))
            else:
                meta = json.loads((out / pathlib.Path(x["src"]).with_suffix(".json")).read_text())
                W, H, credit = meta["width"], meta["height"], x.get("credit", meta["credit"])
            cx, cy, cw, ch = x.get("crop") or [0, 0, W, H]
            z = min(ZONE_W / cw, ZONE_H / ch)
            ww, wh = round(cw * z), round(ch * z)
            left, top = (1080 - ww) // 2, ZONE_TOP + (ZONE_H - wh) // 2
            body.append(clip("credit", s, d, esc(credit), f"top:{top - 52}px"))
            if kind == "shot":
                body.append(clip("win", s, d, f'<img src="{esc(x["src"])}" alt="" style="left:{-cx * z:.0f}px;'
                                              f'top:{-cy * z:.0f}px;width:{W * z:.0f}px;height:{H * z:.0f}px">',
                                 f"left:{left}px;top:{top}px;width:{ww}px;height:{wh}px"))
            else:   # a timed <video> of its own, with an id, or it renders frozen
                tr[0] += 1
                body.append(f'<video class="clip vid" id="v{tr[0]}" src="{esc(x["src"])}" data-start="{s:.2f}" '
                            f'data-duration="{d:.2f}" data-media-start="0" data-track-index="{tr[0]}" muted playsinline '
                            f'style="left:{left}px;top:{top}px;width:{ww}px;height:{wh}px"></video>')
            for bx, by, bw, bh in x.get("box", []):
                body.append(clip("box", s + 0.35, d - 0.4, "", f"left:{left + (bx - cx) * z - 8:.0f}px;"
                                 f"top:{top + (by - cy) * z - 8:.0f}px;width:{bw * z + 16:.0f}px;height:{bh * z + 16:.0f}px"))
        elif kind == "cta":
            word = x.get("keyword") or x.get("text", "FOLLOW")
            big = f'&ldquo;{esc(word.upper())}&rdquo;' if x.get("keyword") else esc(word.upper())
            size = min(200, int(1000 / (0.72 * (len(word) + (2 if x.get("keyword") else 0)))))   # ~0.72em a capital
            pre = x.get("pre", "comment" if x.get("keyword") else "")
            body.append(clip("cta", s, d, f'<div class="ca">{esc(pre)}</div><div class="cb" style="font-size:{size}px">{big}</div>'))
        else:
            sys.exit(f"build_parker: line {k + 1} has an unknown kind '{kind}'")
        # captions: 1-4 words a chunk, broken at punctuation, the key words lit
        keys = {norm(w) for w in x.get("key", [])}
        chunk, chunks = [], []
        for i, w in enumerate(words):
            chunk.append(i)
            if len(chunk) == 4 or re.search(r"[.,:;?!]$", w):
                chunks.append(chunk); chunk = []
        if chunk:
            chunks.append(chunk)
        for j, c in enumerate(chunks):
            c0 = on[c[0]]; c1 = on[chunks[j + 1][0]] if j + 1 < len(chunks) else e
            txt = " ".join(f'<span class="lit">{esc(words[i])}</span>' if norm(words[i]) in keys else esc(words[i]) for i in c)
            caps.append(f'<div class="clip cap2" data-start="{c0:.2f}" data-duration="{max(0.2, c1 - c0 - 0.02):.2f}" '
                        f'data-track-index="{900 + j % 2}">{txt}</div>')
        t = e + GAP
    total = round(t - GAP, 2)

    doc = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"/><title>{esc(spec.get("name", "short"))}</title>
<link rel="stylesheet" href="tokens.css"/>
<style>
  body{{margin:0;background:#07080B}}
  .clip{{position:absolute}}
  .ground{{left:0;top:0;width:1080px;height:1920px;z-index:1;background:
     radial-gradient(70% 40% at 50% 34%, color-mix(in srgb, var(--display) 16%, transparent) 0%, transparent 70%),
     radial-gradient(60% 35% at 80% 92%, color-mix(in srgb, var(--emph-accent) 10%, transparent) 0%, transparent 70%),
     linear-gradient(180deg,#0B0D12 0%,#07080B 100%)}}
  .flash{{left:0;top:0;width:1080px;height:1920px;z-index:9;
     background:radial-gradient(60% 45% at 50% 45%, color-mix(in srgb, var(--display) 34%, transparent), transparent 75%)}}
  .pill{{left:0;top:190px;width:1080px;z-index:6;text-align:center}}
  .pill span{{display:inline-block;font:800 34px/1 var(--font-ui);letter-spacing:.14em;color:#0B0D12;text-transform:uppercase;
     background:var(--emph-accent);padding:16px 30px;border-radius:999px}}
  .cover{{left:60px;top:560px;width:960px;z-index:5;text-align:center}}
  .cover .c1{{font:900 132px/0.98 Montserrat,var(--font-ui);color:#fff;text-transform:uppercase;letter-spacing:-.02em}}
  .cover .c2{{font:900 132px/0.98 Montserrat,var(--font-ui);color:var(--emph-accent);text-transform:uppercase;letter-spacing:-.02em;margin-top:10px}}
  .cover .csub{{font:600 44px/1.3 var(--font-ui);color:rgba(255,255,255,.72);margin-top:40px}}
  .card{{left:70px;top:520px;width:940px;height:760px;z-index:5;display:flex;align-items:center;justify-content:center;text-align:center}}
  .card div{{font:800 86px/1.12 var(--font-ui);color:#fff;letter-spacing:-.015em}}
  .lit{{color:var(--emph-accent)}}
  .num{{left:0;top:330px;width:1080px;z-index:5;text-align:center}}
  .num .n{{font:400 560px/0.9 var(--font-display);color:var(--emph-fill);-webkit-text-fill-color:var(--emph-fill);
     -webkit-text-stroke:7px var(--display);filter:drop-shadow(0 0 24px color-mix(in srgb, var(--display) 80%, transparent))}}
  .num .nt{{font:900 92px/1.05 Montserrat,var(--font-ui);color:#fff;text-transform:uppercase;margin-top:30px;padding:0 60px}}
  .num .ns{{font:600 46px/1.3 var(--font-ui);color:rgba(255,255,255,.72);margin-top:22px;padding:0 80px}}
  .stackw{{left:0;width:1080px;z-index:5;text-align:center;font:900 112px/1 Montserrat,var(--font-ui);
     color:var(--emph-accent);text-transform:uppercase;letter-spacing:-.01em;filter:drop-shadow(0 6px 18px rgba(0,0,0,.6))}}
  .options{{left:90px;top:420px;width:900px;z-index:5}}
  .options .oq{{font:800 70px/1.15 var(--font-ui);color:#fff;margin-bottom:46px;text-align:center}}
  .opt{{display:flex;align-items:center;gap:30px;margin:0 0 30px;padding:28px 34px;border-radius:24px;
     background:rgba(255,255,255,.07);box-shadow:inset 0 0 0 2px rgba(255,255,255,.14);font:700 60px/1 var(--font-ui);color:#fff}}
  .opt .ol{{display:inline-flex;align-items:center;justify-content:center;width:86px;height:86px;border-radius:50%;
     background:rgba(255,255,255,.12);font:900 50px/1 Montserrat,var(--font-ui)}}
  .opt.win{{background:color-mix(in srgb, var(--display) 26%, transparent);box-shadow:inset 0 0 0 4px var(--display),0 0 40px color-mix(in srgb, var(--display) 50%, transparent)}}
  .opt.win .ol{{background:var(--display);color:#0B0D12}}
  .opt.dim{{opacity:.35}}
  .chart{{left:70px;top:330px;width:940px;z-index:5}}
  .chart .ct{{font:800 62px/1.15 var(--font-ui);color:#fff;margin-bottom:40px}}
  .bar{{display:grid;grid-template-columns:330px 1fr 190px;align-items:center;gap:18px;margin-bottom:26px}}
  .bar .bl{{font:700 38px/1.15 var(--font-ui);color:#fff}}
  .bar .bt{{height:58px;background:rgba(255,255,255,.07);border-radius:12px;overflow:hidden}}
  .bar .bt i{{display:block;height:100%;background:var(--display);border-radius:12px}}
  .bar .bt i.top{{background:var(--emph-accent)}}
  .bar .bv{{font:800 40px/1 var(--font-ui);color:#fff;text-align:right}}
  .chart .cn{{font:500 28px/1.3 var(--font-ui);color:rgba(255,255,255,.55);margin-top:24px}}
  .win{{z-index:4;overflow:hidden;border-radius:22px;background:#fff;
     box-shadow:0 0 0 2px color-mix(in srgb, var(--display) 55%, transparent),0 0 60px color-mix(in srgb, var(--display) 28%, transparent),0 30px 80px rgba(0,0,0,.6)}}
  .win img{{position:absolute;max-width:none;display:block}}
  .vid{{z-index:4;object-fit:cover;border-radius:22px;
     box-shadow:0 0 0 2px color-mix(in srgb, var(--display) 55%, transparent),0 0 60px color-mix(in srgb, var(--display) 28%, transparent),0 30px 80px rgba(0,0,0,.6)}}
  .box{{z-index:5;border:7px solid var(--emph-accent);border-radius:14px;box-shadow:0 0 28px color-mix(in srgb, var(--emph-accent) 70%, transparent)}}
  .credit{{left:0;width:1080px;z-index:5;text-align:center;font:600 28px/1 var(--font-ui);letter-spacing:.08em;color:rgba(255,255,255,.6)}}
  .cta{{left:0;top:600px;width:1080px;z-index:5;text-align:center}}
  .cta .ca{{font:800 64px/1 var(--font-ui);color:#fff;text-transform:uppercase;letter-spacing:.06em}}
  .cta .cb{{font:900 200px/1.05 Montserrat,var(--font-ui);color:var(--display);text-transform:uppercase;margin-top:24px;
     filter:drop-shadow(0 0 30px color-mix(in srgb, var(--display) 60%, transparent))}}
  .cap2{{left:60px;top:1560px;width:960px;z-index:8;text-align:center;font:800 60px/1.15 var(--font-ui);color:#fff;
     text-shadow:0 4px 18px rgba(0,0,0,.85)}}
  .label{{left:0;top:1846px;width:1080px;text-align:center;z-index:9;font:600 24px var(--font-ui);letter-spacing:.08em;color:rgba(255,255,255,.7)}}
</style></head>
<body>
<div id="root" data-composition-id="main" data-no-timeline data-start="0" data-duration="{total}"
     data-width="1080" data-height="1920" data-fps="30">
<div class="clip ground" data-start="0" data-duration="{total}" data-track-index="1"></div>
{chr(10).join(body + caps)}
<div class="clip label" data-start="0" data-duration="{total}" data-track-index="2">{esc(spec.get("label", "EXAMPLE · AI STAND-IN VOICE · NO FACE"))}</div>
</div>
</body></html>
"""
    out.mkdir(parents=True, exist_ok=True)
    shutil.copy2(SKILL / "assets/tokens.css", out / "tokens.css")
    shutil.copy2(SKILL / "template/hyperframes.json", out / "hyperframes.json")
    (out / "index.html").write_text(doc)
    print(json.dumps({"duration": total, "voiced": bool(durs)}))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("spec"); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    build(json.loads(pathlib.Path(a.spec).read_text()), pathlib.Path(os.path.expanduser(a.out)))
