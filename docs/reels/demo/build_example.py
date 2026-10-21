#!/usr/bin/env python3
"""build_example.py — an example of Script 3 ("We counted the same patients three ways") as a finished 9:16 short,
before anything is recorded.

    python3 -I docs/reels/demo/build_example.py --out <folder>          # then: npx --yes hyperframes render <folder> ...

It builds a HyperFrames composition with the Persa Shorts brand (tokens.css, persa-roles.css): the creator is the
theme preview's stand-in room and silhouette, and every "screen" beat is a SQL editor showing the real query and the
real result, computed here from the synthetic month (synthetic_month.py, seed 20261123) — no number is typed in by
hand. Swap the silhouette for the real take with nextphase-persa-shorts once the script is recorded.
"""
import argparse, csv, html, json, os, pathlib, shutil, sqlite3, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
SKILL = pathlib.Path(os.path.expanduser("~/.claude/skills/nextphase-persa-shorts"))
PACE = 2.75          # words per second, a calm talking-head pace
GAP = 0.25           # breath between lines


def esc(s):
    return html.escape(str(s), quote=True)


def load_data(folder):
    if not (folder / "encounters.csv").exists():
        subprocess.run([sys.executable, "-I", str(HERE / "synthetic_month.py"), str(folder)], check=True,
                       stdout=subprocess.DEVNULL)
    db = sqlite3.connect(":memory:")
    db.execute("create table encounters(encounter_id, patient_id, visit_date)")
    db.execute("create table encounter_diagnoses(encounter_id, icd10)")
    for t in ("encounters", "encounter_diagnoses"):
        rows = list(csv.reader(open(folder / f"{t}.csv")))[1:]
        db.executemany(f"insert into {t} values ({','.join('?' * len(rows[0]))})", rows)
    return db


QUERIES = {
    "q1": "SELECT COUNT(*) AS visits\nFROM encounters;",
    "q2": "SELECT COUNT(*) AS rows\nFROM encounters e\nJOIN encounter_diagnoses d\n  ON d.encounter_id = e.encounter_id;",
    "q3": "SELECT COUNT(DISTINCT patient_id)\n  AS patients\nFROM encounters;",
}


def editor(title, sql, result_head, result_rows, big=None):
    """A neutral SQL editor (a stand-in for the creator's own screen recording): query on top, result below,
    everything above the camera card (y < 1100)."""
    code = "".join(f"<div>{esc(l) or '&nbsp;'}</div>" for l in sql.split("\n"))
    if big is not None:
        res = f'<div class="bigres"><span>{esc(result_head[0])}</span><b>{big:,}</b></div>'
    else:
        head = "".join(f"<th>{esc(h)}</th>" for h in result_head)
        body = "".join("<tr>" + "".join(f"<td>{esc(c)}</td>" for c in r) + "</tr>" for r in result_rows)
        res = f'<table class="grid"><tr>{head}</tr>{body}</table>'
    return (f'<div class="sql"><div class="bar"><i></i><i></i><i></i><span>{esc(title)}</span></div>'
            f'<div class="code">{code}</div><div class="restab">Results · synthetic data</div>{res}</div>')


