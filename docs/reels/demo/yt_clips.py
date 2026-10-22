#!/usr/bin/env python3
"""yt_clips.py — splice real footage into a short, legally: check the licence, find the moment, cut it clean.

    PY=~/.cache/persa-shorts/py/bin/python
    $PY -I yt_clips.py info <url>                                   # licence, length, channel, title
    $PY -I yt_clips.py scan <url|file> <dir> [--every 10]           # a frame every N s, with timecodes -> dir/sheet-*.jpg
    $PY -I yt_clips.py cut  <url|file> <at> <dur> <out.mp4> [--crop x,y,w,h] [--licence "..."] [--credit "..."]
                                                    [--source <url>] [--permission "who said yes, when, where"]

What may be spliced (content-machine/systems/3-editor/BROLL.md):
  - YouTube videos whose licence reads "Creative Commons Attribution" (reuse allowed, with credit)
  - Microsoft Learn's animated demos (.gif from the Fabric docs, CC BY 4.0; learn_media.py collects them)
  - the creator's own recordings (--licence own)
  - anything else only with written permission (--permission), which goes into the credit record
The tool checks the licence before it downloads anything. A cut has no audio (the creator's voice runs over it), is
30fps CFR and cropped to the part that matters. Its sidecar <out>.json (size, source, licence, credit) is what
build_short.py reads for the on-screen credit; every cut is also added to credits.json in the same folder. Look at the
scan sheet first: no other presenter's face, no webcam bubble, no YouTube interface, watermark or burned-in captions.

YouTube bot-checks this container after a few requests (HTTP 429, "confirm you're not a bot"): one scan and one or two
cuts per video, minutes apart. If it refuses, download on your computer (yt-dlp -f "bv*[height<=1080][ext=mp4]" <url>),
drop the file into the session, and pass it with --source <url> --licence "<what the video page says>".
"""
import argparse, json, os, re, shutil, subprocess, sys, tempfile

YT = ["yt-dlp", "--no-warnings"] + (["--js-runtimes", "node"] if shutil.which("node") else [])


