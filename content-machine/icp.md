# ICP — who every video is for

Researched 2026-10-21. Every finding carries its label: **Verified** (primary source read), **Reported** (secondary,
vendor, or a search excerpt of a page that couldn't be opened — check before saying it on camera), **Inference** (our
reasoning, not a finding). Full evidence and every link: `research/buyers.md`, `research/fabric-healthcare.md`,
`research/linkedin-video.md`, `research/fabric-community-research.xlsx`.

**In one line:** the analytics leader at a US health system (usually on Epic, usually already paying for Power BI) who is
accountable for reports people don't trust, can't get fast enough, and fix by hand — and the data/BI engineers on their
team who live with it every day.

## 1. The people — who signs, who champions, who does the work (Inference, built from the evidence below)
| Role | What they own | What they want to hear | Funnel videos that reach them |
|---|---|---|---|
| **CIO / Chief Digital Officer / CDAO** — signs platform decisions | strategy, architecture, accountability | lower risk and cost, AI readiness, ROI they can defend | offer, authority |
| **VP / Director of Enterprise Analytics or BI** — signs or recommends a services engagement; **your main buyer** | the report backlog, self-service, trust in numbers | "fewer open requests, faster loads, numbers people trust" | offer, authority |
| **Data engineering / BI manager** — your champion, brings you in | refresh failures, pipelines, capacity, the 2 a.m. page | how to fix the thing that broke this week | reach, authority |
| **Clarity/Caboodle report writers, BI developers, data engineers** — do the work, follow you, forward you | building and fixing reports and pipelines | tutorials, tests, honest tool limits | reach |
| **CISO / privacy, Epic Cogito team, enterprise architecture** — can block | PHI, Epic's roadmap, standards | access proven by tests, no compliance promises, fits Epic's direction | authority (P4) |
| **CFO / finance** — pulled in when the case is cost or finance reporting | finance reporting, IT spend | accurate, timely data; cost you can forecast | offer (P3) |

Evidence behind it:
- Large systems have a distinct **Chief Data & Analytics Officer** (Sutter, Tufts, Montefiore on Becker's podcasts —
  Reported). In smaller systems "one Vice President of Analytics or Information typically wears two or three of these
  hats" (consultancy blog — Reported).
- **VP Enterprise Analytics** owns report volume: Zach Bork, CentraCare — "In the past, we produced more than 12,000
  reports each month"; about **43 outstanding requests per month** before self-service (Chartis, 2025-01-03 — Verified).
- **CIOs buy capacity, keep accountability:** "I'm comfortable outsourcing capabilities, capacity and commodity work.
  What I would not outsource is our technology strategy, architecture and accountability for technology decisions" —
  Reid Stephan, CIO, St. Luke's (Becker's — Reported). → Position yourself as capacity and expertise *under* their
  architecture, never as the owner of their strategy (Inference).
- **The doers, in a real posting:** UVM Health Network "Data Engineer, Microsoft Fabric" — Epic Clarity/Caboodle into a
  Fabric lakehouse, 2–4 years' experience, $42.85–64.28/hr (posting now closed — Reported).
- Team size: **no source found.** Ask on your calls.

## 2. What's on their mind (2025–2026)
- **They don't trust the data.** 45% of health systems cite "lack of trust in data accuracy" as a primary barrier; only
  39% have a formally chartered data governance function (CHIME Most Wired 2025, 278 orgs, via InterSystems — Reported).
- **Finance feels it too.** Nearly 90% say data accuracy is the biggest challenge in meeting internal needs; 81%+ call
  lack of reporting capabilities a major hurdle (HFMA, Sage-sponsored, 2026-06-01 — Reported).
- **AI is the priority, data readiness is the gate.** AI is the top tech priority for 57% (Sage Growth via Becker's —
  Reported); 9 in 10 executives prioritise digital/AI and the report recommends "investing in data infrastructure and
  readiness" (Chartis 2025 survey — Verified). Top AI barrier: "lack of AI tool maturity", 77% (JAMIA 2025, Scottsdale
  Institute — Verified).
- **ROI or nothing.** Buyers with formal ROI thresholds expect about 3–4× (Bain/KLAS via Healthcare Dive, 2026-09-24 —
  Reported). "ROI will become increasingly important to sustain investment."