def build(out, data):
    db = load_data(data)
    n1 = db.execute("select count(*) from encounters").fetchone()[0]
    n2 = db.execute("select count(*) from encounters e join encounter_diagnoses d on d.encounter_id = e.encounter_id").fetchone()[0]
    n3 = db.execute("select count(distinct patient_id) from encounters").fetchone()[0]
    # one patient who came back, with the visit that carries three diagnoses: the rows the join multiplies
    pid = db.execute("""select e.patient_id from encounters e join encounter_diagnoses d on d.encounter_id = e.encounter_id
                        group by e.patient_id having count(distinct e.encounter_id) >= 2 and count(*) >= 4
                        order by e.patient_id limit 1""").fetchone()[0]
    joined = db.execute("""select e.encounter_id, e.patient_id, e.visit_date, d.icd10 from encounters e
                           join encounter_diagnoses d on d.encounter_id = e.encounter_id
                           where e.patient_id = ? order by e.visit_date, e.encounter_id limit 6""", (pid,)).fetchall()
    brand = json.loads((SKILL / "brand/brand.json").read_text())
    kw = "COUNTS"

    lines = [  # (spoken line, beat kind, beat details) — the script, docs/reels/fabric-health-systems-scripts.md #3
        (f"We counted one month of patients three ways. We got {n3}, {n1} and {n2}.", "hook", {"broll": "corridor"}),
        ("Same data. Three queries. Here's what each one actually counted.", "face", {"emph": ("THREE", "w")}),
        (f"Query one: count the rows in the visits table. {n1}.", "ui", {"ui": editor("query 1 · visits", QUERIES["q1"], ["visits"], [], n1), "annot": "= VISITS"}),
        ("That's visits, not patients. Anyone who came back is counted again.", "face", {"emph": ("AGAIN", "a")}),
        (f"Query two: join the diagnoses first, then count. {n2}.", "ui", {"ui": editor("query 2 · join first", QUERIES["q2"], ["rows"], [], n2), "annot": "= VISIT ×\nDIAGNOSIS"}),
        ("Every extra diagnosis on a visit adds another row.", "ui", {"ui": editor(f"one patient · {pid}", f"SELECT ... WHERE patient_id = '{pid}';", ["encounter", "patient", "date", "icd10"], joined), "annot": "SAME VISIT,\nMORE ROWS"}),
        (f"Query three: count distinct patient IDs. {n3}.", "ui", {"ui": editor("query 3 · distinct", QUERIES["q3"], ["patients"], [], n3), "annot": "= PATIENTS"}),
        ("That's the answer to how many patients did we see.", "face", {"payoff": str(n3), "broll": "waiting-room"}),
        (f"And even {n3} is wrong if one person ended up with two patient IDs.", "ui", {"ui": editor("possible duplicates · synthetic", "SELECT patient_id, name, birth_date\nFROM patients WHERE ...;", ["patient", "name", "birth date"], [("P0007", "A. Rivera", "1961-03-14"), ("P0391", "A. Rivera", "1961-03-14")]), "annot": "SAME\nPERSON?"}),
        ("So before a count goes on a dashboard: name the grain, check rows across every join, label the question.", "list", {"items": ["NAME THE GRAIN", "CHECK EVERY JOIN", "LABEL THE QUESTION"]}),
        ("Most teams argue about which number is right. The fix is agreeing what each number means.", "face", {"emph": ("RIGHT", "w"), "payoff_late": "MEANS"}),
        (f"Comment {kw} and I'll send you the five checks I'd run before a patient count reaches a CFO.", "cta", {}),
    ]

    adv = 0.5
    for ln in (SKILL / "assets/tokens.css").read_text().splitlines():
        if "--display-advance:" in ln:
            adv = float(ln.split(":")[1].split(";")[0])
    fit = lambda w, cap=290, box=940: max(60, min(cap, int(box / (adv * max(1, len(w))))))

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

    g = ' class="graded"' if brand.get("grade", "film") == "film" else ""
    broll = {p.stem: f"assets/broll/{p.name}" for p in (out / "assets/broll").glob("*.jpg") if p.stat().st_size > 0} \
        if (out / "assets/broll").exists() else {}
    room = f'<div class="room"{g}><i class="win"></i><i class="lamp"></i><i class="shelf"></i></div>'
    body, caps, t = [], [], 0.0
    for k, (say, kind, x) in enumerate(lines):
        words = say.replace(":", "").split()
        d = max(1.6, len(words) / PACE)
        s, e = t, t + d
        src = broll.get(x.get("broll", ""))
        if src and kind == "hook":      # the hook opens on the real place, then cuts to the creator
            cut = s + d * 0.5
            body.append(clip("brollwrap", s, cut - s, f'<img class="broll{" graded" if g else ""}" src="{src}" alt="">'))
            body.append(clip("vig", s, d))
            body.append(clip("silwrap", cut, e - cut, f"<div{g}>{sil(f's{k}')}</div>"))
        elif src:                       # the line names the place: the real place owns the frame
            body.append(clip("brollwrap", s, d, f'<img class="broll{" graded" if g else ""}" src="{src}" alt="">'))
            body.append(clip("vig", s, d))
        elif kind in ("face", "hook", "list", "cta"):
            body.append(clip("vig", s, d))
            body.append(clip("silwrap", s, d, f"<div{g}>{sil(f's{k}')}</div>"))
        if kind == "hook":
            nums = (f'<span class="pn">{n3}</span><span class="pw">{n1}</span><span class="pa">{n2}</span>')
            body.append(clip("hooknums", s, d, nums))
        per = d / len(words)
        on_word = lambda w: s + per * next(i for i, x_ in enumerate(words) if x_.strip(".,'?").upper() == w)  # lands ON the word
        if kind == "face" and "emph" in x:
            w, tone = x["emph"]
            at = max(s, on_word(w) - 0.5)
            body.append(clip(f"emph e-{tone}", at, max(1.0, min(1.6, e - at)), w, f"top:300px;font-size:{fit(w)}px"))
        if kind == "face" and "payoff" in x:
            w = x["payoff"]
            body.append(clip("payoff", s + 0.2, d - 0.3, w, f"top:250px;font-size:{fit(w, 300)}px"))
        if kind == "face" and "payoff_late" in x:
            w = x["payoff_late"]
            at = max(s, on_word(w) - 0.5)
            body.append(clip("payoff", at, max(1.0, e - at), w, f"top:300px;font-size:{fit(w)}px"))
        if kind == "ui":
            body.append(clip("uiwrap", s, d, x["ui"]))
            body.append(clip("annot", s + 0.4, d - 0.5, esc(x["annot"]).replace("\n", "<br>"), "left:70px;top:905px;font-size:50px"))
            body.append(clip("cardwrap", s, d, f'<div class="cardroom"{g}></div><div class="cardsil"{g}>{sil(f"c{k}")}</div>'))
            body.append(clip("cardhead", s, d, f"<div{g}>{sil(f'h{k}')}</div>"))
        if kind == "list":
            for i, item in enumerate(x["items"]):
                at = s + 0.3 + i * d / 3.2
                body.append(clip("pillrow", at, e - at, f'<span class="tpill big">{esc(item)}</span>', f"top:{250 + i * 120}px"))
        if kind == "cta":
            size = fit(kw + "  ", 250)
            body.append(clip("cta", s + 0.1, d - 0.1, f'<div class="ctaline">comment</div><div class="tword" '
                                                       f'style="font-size:{size}px">&ldquo;{esc(kw)}&rdquo;</div>'))
            body.append(clip("ctaarrow", s + 0.1, d - 0.1, "<i></i>", f"top:{170 + 82 + 26 + round(size * 0.9) + 30}px"))
        if kind != "cta":   # captions drop on the CTA
            for i, w in enumerate(words):
                caps.append(f'<div class="clip cap" data-start="{s + i * per:.2f}" data-duration="{per * 0.92:.2f}" '
                            f'data-track-index="{900 + (len(caps) % 2)}" style="top:1400px">{esc(w.strip(".,"))}</div>')
        t = e + GAP
    total = round(t - GAP, 2)
    body.insert(0, f'<div class="clip stage" data-start="0" data-duration="{total}" data-track-index="1">{room}</div>')
    body.append(clip("label", 0, total, "EXAMPLE · SYNTHETIC DATA · THE SILHOUETTE STANDS IN FOR YOU"))
    credits = out / "assets/broll/credits.json"
    used = [c for c in (json.loads(credits.read_text()) if credits.exists() else []) if pathlib.Path(c["file"]).stem in broll]

    grade_svg = (SKILL / "components/grade-persa.svg").read_text() if g else ""
    doc = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"/><title>example-patient-counts</title>
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
  .cardhead>div{{position:absolute;left:107px;top:{1143 - 120 - round(600 * 0.81)}px;width:875px;height:1555px}}
  .cardhead svg,.cardsil svg{{width:100%;height:100%}}
  .uiwrap{{position:absolute;left:0;top:0;width:1080px;height:1920px;z-index:2;background:#0F1012}}
  .brollwrap{{position:absolute;left:0;top:0;width:1080px;height:1920px;z-index:2;overflow:hidden}}
  .cardwrap{{position:absolute;left:114px;top:1143px;width:861px;height:777px;overflow:hidden;border-radius:var(--r-card);z-index:3}}
  .cardroom{{position:absolute;inset:0;background:linear-gradient(180deg,var(--ground-2),var(--ground))}}
  .cardsil{{position:absolute;left:-7px;top:{(1143 - 120 - round(600 * 0.81)) - 1143}px;width:875px;height:1555px}}
  .sql{{position:absolute;left:40px;top:90px;width:1000px;height:1000px;background:#16171A;border:2px solid #26282D;border-radius:22px;overflow:hidden}}
  .sql .bar{{height:74px;background:#1D1F23;border-bottom:2px solid #26282D;display:flex;align-items:center;padding-left:26px;gap:12px}}
  .sql .bar i{{width:18px;height:18px;border-radius:50%;background:#3A3D44}}
  .sql .bar span{{margin-left:18px;font:600 30px var(--font-ui);color:#B9BEC7}}
  .sql .code{{padding:28px 34px;font:500 38px/1.4 ui-monospace,Menlo,Consolas,monospace;color:#E6E8EC;min-height:300px}}
  .sql .restab{{margin:0 34px;padding:14px 0;border-top:2px solid #26282D;font:600 26px var(--font-ui);color:#8E95A1;letter-spacing:.04em}}
  .bigres{{margin:10px 34px;display:flex;flex-direction:column}}
  .bigres span{{font:600 30px var(--font-ui);color:#8E95A1}}
  .bigres b{{font:800 190px/1 var(--font-ui);color:#FFFFFF}}
  .grid{{margin:6px 34px;border-collapse:collapse;font:500 30px var(--font-ui);color:#E6E8EC}}
  .grid th{{text-align:left;color:#8E95A1;font-weight:600;padding:8px 22px 8px 0}}
  .grid td{{padding:10px 22px 10px 0;border-top:1px solid #26282D}}
  .hooknums{{position:absolute;left:0;top:250px;width:1080px;text-align:center;z-index:6;
     font-family:var(--font-display);font-weight:var(--display-weight);font-size:190px;line-height:1;letter-spacing:.01em}}
  .hooknums span{{margin:0 22px}}
  .hooknums .pn{{color:var(--display)}}
  .hooknums .pw,.hooknums .pa{{color:var(--emph-fill);-webkit-text-fill-color:var(--emph-fill);
     -webkit-text-stroke-width:var(--emph-stroke);mix-blend-mode:screen}}
  .hooknums .pw{{-webkit-text-stroke-color:var(--emph-white);filter:var(--glow-white)}}
  .hooknums .pa{{-webkit-text-stroke-color:var(--emph-accent);filter:var(--glow-accent)}}
  .tpill.big{{font-size:52px;padding:18px 36px}}
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
    starts, t2 = [], 0.0
    for say, _, _ in lines:
        d = max(1.6, len(say.replace(":", "").split()) / PACE); starts.append(round(t2 + d / 2, 2)); t2 += d + GAP
    print(json.dumps({"duration": total, "numbers": {"distinct_patients": n3, "visit_rows": n1, "joined_rows": n2},
                      "sample_patient": pid, "beat_middles": starts, "photos": used}, ensure_ascii=False))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--data", default=None, help="folder with the synthetic CSVs (made if missing)")
    a = ap.parse_args()
    out = pathlib.Path(a.out)
    build(out, pathlib.Path(a.data) if a.data else out / "data")
