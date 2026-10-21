# Microsoft Fabric for health-system data teams — scripts (Persa Shorts edit, 9:16)

Three ~60 s talking-head scripts for LinkedIn, each modelled on a format that beat its channel's own median on YouTube
(pulled 2026-10-21): the honest skeptic (112×), "will X replace Y?" (up to 17×) and "we tested it" (11×) — aimed at a
health-system situation, because no short-form Fabric content for health systems turned up in the sample.

Evidence: `docs/reels/fabric-health-systems-research.md`. Facts re-checked on Microsoft Learn on 2026-10-21.

## The formula (from 2026-10-21, YouTube only)

- **Hook A — the honest skeptic:** ["Why Customers are Rejecting Microsoft Fabric"](https://www.youtube.com/watch?v=nxW6gUFzffg)
  (33,000 views, 112× its channel's median, Aug 2026), then four more in the same shape at 23–28× ("Is Microsoft Gutting
  Power BI?", "Why Microsoft Fabric is a Failure!"). The stance repeats, not luck: five hits in two months on one channel.
- **Hook B — "will X replace Y?" on the newest Fabric feature:** Fabric Apps vs Power BI on five channels —
  ["Good Bye Power BI Reports / Welcome Fabric Apps"](https://www.youtube.com/watch?v=p0gzrFG868w) 185,454 (3.3×),
  ["Can Fabric Apps REPLACE Power BI?"](https://www.youtube.com/watch?v=SStJcXn5vGE) 55,987 (4.0×),
  ["What are Fabric Apps?"](https://www.youtube.com/watch?v=b3dybvW5WdA) 52,879 (17.1×).
- **Hook C — "we tested it":** ["We tested the New Power BI Report Skills"](https://www.youtube.com/watch?v=pDRSXOK6fq0)
  158,069 (11.3×), the best recent video on Guy in a Cube.
- **Structure:** a stance or a question in the first line → three concrete reasons or results → what to do → a keyword CTA.
- **Length:** the winners are 4–15 min YouTube videos; for 9:16 on LinkedIn we follow LinkedIn's own advice (about
  1–2 min) and the skill's default: ~60 s here, test 90 s later.
- **CTA:** comment a keyword for a checklist or test plan — reference content. YouTube shows no saves or shares, so judge
  it on LinkedIn by keyword comments and DMs.
- **Cadence:** the skeptic channel's reach rose while it posted 11–20 videos a month; keep the plan's 3 a week.
- **The gap to own:** healthcare Fabric content is long, job-seeker portfolio work; every script here names a situation a
  health-system data team actually has.

## How to record

Sit a little further back with room above your head (brand.md). One take per script, all three in one sitting; if you
fluff a line, pause and say it again — the editor keeps the last clean take. For every "screen" row, record your screen
on a demo tenant or synthetic data only (never a client's data). Then: "Edit ~/content-machine/recordings/<file> with
nextphase-persa-shorts, script: docs/reels/fabric-health-systems-scripts.md, script <n>".

---

## Script 1 — "Three reasons to wait on Fabric" (~60 s)

Modelled on: [Microsoft Hates Greg, "Why Customers are Rejecting Microsoft Fabric"](https://www.youtube.com/watch?v=nxW6gUFzffg) — 33,000 views, 112× channel median.

**Hook (caption + post title):** Three reasons a health system should wait on Fabric. One is about patient data.

| # | Say | Picture | Source |
|---|---|---|---|
| 1 | "Three reasons a health system should wait on Fabric. One is about patient data." | face; display word WAIT; first frame "3 REASONS TO WAIT" | — |
| 2 | "I build on Fabric for a living. So here's the honest version." | face | — |
| 3 | "One: your viewers. Below an F64 capacity, everyone who opens a Power BI report needs a Pro or PPU licence." | 9:16 shot of the Microsoft Learn licences page; claim typed in its empty space: BELOW F64 = PRO PER VIEWER | [Licences](https://learn.microsoft.com/en-us/fabric/enterprise/licenses) |
| 4 | "Thousands of managers opening one dashboard? Do that math first." | face; hollow word MATH | — |
| 5 | "Two: who can see patient data. Workspace admins, members and contributors can read everything in OneLake." | the workspace-roles table, row "Can read data in OneLake?" highlighted | [OneLake security: get started](https://learn.microsoft.com/en-us/fabric/onelake/security/get-started-security) |
| 6 | "OneLake security roles are how you limit viewers. They don't hold back the people building it." | same table, the Viewer row and its footnote | same |
| 7 | "So if engineers share a workspace with patient data, they can read all of it." | face; hollow word ALL | inference from the table (see Keep exact) |
| 8 | "Three: the audit trail. Warehouse audit logs record nothing until someone turns them on." | 9:16 shot of the SQL audit logs page, "must enable it" line | [SQL audit logs](https://learn.microsoft.com/en-us/fabric/data-warehouse/sql-audit-logs) |
| 9 | "Delete the warehouse, and its audit logs go with it." | same page, the delete line | same |
| 10 | "None of these is a reason to say no. They're decisions to make before you move." | face | — |
| 11 | "Price the F64 line. Split workspaces by who sees patient data. Turn on audit logs on day one." | three labels on screen, one per sentence | — |
| 12 | "Most teams plan the migration. The good ones plan the access." | face; display word ACCESS | — |
| 13 | "Comment WAIT and I'll send you the checklist I'd run before a health system moves." | COMMENT WAIT + arrow | — |

**Keep exact:**
- "On F SKUs smaller than F64, each user viewing Power BI content must have Pro, PPU, or an individual trial." (Licences page, checked 2026-10-21)
- Roles table: Admin, Member and Contributor — "Can read data in OneLake? Yes"; Viewer — only through OneLake security roles. (Get started with OneLake security, ms.date 2026-09-01)
- "Users with Audit queries permissions must enable it to capture the logs." · "If you delete the Warehouse, you also delete the associated audit log files." (SQL audit logs, ms.date 2026-08-10)
- Line 7 is our reading of the roles table → fallback: "Anyone with contributor access or higher can read that workspace's data in OneLake."
- Don't say Fabric is or isn't HIPAA compliant in this video. Re-open all three pages the week you film.

**Post caption:** Three reasons a health system should wait on Fabric — and the decision that fixes each one. Below F64,
every report viewer needs Pro or PPU. Admins, members and contributors can read all the data in OneLake; security roles
limit viewers. Warehouse audit logs capture nothing until someone enables them. Comment WAIT for the pre-move checklist.
#MicrosoftFabric #PowerBI #HealthcareAnalytics

---

## Script 2 — "Can a Fabric App replace your unit's Excel tracker?" (~55 s)

Modelled on: [Guy in a Cube, "Can Fabric Apps REPLACE Power BI?"](https://www.youtube.com/watch?v=SStJcXn5vGE) — 55,987 views, 4.0× channel median (the same question on four more channels, up to 17.1×).

**Hook (caption + post title):** That Excel tracker your unit emails every morning. Could a Fabric App replace it?

| # | Say | Picture | Source |
|---|---|---|---|
| 1 | "That Excel tracker your unit emails every morning. Could a Fabric App replace it?" | face; first frame "EXCEL TRACKER → APP?" | — |
| 2 | "Everyone's asking if Fabric Apps will replace Power BI. In a hospital, the better question is the spreadsheet." | face; hollow word SPREADSHEET | — |
| 3 | "Fabric Apps lets developers build data apps on Fabric. They can read a lakehouse, a warehouse, a SQL database or a semantic model." | 9:16 shot of the Fabric Apps overview, "Fabric data connectors" line | [Fabric Apps overview](https://learn.microsoft.com/en-us/fabric/apps/overview) |
| 4 | "So the tracker could sit on the same data as your reports, not last night's export." | face | inference (see Keep exact) |
| 5 | "Three things first." | display 3 THINGS | — |
| 6 | "One: it's in preview. Fabric's own healthcare tools dropped two preview features in November 2025." | the "This feature is in preview" note, then the discontinued note on the healthcare data solutions page | [Fabric Apps](https://learn.microsoft.com/en-us/fabric/apps/overview) · [Healthcare data solutions overview](https://learn.microsoft.com/en-us/industry/healthcare/healthcare-data-solutions/overview) |
| 7 | "Two: a tenant admin has to switch it on, and it runs on your capacity." | the Prerequisites section | Fabric Apps overview |
| 8 | "Three: hosted pages can be set to allow anonymous access. Decide that before patient data is anywhere near it." | the "allow anonymous access to hosted assets" line; hollow word ANONYMOUS | Fabric Apps overview |
| 9 | "So start with one tracker that has no patient data." | face | — |
| 10 | "Rebuild it as a test, and count the manual steps before and after." | on screen STEPS BEFORE → AFTER | — |
| 11 | "The report was never the problem. The spreadsheet around it was." | face; display word SPREADSHEET | — |
| 12 | "Comment TRACKER and I'll send you the one-page test plan." | COMMENT TRACKER + arrow | — |

**Keep exact:**
- "Fabric Apps (preview)" · "Fabric data connectors – Add typed access to a lakehouse, warehouse, SQL database in Fabric, or semantic model." (Fabric Apps overview, ms.date 2026-09-15)
- "A Fabric tenant administrator must enable the Fabric Apps workload" · "Fabric Apps services consume capacity units from the assigned capacity." (same page)
- "Require Fabric item access or allow anonymous access to hosted assets." → say "can be set to", never "is open by default" (the page doesn't say what the default is).
- "Discover and build cohorts and Unstructured clinical notes enrichment … effective November 2025 … discontinued." (Healthcare data solutions overview)
- Line 4 is our inference → fallback: "So the tracker could run on governed Fabric data."
- "Fabric Apps are not available in all regions yet" — check the tenant's region before promising it. If Fabric Apps is GA by filming day, rewrite line 6.

**Post caption:** Everyone's asking if Fabric Apps will replace Power BI. In a hospital, the better question is the Excel
tracker your unit emails every morning. It's in preview, a tenant admin has to enable it, and hosted pages can allow
anonymous access — so start with one tracker that holds no patient data. Comment TRACKER for the test plan.
#MicrosoftFabric #PowerBI #HealthcareAnalytics

---

## Script 3 — "We counted the same patients three ways" (~60 s)

Modelled on: [Guy in a Cube, "We tested the New Power BI Report Skills"](https://www.youtube.com/watch?v=pDRSXOK6fq0) — 158,069 views, 11.3× channel median.

**Hook (caption + post title):** We counted one month of patients three ways. We got 412, 522 and 946.

| # | Say | Picture | Source |
|---|---|---|---|
| 1 | "We counted one month of patients three ways. We got 412, 522 and 946." | face; first frame 412 · 522 · 946 | demo (synthetic) |
| 2 | "Same data. Three queries. Here's what each one actually counted." | face | — |
| 3 | "Query one: count the rows in the visits table. 522." | screen: the query and its result | demo |
| 4 | "That's visits, not patients. Anyone who came back is counted again." | hollow word AGAIN | true by construction |
| 5 | "Query two: join the diagnoses first, then count. 946." | screen: the join query and result | demo |
| 6 | "Every extra diagnosis on a visit adds another row." | the joined rows, one visit repeated | true by construction |
| 7 | "Query three: count distinct patient IDs. 412." | screen; display 412; typed note "= patients, not visits" | demo |
| 8 | "That's the answer to 'how many patients did we see?'" | face | — |
| 9 | "And even 412 is wrong if one person ended up with two patient IDs." | two demo rows, P0007 and P0391, "same person?" | — (no number claimed) |
| 10 | "So before a count goes on a dashboard: name the grain, check rows across every join, label the question." | three labels on screen | — |
| 11 | "Most teams argue about which number is right. The fix is agreeing what each number means." | face; display word MEANS | — |
| 12 | "Comment COUNTS and I'll send you the five checks I'd run before a patient count reaches a CFO." | COMMENT COUNTS + arrow | — |

**Keep exact:**
- 412 / 522 / 946 come from the synthetic month in `docs/reels/demo/synthetic_month.py` (seed 20261123):
  `COUNT(DISTINCT patient_id)` = 412, `COUNT(*)` on visits = 522, `COUNT(*)` after the diagnosis join = 946. Re-run it before
  filming and say whatever it prints; put "synthetic data" on screen.
- Lines 4 and 6 are true by how the tables are built (one row per visit; one row per visit-diagnosis) — show it in the demo.
- Line 9 names a real data-quality risk (duplicate patient records) without a number; keep it that way.

**Post caption:** We counted one month of patients three ways and got 412, 522 and 946. None of the queries is broken —
each answers a different question: visits, visit-diagnosis rows, patients. Name the grain, check rows across every join,
label the question. Comment COUNTS for the five checks. (Synthetic data, no real patients.)
#PowerBI #MicrosoftFabric #HealthcareAnalytics
