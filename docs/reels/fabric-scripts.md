# Set 1: Fabric scripts (modelled on @shreya.knows.data)

Brought into this repo on Oct 22 2026 from the summary "All scripts and what inspired them" (`all-scripts-and-inspirations.md`). The wording matches that summary except where the Oct 22 fact-check changed it; each change is listed under its script. The inspiration numbers are from the original TikTok and YouTube research; they were not re-pulled here (TikTok needs the ScrapeCreators key). Example cuts are in the house style (`content-machine/formats.md`) with a free local AI stand-in voice; replace it with your own take.

## 1. Fabric vs Power BI

| | |
| --- | --- |
| Set | Set 1 |
| File | `fabric-scripts.md` |
| Length | ~65 s (example cut: 45 s) |
| Keyword | FABRIC |

**Inspired by:**
- [@shreya.knows.data, "Microsoft Fabric vs. Power BI is the most searched question…"](https://www.tiktok.com/@shreya.knows.data/video/7638031376217853205): 68,935 views (her 2nd best).

**What we took:** The claim-as-first-line hook, three reasons, a "what to do next" close, under 90 s.

**Script:**

> Microsoft Fabric or Power BI: which one should you learn?

> It's the wrong question.

> Power BI isn't competing with Fabric. Power BI is inside Fabric.

> Fabric is the whole kitchen: getting data in, storing it, cleaning it, and serving it.

> Everything lands in one lake, OneLake, as open Delta tables.

> Then Power BI reads those tables directly. That's Direct Lake. No import copy, and a refresh only copies metadata.

> So if you already know Power BI, you're not starting over. You're one layer up from where Fabric starts.

> Learn the lakehouse, a little SQL, and how data gets into OneLake.

> That's the difference between a report builder and the person who owns the data.

> Comment FABRIC and I'll send you the free learning path I'd follow.

**Facts from** (re-checked Oct 22 2026):
- [What is Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/fundamentals/microsoft-fabric-overview): the architecture diagram lists Power BI among the Fabric workloads (ms.date 2026-03-18, re-checked Oct 22 2026)
- [What is OneLake](https://learn.microsoft.com/en-us/fabric/onelake/onelake-overview): "all store data in OneLake in the open Delta Parquet format" (2026-03-09)
- [Direct Lake overview](https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-overview): "A Direct Lake refresh copies only metadata… which can take a few seconds" (2026-09-02)

**Keep exact / check before filming:**
- OneLake also stores Iceberg tables; "open Delta tables" is still true for Fabric's own engines.

**Example cut:** `docs/reels/demo/nine/s1-fabric-vs-power-bi.json` → `~/persa-shorts/nine/s1-fabric-vs-power-bi/s1-fabric-vs-power-bi.mp4` (house style, AI stand-in voice, no face). Shot list:

| # | Say | Picture (example cut) |
|---|---|---|
| 1 | Microsoft Fabric or Power BI: which one should you learn? | First frame (the thumbnail): **FABRIC / OR POWER BI?** |
| 2 | It's the wrong question. | Text card: It's the **wrong question**. |
| 3 | Power BI isn't competing with Fabric. Power BI is inside Fabric. | Real screen `fabric-arch.png` (MICROSOFT LEARN · CC BY 4.0), phrase boxed |
| 4 | Fabric is the whole kitchen: getting data in, storing it, cleaning it, and serving it. | Stage words in big yellow caps, each on its spoken word: GET DATA IN · STORE IT · CLEAN IT · SERVE IT |
| 5 | Everything lands in one lake, OneLake, as open Delta tables. | Real screen `onelake-engines.png` (MICROSOFT LEARN · CC BY 4.0), phrase boxed |
| 6 | Then Power BI reads those tables directly. That's Direct Lake. No import copy, and a refresh only copies metadata. | Real screen `directlake.png` (MICROSOFT LEARN), phrase boxed |
| 7 | So if you already know Power BI, you're not starting over. You're one layer up from where Fabric starts. | Text card: You're not starting over. You're **one layer up**. |
| 8 | Learn the lakehouse, a little SQL, and how data gets into OneLake. | Stage words in big yellow caps, each on its spoken word: THE LAKEHOUSE · A LITTLE SQL · DATA INTO ONELAKE |
| 9 | That's the difference between a report builder and the person who owns the data. | Text card: Report builder vs. the person who **owns the data**. |
| 10 | Comment FABRIC and I'll send you the free learning path I'd follow. | Call to action: COMMENT “FABRIC” |

---

## 2. The free DP-700 path

| | |
| --- | --- |
| Set | Set 1 |
| File | `fabric-scripts.md` |
| Length | ~70 s (example cut: 44 s) |
| Keyword | — |

**Inspired by:**
- [@shreya.knows.data, "Microsoft is giving away 100% FREE exam vouchers for DP-600, DP-700…"](https://www.tiktok.com/@shreya.knows.data/video/7659620910105677076): 43,638 views.

**What we took:** A free-offer hook. Rewritten as "be ready for the next round" because that offer closed Aug 10 2026.

**Script:**

> Microsoft gave away free Fabric certification exams this summer.

> And most people missed it because they weren't ready.

> The last round, Fabric Data Days, closed in August.

> To get a voucher you had to join the Fabric Community, watch sessions and finish Microsoft Learn modules.

> So here's how to be ready before the next one drops.

> One: pick DP-700, the Fabric Data Engineer exam, or DP-600 if you're a Power BI person.

> Two: do the free Microsoft Learn path for it now. It's the same content the vouchers asked for.

> Three: take the free practice assessment until you pass it twice.

> Then when the vouchers come back, you claim one and book the exam the same week.

> Follow so you hear about the next round the day it opens.

**Facts from** (re-checked Oct 22 2026):
- [Microsoft Reactor, Fabric Data Days 2026 series](https://developer.microsoft.com/en-us/reactor/series/s-1675/): sessions ran Jun 16 – Aug 6 2026, "we may have a voucher offer available"
- [DP-700 certification page](https://learn.microsoft.com/en-us/credentials/certifications/fabric-data-engineer-associate/) and the [DP-600 page](https://learn.microsoft.com/en-us/credentials/certifications/fabric-analytics-engineer-associate/) (updated 10/19/2026)

**Changed from the original wording** (the fact-check):
- Hook: "twice in the last year" → **"this summer"**. No official page we could open confirms a Dec 2025 voucher round (the script's own ⚠ fallback).

**Keep exact / check before filming:**
- ⚠ The entry steps (join the Community, watch sessions, finish Learn modules; requests by Aug 10) come from the official terms page aka.ms/FabCert/2026, which blocks the cloud container. Open it in your browser before filming.

**Example cut:** `docs/reels/demo/nine/s2-free-dp700-path.json` → `~/persa-shorts/nine/s2-free-dp700-path/s2-free-dp700-path.mp4` (house style, AI stand-in voice, no face). Shot list:

| # | Say | Picture (example cut) |
|---|---|---|
| 1 | Microsoft gave away free Fabric certification exams this summer. | First frame (the thumbnail): **FREE FABRIC / EXAMS** · "this summer" |
| 2 | And most people missed it because they weren't ready. | Text card: Most people **missed it**. They weren't ready. |
| 3 | The last round, Fabric Data Days, closed in August. | Text card: Fabric Data Days: **closed in August**. |
| 4 | To get a voucher you had to join the Fabric Community, watch sessions and finish Microsoft Learn modules. | Stage words in big yellow caps, each on its spoken word: JOIN THE COMMUNITY · WATCH SESSIONS · FINISH LEARN MODULES |
| 5 | So here's how to be ready before the next one drops. | Text card: Be ready for **the next one**. |
| 6 | One: pick DP-700, the Fabric Data Engineer exam, or DP-600 if you're a Power BI person. | Giant outlined **1** · PICK YOUR EXAM · DP-700 Data Engineer · DP-600 if you're a Power BI person |
| 7 | Two: do the free Microsoft Learn path for it now. It's the same content the vouchers asked for. | Giant outlined **2** · DO THE FREE PATH · on Microsoft Learn, now |
| 8 | Three: take the free practice assessment until you pass it twice. | Real screen `dp700.png` (MICROSOFT LEARN) · tag "3 · PRACTICE ASSESSMENT" |
| 9 | Then when the vouchers come back, you claim one and book the exam the same week. | Text card: Vouchers back? Claim one. **Book that week.** |
| 10 | Follow so you hear about the next round the day it opens. | Call to action: FOLLOW (for the next round) |

---

## 3. Future data analysts will be using Fabric

| | |
| --- | --- |
| Set | Set 1 |
| File | `fabric-scripts.md` |
| Length | ~60 s (example cut: 44 s) |
| Keyword | — |

**Inspired by:**
- [@shreya.knows.data, "Future Data Analysts will be using Microsoft Fabric"](https://www.tiktok.com/@shreya.knows.data/video/7635415703377448212): 82,211 views, 11.9× her followers (her best post).

**What we took:** The same claim hook, then three reasons and what to learn first.

**Script:**

> Future data analysts will be using Microsoft Fabric.

> Not because it's new. Because of three things.

> One: one copy of the data. Every tool reads the same lake, so nobody's arguing about whose numbers are right.

> Two: one capacity. It pays the compute for pipelines, SQL, Spark and Power BI.

> Three: AI built in. Data agents answer questions in plain English, on top of the models you already built.

> Which means the analyst who understands the whole flow gets the job, not just the one who builds charts.

> So learn SQL, keep Power BI, and add one thing: the lakehouse.

> That's the DP-600 exam, and it's the skill set most Fabric job posts I've seen list.

> Follow for one Fabric skill a day.

**Facts from** (re-checked Oct 22 2026):
- OneLake (one copy), capacity, data agents: the field guide and [Fabric licences](https://learn.microsoft.com/en-us/fabric/enterprise/licenses)
- [Data agent concepts](https://learn.microsoft.com/en-us/fabric/data-science/concept-data-agent) (2026-05-11)
- The DP-600 exam page on Microsoft Learn

**Changed from the original wording** (the fact-check):
- "Two: one bill. A single capacity pays for…" → **"Two: one capacity. It pays the compute for pipelines, SQL, Spark and Power BI."** Storage is billed separately, and below F64 report viewers still need Power BI Pro.
- "the skill set every Fabric job posting lists" → **"the skill set most Fabric job posts I've seen list"** (the script's own ⚠ fallback). Check 10 postings to say more.

**Example cut:** `docs/reels/demo/nine/s3-future-analysts-fabric.json` → `~/persa-shorts/nine/s3-future-analysts-fabric/s3-future-analysts-fabric.mp4` (house style, AI stand-in voice, no face). Shot list:

| # | Say | Picture (example cut) |
|---|---|---|
| 1 | Future data analysts will be using Microsoft Fabric. | First frame (the thumbnail): **FUTURE ANALYSTS / USE FABRIC** |
| 2 | Not because it's new. Because of three things. | Giant outlined **3** · REASONS |
| 3 | One: one copy of the data. Every tool reads the same lake, so nobody's arguing about whose numbers are right. | Real screen `onelake-engines.png` (MICROSOFT LEARN · CC BY 4.0), phrase boxed · tag "1 · ONE COPY OF THE DATA" |
| 4 | Two: one capacity. It pays the compute for pipelines, SQL, Spark and Power BI. | Giant outlined **2** · ONE CAPACITY · compute for pipelines · SQL · Spark · Power BI |
| 5 | Three: AI built in. Data agents answer questions in plain English, on top of the models you already built. | Real demo clip `agent-reasoning.mp4` (Microsoft Learn, CC BY 4.0) · tag "3 · AI BUILT IN" |
| 6 | Which means the analyst who understands the whole flow gets the job, not just the one who builds charts. | Text card: The analyst who knows **the whole flow** gets the job. |
| 7 | So learn SQL, keep Power BI, and add one thing: the lakehouse. | Stage words in big yellow caps, each on its spoken word: LEARN SQL · KEEP POWER BI · ADD THE LAKEHOUSE |
| 8 | That's the DP-600 exam, and it's the skill set most Fabric job posts I've seen list. | Text card: That's **DP-600**: the skill set most Fabric job posts list. |
| 9 | Follow for one Fabric skill a day. | Call to action: FOLLOW (one Fabric skill a day) |

---