def run(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode:
        sys.exit(f"yt_clips: {' '.join(cmd[:3])}… failed:\n{(r.stderr or r.stdout).strip()[-600:]}")
    return r.stdout


def is_url(s):
    return s.startswith(("http://", "https://"))


def info(url):
    out = run(YT + ["--skip-download", "--print", "%(license)s\t%(duration)s\t%(channel)s\t%(title)s\t%(id)s", url])
    lic, dur, ch, title, vid = out.strip().split("\t")[:5]
    return dict(licence=lic if lic != "NA" else "standard YouTube licence", duration=float(dur) if dur != "NA" else 0,
                channel=ch, title=title, url=f"https://www.youtube.com/watch?v={vid}")


def gate(meta, a):
    lic = (a.licence or meta.get("licence") or "").strip()
    if a.permission:
        return lic or "used with permission"
    if re.search(r"creative commons|cc[ -]?by|\bown\b", lic, re.I) and not re.search(r"\b(nc|nd)\b|-nc|-nd|non-?commercial|no ?deriv", lic, re.I):
        return lic
    sys.exit(f"yt_clips: '{meta.get('title', meta.get('source'))}' is under '{lic or 'an unknown licence'}'. Only "
             "Creative Commons Attribution, Microsoft Learn's CC BY 4.0 demos and your own recordings can be spliced "
             "without asking. Ask the creator, then pass --permission \"who said yes, when, where\".")


def source_meta(src, a):
    if is_url(src):
        return info(src)
    if not a.licence and not a.permission:
        sys.exit("yt_clips: a local file needs --licence (\"own\", \"CC BY 4.0\", what the video page says) or --permission")
    return dict(licence=a.licence or "", title=a.title or os.path.basename(src), channel=a.channel or "", url=a.source or "",
                duration=0, source=src)


def frames_sheet(video, outdir, every):
    from PIL import Image, ImageDraw
    fdir = os.path.join(outdir, "frames"); os.makedirs(fdir, exist_ok=True)
    run(["ffmpeg", "-v", "error", "-y", "-i", video, "-vf", f"fps=1/{every},scale=360:-2", os.path.join(fdir, "f%04d.jpg")])
    fs = sorted(os.listdir(fdir))
    cols, per = 5, 20
    for k in range(0, len(fs), per):
        chunk = fs[k:k + per]
        ims = [Image.open(os.path.join(fdir, f)).convert("RGB") for f in chunk]
        w, h = ims[0].size
        sheet = Image.new("RGB", (cols * (w + 6), ((len(ims) + cols - 1) // cols) * (h + 26)), "white")
        for j, im in enumerate(ims):
            x, y = (j % cols) * (w + 6), (j // cols) * (h + 26)
            sheet.paste(im, (x, y + 22))
            t = (k + j) * every
            ImageDraw.Draw(sheet).text((x + 4, y + 4), f"{t // 60}:{t % 60:02d}", fill="black")
        sheet.save(os.path.join(outdir, f"sheet-{k // per:02d}.jpg"), quality=80)
    return len(fs)


def vtt_to_text(vtt):
    out, last = [], ""
    for block in open(vtt, encoding="utf-8").read().split("\n\n"):
        m = re.search(r"(\d+):(\d\d):(\d\d)\.\d+ -->", block)
        if not m:
            continue
        text = re.sub(r"<[^>]+>", "", block.split("\n", 1)[1] if "\n" in block else "")
        text = " ".join(l.strip() for l in text.splitlines() if "-->" not in l).strip()
        if text and text != last:
            s = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + int(m.group(3))
            out.append(f"{s // 60}:{s % 60:02d}  {text}"); last = text
    return "\n".join(out)


def cmd_scan(a):
    os.makedirs(a.dir, exist_ok=True)
    meta = source_meta(a.src, a)
    meta["licence"] = gate(meta, a)
    video = a.src
    if is_url(a.src):
        video = os.path.join(a.dir, "low.mp4")
        if not os.path.exists(video):
            run(YT + ["-f", "160/278/133/242/worstvideo[ext=mp4]/worstvideo", "-o", video, a.src])
        try:   # the transcript helps find the moment; YouTube often refuses it from here, so it is optional
            run(YT + ["--skip-download", "--write-auto-subs", "--write-subs", "--sub-langs", "en.*,en", "--sub-format", "vtt",
                      "-o", os.path.join(a.dir, "subs"), a.src])
            vtts = [f for f in os.listdir(a.dir) if f.endswith(".vtt")]
            if vtts:
                open(os.path.join(a.dir, "transcript.txt"), "w").write(vtt_to_text(os.path.join(a.dir, vtts[0])))
        except SystemExit as e:
            print(f"  (no transcript: {str(e).splitlines()[-1][:120]})", file=sys.stderr)
    n = frames_sheet(video, a.dir, a.every)
    json.dump(meta, open(os.path.join(a.dir, "source.json"), "w"), indent=1)
    print(f"{meta['title']} · {meta['channel']} · {meta['licence']}\n{n} frames every {a.every}s -> {a.dir}/sheet-*.jpg"
          + (" + transcript.txt" if os.path.exists(os.path.join(a.dir, "transcript.txt")) else ""))


def secs(tc):
    p = [float(x) for x in str(tc).split(":")]
    return p[0] if len(p) == 1 else p[0] * 60 + p[1] if len(p) == 2 else p[0] * 3600 + p[1] * 60 + p[2]


def cmd_cut(a):
    meta = source_meta(a.src, a)
    meta["licence"] = gate(meta, a)
    at, dur = secs(a.at), float(a.dur)
    out = os.path.abspath(a.out); os.makedirs(os.path.dirname(out), exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        src, offset = a.src, at
        if is_url(a.src):
            raw = os.path.join(tmp, "raw.mp4")
            run(YT + ["-f", "bv*[height<=1080][ext=mp4]/bv*[height<=1080]/bv*", "--download-sections",
                      f"*{max(0, at - 1):.2f}-{at + dur + 1:.2f}", "--force-keyframes-at-cuts", "-o", raw, a.src])
            src, offset = raw, min(1.0, at)
        vf = []
        if a.crop:
            x, y, w, h = [int(v) for v in a.crop.split(",")]
            vf.append(f"crop={w}:{h}:{x}:{y}")
        vf += ["scale=trunc(iw/2)*2:trunc(ih/2)*2", "fps=30"]
        run(["ffmpeg", "-v", "error", "-y", "-ss", f"{offset:.3f}", "-i", src, "-t", f"{dur:.3f}", "-vf", ",".join(vf),
             "-an", "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", "-g", "30", "-movflags", "+faststart", out])
    probe = run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height:format=duration",
                 "-of", "json", out])
    p = json.loads(probe)
    lic = meta["licence"]
    short = lic if re.match(r"cc by", lic, re.I) else "CC BY" if re.search(r"creative commons", lic, re.I) else lic
    who = a.channel or meta.get("channel") or ""
    credit = a.credit or (f"VIDEO: {who.upper()} · {short.upper()}" if who else short.upper())
    side = dict(width=p["streams"][0]["width"], height=p["streams"][0]["height"], duration=float(p["format"]["duration"]),
                source=a.source or meta.get("url") or a.src, title=meta.get("title", ""), channel=who,
                licence=meta["licence"], at=at, dur=dur, crop=a.crop or "", permission=a.permission or "", credit=credit,
                post_credit=(f'Clip: {who}, "{meta.get("title", "")}" ({a.source or meta.get("url", "")}), '
                             f'{meta["licence"]}{", cropped" if a.crop else ""}{", " + a.permission if a.permission else ""}'))
    json.dump(side, open(os.path.splitext(out)[0] + ".json", "w"), indent=1)
    cj = os.path.join(os.path.dirname(out), "credits.json")
    rows = json.load(open(cj)) if os.path.exists(cj) else []
    rows = [r for r in rows if r.get("file") != os.path.basename(out)] + [dict(file=os.path.basename(out), **side)]
    json.dump(rows, open(cj, "w"), indent=1)
    print(f"{out}: {side['width']}x{side['height']}, {side['duration']:.1f}s\n  on screen: {credit}\n  in the post: {side['post_credit']}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("info"); s.add_argument("src")
    for name in ("scan", "cut"):
        s = sub.add_parser(name); s.add_argument("src")
        if name == "scan":
            s.add_argument("dir"); s.add_argument("--every", type=int, default=10)
        else:
            s.add_argument("at"); s.add_argument("dur"); s.add_argument("out"); s.add_argument("--crop")
            s.add_argument("--credit")
        s.add_argument("--licence"); s.add_argument("--permission"); s.add_argument("--source"); s.add_argument("--channel")
        s.add_argument("--title")
    a = ap.parse_args()
    if a.cmd == "info":
        print(json.dumps(info(a.src), indent=1))
    elif a.cmd == "scan":
        cmd_scan(a)
    else:
        cmd_cut(a)
