# Microsoft Fabric for health-system data teams — what is performing (research)

Pulled **2026-10-21** with `niche-scripts` (discover.py + history.py), **YouTube only**: `SCRAPECREATORS_API_KEY` was
not set, so TikTok and Instagram were not searched. 254 relevant videos, 133 channels, uploaded in the last 12 months.

**Search terms (12):** microsoft fabric · microsoft fabric tutorial · fabric data engineer · dp-700 · dp-600 · direct lake
power bi · fabric capacity · power bi healthcare · healthcare data analytics · epic clarity · fhir analytics · microsoft
fabric shorts.
**Relevance:** title must match `microsoft ?fabric|onelake|dp-?[67]00|direct ?lake|power ?bi|lakehouse|epic.{0,20}(clarity|caboodle|cogito)|fhir|(healthcare|hospital|clinical) (data|analytics|reporting|dashboard)`;
excluded `sewing|textile|quilt|upholster|fashion|clothing|knit|crochet|minecraft|dp600h|\bamp\b|guitar|dolby|\b8k\b|\b4k\b|\bhdr\b|120fps`
(the second run added the 8K/HDR terms after an "EPIC VISUALS IN ULTRA CLARITY" TV demo matched).

**Metric:** "× median" = the video's views ÷ the median views of that channel's last 60 uploads (discover.py) or of its
full history (history.py, marked *h*). YouTube gives no saves or shares. Dates older than a year are approximate.

## What repeats (the evidence behind the formula)

### 1. The honest skeptic — one channel, five hits in two months
| Video | Views | × median | Length | Posted |
|---|---|---|---|---|
| [Why Customers are Rejecting Microsoft Fabric](https://www.youtube.com/watch?v=nxW6gUFzffg) | 33,000 | 112× *h* | 355 s | Aug 2026 |
| [Is Microsoft Gutting Power BI?](https://www.youtube.com/watch?v=wzKnx_HchvM) | 8,200 | 28× *h* | 676 s | Sep 2026 |
| [Microsoft is Killing ODBC!](https://www.youtube.com/watch?v=HJIz3NRcops) | 7,400 | 25× *h* | 294 s | Oct 2026 |
| [The Power BI Killer!](https://www.youtube.com/watch?v=jGrCdmOv9ik) | 7,300 | 25× *h* | 698 s | Oct 2026 |
| [Why Microsoft Fabric is a Failure!](https://www.youtube.com/watch?v=qVrni8qNTME) | 6,700 | 23× *h* | 514 s | Oct 2026 |

Channel: Microsoft Hates Greg, 11,200 subscribers, median 295 views over 490 videos. Its monthly median went from ~300 to
~1,000 in Oct 2026 while it posted 11–20 videos a month (Aug–Oct), up from 3–8.

### 2. "Will X replace Y?" on a new Fabric feature — one topic, five channels
| Video | Channel | Views | × median | Length |
|---|---|---|---|---|
| [Good Bye Power BI Reports / Welcome Fabric Apps](https://www.youtube.com/watch?v=p0gzrFG868w) | How to Power BI (1.06M subs) | 185,454 | 3.3× | 751 s |
| [Microsoft Fabric Apps Explained (The SaaS Killer?)](https://www.youtube.com/watch?v=xjizOqvu-EU) | How to Power BI | 130,970 | 2.3× | 911 s |
| [Can Fabric Apps REPLACE Power BI?](https://www.youtube.com/watch?v=SStJcXn5vGE) | Guy in a Cube (561K) | 55,987 | 4.0× | 643 s |
| [What are Fabric Apps? Is this the future for Power BI?](https://www.youtube.com/watch?v=b3dybvW5WdA) | Data Goblins (6.7K) | 52,879 | 17.1× | 2,258 s |
| [Microsoft Fabric Apps: Everything You Need to Know](https://www.youtube.com/watch?v=dBicz2tD8Wo) | Lumio Visuals (1.3K) | 44,850 | 13.6× | 702 s |

### 3. "We tested it"
| Video | Channel | Views | × median | Length |
|---|---|---|---|---|
| [We tested the New Power BI Report Skills: The Future of AI-Powered Reporting?](https://www.youtube.com/watch?v=pDRSXOK6fq0) | Guy in a Cube | 158,069 | 11.3× | 499 s |

Guy in a Cube: 822 videos, 1.4 a week, full-history median 26,000; 3% of videos at 10×+ its median.

### 4. Short official demos (the short-form that does exist)
| Video | Channel | Views | × median | Length |
|---|---|---|---|---|
| [Fabric demo / An end-to-end tour of the OneLake catalog](https://www.youtube.com/watch?v=gbcj7I0OpcY) | Microsoft Fabric (26.7K) | 50,672 | 29.8× | 170 s |
| [Introducing IQ in Microsoft Fabric](https://www.youtube.com/watch?v=RjU0slwcZGs) | Microsoft Fabric | 20,390 | 12.0× | 95 s |

## What does not exist yet (the opening)
- **Short-form is under-supplied:** 21 of 254 relevant videos are 3 minutes or shorter; most are official demos, DP-700
  exam-question series (Learn With Priyanka, ~2,400–2,900 views each) and free-voucher videos.
- **Healthcare is long-form and job-seeker-facing:** 62 videos mention healthcare, hospitals, patients, Epic or FHIR; the
  top ones are multi-hour "build a hospital dashboard" portfolio projects (e.g.
  [Data Tutorials, 32,882 views, 11,732 s](https://www.youtube.com/watch?v=oiuSf8dWopA)). None found is short-form for the
  people who run a health system's data platform.

## Dropped, and why
| Account / video | Why |
|---|---|
| DVW Analytics — "SAP Data into a Microsoft Fabric Lakehouse in Minutes" (1,847,271 views, 64K subs) | channel median ~190K on 64K subscribers: the paid-promotion pattern (`reference/lessons.md`) |
| CloudThat — "Stop Hardcoding in Microsoft Fabric!" (64K) and "Power BI Storage Modes Explained" (51K) | 2,670 subs, history median 162; Feb–Aug 2026 every upload, Fabric or not (SC-200, GitHub Copilot, Azure Agents), got 24K–64K, then Sep–Oct fell to <400 — looks promoted, so not a formula |
| Informatec — "Agentic AI in Microsoft Fabric" (45K, 46 subs) | one hit on a tiny channel: a lead, not a pattern |
| Alex The Analyst — 24-hour data analyst bootcamp; Vedakarna — HR dashboard | generic Power BI/data-analyst, not this niche |
| 8K Paradise — "EPIC VISUALS IN ULTRA CLARITY" | homonym (excluded on the second run) |
| Aleksi Partanen — "FREE Vouchers for DP-700 & DP-600! - Limited Time!" | time-bound offer; the Fabric Data Days voucher offer closed Aug 10 2026 (`reference/lessons.md`) |

## Limits
- YouTube only. Search returns about 40 results per term; Shorts are undercounted; no saves or shares.
- Channel medians come from the last 60 uploads (discover) or full history (history); older YouTube dates are approximate.
- No frames were watched (clips.py needs TikTok/Instagram media); formats are read from titles and lengths only.
- To add TikTok and Instagram: set `SCRAPECREATORS_API_KEY` and re-run discover.py (about 2 credits per term per platform —
  ~48 credits for these 12 terms on two platforms).