- **Too many tools, unpredictable bills.** CommonSpirit's CIO: "from proliferation to precision", 230+ tools live
  (Becker's — Reported). Consumption pricing makes total cost harder to forecast (Reid Health CIO — Reported).
- **Value-based care raises the stakes:** at CentraCare 40% of margin is tied to VBC (Chartis — Verified).

## 3. Pains in their words — the hook bank
Use these as the *shape* of hooks; quote word for word only with the source on screen. Speaker type matters.
| Quote | Who said it | Source |
|---|---|---|
| "In the past, we produced more than 12,000 reports each month." | VP Enterprise Analytics, CentraCare | Chartis 2025-01-03 (Verified) |
| "Self-service is absolutely a key strategy for us." | same | same |
| "create better data hygiene at the point of capture to increase confidence for reliable analysis" | SVP CIDO, LifeBridge Health | same |
| "It's no longer a ticketing queue with a 30-to-45-day response time." | UNC Health (after Fabric) | Microsoft customer story 2026-05-26 (Verified, vendor-published) |
| "couldn't keep pace with 40% annual data growth" | UNC Health | same |
| "The second you do an export, it's not up to date." | a vendor exec (Sage), not a health system | HFMA 2026-06-01 (Reported) |
| "Departments develop workarounds and manual processes that eventually become permanent parts of the workflow." | vendor CTO (Xsolis) | HIT Consultant 2026-04-20 (Reported) |
| "Refresh Succeeds but Does Not Pick Up Latest Data" | Fabric Community thread title | community.fabric.microsoft.com (Reported) |
| "data aggregation and integration" (top barrier) · "frustrations with data storage costs" | KLAS customer themes | HIT Consultant on KLAS 2025-05-02 (Reported) |

From the Fabric community research (your spreadsheet, healthcare rows, firsthand):
- Can't count distinct patients across visits, diagnoses, procedures and care sites without ambiguity (Fabric Community,
  2025-04-04) → P1.
- A paginated clinical report migrated to Power BI calculates wrongly and can't filter care locations by physician
  organisation (2024-11-05) → P1.
- A team can't assemble access evidence to answer "who accessed which patient information" across audit logs, semantic
  models, storage and AI for a HIPAA project (r/MicrosoftFabric, ~Sep 2026) → P4.
- A doctor supporting hospital management analytics is drowning in repeated Power Query logic across Excel workbooks
  (r/MicrosoftFabric) → P2.
- Conflicting numbers between Epic reports when teams build the same metric (e.g. readmissions) without shared logic —
  "a data governance problem rather than an SQL problem" (consultancy blogs — Reported) → P1.

## 4. Why now — dated triggers
1. **Microsoft is changing how its healthcare solution for Fabric is delivered (Verified, Microsoft Learn, read
   2026-10-21).** Since 2026-08-03 there's a downloadable source-code package for customer-managed implementations; since
   2026-10-01 only existing customers can deploy the managed version; **support for the managed version ends
   2027-12-31.** Every existing customer needs a transition plan; every new one builds and runs it themselves or with a
   partner (Inference). Also verified: cohort builder and clinical-notes enrichment were discontinued Nov 2025 — buyers
   have seen preview features withdrawn.
2. **Epic's analytics moving to the cloud on Azure (Reported — consultancies only).** RSM (2026-04-21): Epic plans to
   "release all new data models exclusively through the Cogito Cloud"; "Every Epic customer will need to respond." EHC
   Consulting: Cogito Cloud (formerly Nebula) is built on Azure and leverages Fabric. **Not found on any Epic page —
   never state it as fact on camera without Epic's own source.**
3. **Epic on Azure.** Franciscan, Jefferson, St. Luke's (Microsoft, 2026-03-19) and Duke Health (2026-07-28) — Verified,
   vendor-published. A likely leading indicator of Fabric work (Inference).
4. **Power BI Premium P SKUs are retiring** → re-sizing to F SKUs, and the F64 line decides whether thousands of viewers
   need Pro (Microsoft Learn licences page — Verified). A natural cost-review moment.
5. **Mergers.** 46 hospital deals in 2025, a record 43.5% with a financially distressed party (Kaufman Hall 2026-01-15 —
   Verified); Q1 2026 the busiest quarter since early 2020 (Reported). Every merger doubles the warehouses and dashboards
   to reconcile (Inference).
6. Not found: evidence for a new CDAO hire or a failed audit as triggers, or any Synapse retirement — don't claim one.

