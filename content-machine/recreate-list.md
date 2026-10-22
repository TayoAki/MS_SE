# Recreate list — start with what already works

While the channel is new, most videos recreate a post that already beat its own channel's normal. We keep its **topic,
title/hook shape, structure and length band**; we write **every word ourselves**, show **our own screens**, and use
**facts we checked**. Never their script, footage or audio (niche-scripts rule: copy formats, not content). If a
recreation follows one creator's unusual framework closely, credit them in the post.

Evidence: `docs/reels/fabric-health-systems-research.md` (YouTube, pulled 2026-10-21). "× median" = views ÷ that channel's
median. Scripts: `docs/reels/fabric-recreations-scripts.md`.

**Closest recreation:** paste a winner's transcript (YouTube → "…more" → "Show transcript" → copy) and say "recreate
this" — Claude maps its beat order, then rewrites every line from our facts. YouTube blocks transcript downloads from
the cloud container, so the paste is the way.

## Up next (scripted)
| # | Recreates | Proof it works | Our version | Status |
|---|---|---|---|---|
| RC1 | "Can Fabric Apps REPLACE Power BI?" | the same question on 5 channels: 185K (3.3×), 131K (2.3×), 56K (4.0×), 53K (17.1×), 45K (13.6×) | "Can Fabric Apps replace Power BI?" — what it is, what it can do, 3 reasons it won't | scripted, facts checked |
| RC2 | Storage modes explained: Import vs DirectQuery vs Direct Lake | evergreen across channels and years: Guy in a Cube 428K (2021, approx.), Data with Baraa 40K (2026) | the three modes in 70 s, with the Direct Lake fallback catch | scripted, facts checked |
| RC3 | "What Is Fabric IQ?! … Explained" | 3 channels: Guy in a Cube 45K (3.2×), Microsoft's own 95 s intro 20K (12×), Informatec 45K | Fabric IQ in 60 s, ending on "an agent is only as right as your definitions" | scripted, facts checked, example built (`scripts/2026-11-09-01-what-is-fabric-iq/`) |
| RC4 | "We tested the New Power BI Report Skills" | Guy in a Cube 158K (11.3×) + How to Power BI "The New Power BI Authoring Skills Change Everything" 155K (2.8×) | we run Microsoft's Power BI Report skill on synthetic data and show what it got right and wrong | **needs the test run first** |
| RC5 | "Why Customers are Rejecting Microsoft Fabric" (+4 follow-ups at 23–28×) | 33K, 112× its channel median | "Why teams push back on Fabric — I read 96 real requests for help" (your community research) | scripted, numbers from your spreadsheet |

### The format each recreation uses (`formats.md`)
The topic proof is the row above. The format proof is a Short that beat its own channel's median.
| RC | Format | Modelled on | Status |
|---|---|---|---|
| RC1 | F3 X vs Y, title held: FABRIC APPS vs POWER BI, three numbered reasons | Alex The Analyst "Data Analyst vs Business Analyst" (215K, 11.3×) | v2 example built: `docs/reels/demo/rc1-v2.json` |
| RC2 | F2 ladder: Import → DirectQuery → Direct Lake, slowest to fastest, plus the fallback catch | MyOnlineTrainingHub "3 Ways to Sum Data / Beginner to Advanced" (3.5M, 103×) | to rewrite |
| RC3 | F1 "Don't start with the AI agent", then #1 definitions, #2 ontology, #3 agent | Alex The Analyst "Don't jump into Power BI first" (740K, 38.9×) | v2 example built: `docs/reels/demo/rc3-v2.json` |
| RC4 | F4 wrong way → fast way, on your own screen | Leila Gharani "Delete Empty Rows" (1.9M, 25.7×) | needs the test run |
| RC5 | F5 the blunt question: "Why do teams push back on Fabric? Honestly…" | Seattle Data Guy "Is Data Engineering Still A Good Career Choice?" (115K, 12.5×) | to rewrite |

## Backlog (proven, not scripted yet)
| Recreates | Proof | Note |
|---|---|---|
| "When Should You START Using Microsoft Fabric?" (Guy in a Cube) | 45K, 3.2× | answer with the field guide's "which to lead with" table |
| "Fabric demo: An end-to-end tour of the OneLake catalog" (Microsoft Fabric) | 50.7K, 29.8×, 170 s | a 60 s tour of your own demo tenant's OneLake catalog |
| "Introducing IQ in Microsoft Fabric" (Microsoft Fabric) | 20.4K, 12×, 95 s | short official-demo format; pairs with RC3 |
| "DP-700 … Exam Question N" series (Learn With Priyanka) | ~2,400–2,900 views each, 10+ in a row | a weekly exam-question short; reference content people save |
| "Is Microsoft Gutting Power BI?" / "Microsoft is Killing ODBC!" (Microsoft Hates Greg) | 8.2K (28×), 7.4K (25×) | only with a verified change behind it; never fabricated urgency |
| "Good Bye Power BI Reports / Welcome Fabric Apps" (How to Power BI) | 185K, 3.3× | same topic as RC1 — use as RC1's second take or a follow-up |

## Rules for a recreation
- Same promise as the original's title, delivered in 45–90 s for 9:16 LinkedIn.
- Every fact re-checked on its official page the week we film; preview features named as preview.
- One healthcare line where it fits naturally — the proven demand is for the topic, so the topic leads.
- Add each original to `swipe/swipe.md` so its shape stays on file.