## 5. Objections and how to answer them
| Objection | Evidence | Answer shape (Inference) |
|---|---|---|
| "We're an Epic shop." | Over half of providers prefer an EHR-native tool with partial functionality over a third party (Bain/KLAS — Reported) | Work *with* Epic's direction: what you build in your own tenant beyond what Epic delivers |
| "PHI / security." | Cybersecurity and compliance is the #1 data priority, 86% top-3 (CHIME-partnered, n=21 — Reported); Fabric Warehouse SQL audit logs are off by default (Microsoft Learn — Reported); a BAA covers Microsoft's side, not your configuration | Show the access test matrix; never say "Fabric makes you compliant" |
| "Cost — consumption pricing scares us." | Consumption pricing hurts forecasting (Reid Health CIO — Reported) | P3: size from the Capacity Metrics app, name the hidden costs up front (`fabric-field-guide.md`) |
| "Microsoft lock-in." | Raised by Snowflake/Databricks partners (Reported) | Open Delta/Parquet in OneLake; shortcuts; be honest about where Databricks wins |
| "Our team doesn't have the skills." | KLAS: "internal staffing limits" (Reported) | Capacity + teaching: you build it with them, they own it after |
| "You'll own our strategy." | St. Luke's CIO quote above | You bring capacity and expertise; their architects decide |

## 6. Proof they trust — and what breaks trust
- **Trusted:** peer evidence (KLAS-style, a named peer health system), before/after numbers (refresh time, open requests,
  manual hours), small proofs of concept — RSM says "Microsoft funding frequently offsets the costs of roadmap and
  proof-of-concept work" (consultancy — Reported). Vendor-free peer settings like HDAA.
- **Real Fabric health systems you can point to (all Microsoft-published, so self-reported):** UNC Health
  ("standardized its entire data estate on Fabric", 2026-05-26), Virtua Health (Epic + Fabric + Power BI, 2026), Duke
  Health (modernising with Fabric, 2026-07-28), Peterborough Regional (Canada, Epic site). Northwestern Medicine also
  presented with Databricks at HIMSS26 — don't call it a Fabric shop.
- **Breaks trust (KLAS themes — Reported):** staff turnover, lack of expertise or operational context, unclear roadmaps,
  surprise storage costs; asking to own their strategy; AI hype when 77% say the tools aren't mature; rip-and-replace.

## 7. Where they are
- **Next 4 weeks:** HDAA Conference, Nov 9–12 2026, Dallas (practitioners, "vendor-free") · CHIME Fall Forum, Nov 11–14
  2026, Aurora CO (CIOs) — Reported; check the official sites. Great hooks for trend/reaction videos and comments.
- **Communities:** CHIME (CIOs), HDAA (analytics practitioners), HFMA (finance), Scottsdale Institute, the Health & Life
  Sciences Fabric User Group (488 members, virtual — your research), r/MicrosoftFabric.
- **Media they appear in:** Becker's Health IT podcasts and lists (e.g. "135 hospital and health system CIOs to know
  2026" — a ready target list), Healthcare Innovation podcast, HealthTech Magazine's influencer list.
- **LinkedIn:** no healthcare-specific data on how these leaders use LinkedIn was found. Best proxy (not healthcare):
  in the Edelman–LinkedIn 2025 B2B thought-leadership report, "hidden" buyers (finance, compliance, procurement,
  operations) read thought leadership too, 86% favour perspectives that challenge their assumptions, and 79% are more
  likely to champion vendors who publish consistently (Reported). See `research/linkedin-video.md` for LinkedIn video
  specs and the creators already in this space.

## 8. Words
- **They say:** "trust in data accuracy", "data governance", "data stewardship", "data hygiene", "self-service",
  "operating model", "data literacy", "actionable insights", "ROI", "total cost of ownership", "rationalization",
  "accountability", "accurate, real-time data".
- **Not evidenced as their phrase:** "single source of truth" — fine to say, but don't present it as their words.
- **Avoid:** "revolutionize", "game-changer", "unlock the power of your data", rip-and-replace, AI promises. Lead with
  plain numbers: refresh time, open requests, manual hours.

## 9. What this means for the videos (Inference)
- **Reach and authority talk to the champion** (engineer/BI manager): the calendar's practitioner topics are right for
  them. **Offer videos talk to the VP/Director:** backlog, trust, cost, risk — in their words above.
- **Lead with a number they own:** open requests, refresh minutes, hours of manual fixes, report count.
- **Three angles nobody owns yet:** (1) the healthcare-solution delivery change and its 2027-12-31 deadline; (2) "who
  accessed which patient's data?" — audit evidence in Fabric isn't on by default; (3) patient and encounter counts that
  disagree — no public source covers it, so your stories make it yours (validate with your own experience first).
- **Be the honest one:** say the caveats out loud (the guide's "say it out loud" column) — it's what KLAS says buyers
  reward.

## 10. Still unknown — ask on calls, then update this file
Typical analytics team size · how these leaders actually use LinkedIn · whether Epic allows CDC on Clarity for Fabric
mirroring (a real blocker to check per customer) · how Cogito Cloud data reaches a health system's own Fabric tenant ·
which offer they'd buy first.
