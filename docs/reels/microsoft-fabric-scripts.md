# Set 2: Microsoft Fabric scripts (modelled on @selectdata, @jennytumay, @dhany.indraswara, @mampolokeng_1)

Brought into this repo on Oct 22 2026 from the summary "All scripts and what inspired them" (`all-scripts-and-inspirations.md`). The wording matches that summary except where the Oct 22 fact-check changed it; each change is listed under its script. The inspiration numbers are from the original TikTok and YouTube research; they were not re-pulled here (TikTok needs the ScrapeCreators key). Example cuts are in the house style (`content-machine/formats.md`) with a free local AI stand-in voice; replace it with your own take.

## 4. The Fabric interview question Power BI people miss

| | |
| --- | --- |
| Set | Set 2 |
| File | `microsoft-fabric-scripts.md` |
| Length | ~55 s (example cut: 49 s) |
| Keyword | — |

**Inspired by:**
- [@selectdata, SQL interview question](https://www.tiktok.com/@selectdata/video/7667345672042974481): 266K views, 10.7K saves (4.0%), 26× the account's median.

**What we took:** Question, four options, a pause, the answer, then one expert detail.

**Script:**

> Here's a Microsoft Fabric interview question that trips up Power BI people.

> Your sales data lives in a lakehouse, as Delta tables in OneLake.

> The report needs import speed, but nobody wants to wait for an import refresh.

> Which storage mode? A, Import. B, DirectQuery. C, Direct Lake. D, Dual.

> Pause, and lock in your answer.

> It's C. Direct Lake.

> Power BI loads the Delta columns straight from OneLake, and a refresh only copies metadata, in a few seconds.

> Now the answer that gets you the job: there are two kinds of Direct Lake.

> Direct Lake on SQL falls back to DirectQuery when the SQL endpoint has row-level security, and can get slower.

> Direct Lake on OneLake never falls back, but it doesn't apply that SQL security either.

> Comment the answer you picked before the reveal.

**Facts from** (re-checked Oct 22 2026):
- [Direct Lake overview](https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-overview): two options, on OneLake and on SQL; SQL endpoint RLS "queries will fall back to DirectQuery mode"; "DirectQuery fallback isn't supported by Direct Lake on OneLake" (2026-09-02)
- [Storage modes](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-storage-mode): Import, DirectQuery, Direct Lake, Dual

**Changed from the original wording** (the fact-check):
- "and gets slower" → **"and can get slower"** (Microsoft: fallback "might result in slower query performance").

**Keep exact / check before filming:**
- If you mention patient data: on OneLake, SQL-endpoint RLS is skipped, so the security has to live in OneLake security or the semantic model.

**Example cut:** `docs/reels/demo/nine/s4-fabric-interview-question.json` → `~/persa-shorts/nine/s4-fabric-interview-question/s4-fabric-interview-question.mp4` (house style, AI stand-in voice, no face). Shot list:

| # | Say | Picture (example cut) |
|---|---|---|
| 1 | Here's a Microsoft Fabric interview question that trips up Power BI people. | First frame (the thumbnail): **FABRIC / INTERVIEW Q** · "that trips up Power BI people" |
| 2 | Your sales data lives in a lakehouse, as Delta tables in OneLake. | Text card: Sales data: **Delta tables** in a lakehouse, in OneLake. |
| 3 | The report needs import speed, but nobody wants to wait for an import refresh. | Text card: Import speed. **No import refresh.** |
| 4 | Which storage mode? A, Import. B, DirectQuery. C, Direct Lake. D, Dual. | Quiz card "Which storage mode?": A Import · B DirectQuery · C Direct Lake · D Dual |
| 5 | Pause, and lock in your answer. | Quiz card "Lock in your answer": A Import · B DirectQuery · C Direct Lake · D Dual · tag "PAUSE" |
| 6 | It's C. Direct Lake. | Quiz card "It's C": A Import · B DirectQuery · C Direct Lake · D Dual (C lights up) |
| 7 | Power BI loads the Delta columns straight from OneLake, and a refresh only copies metadata, in a few seconds. | Real screen `directlake.png` (MICROSOFT LEARN), phrase boxed |
| 8 | Now the answer that gets you the job: there are two kinds of Direct Lake. | Real screen `dl-type.png` (MICROSOFT LEARN · CC BY 4.0), phrase boxed |
| 9 | Direct Lake on SQL falls back to DirectQuery when the SQL endpoint has row-level security, and can get slower. | Text card: On SQL: row-level security → **falls back** to DirectQuery. |
| 10 | Direct Lake on OneLake never falls back, but it doesn't apply that SQL security either. | Text card: On OneLake: **never falls back**, and skips that SQL security. |
| 11 | Comment the answer you picked before the reveal. | Call to action: YOUR ANSWER (comment) |

---

## 5. Your boss is about to ask Power BI questions in plain English

| | |
| --- | --- |
| Set | Set 2 |
| File | `microsoft-fabric-scripts.md` |
| Length | ~65 s (example cut: 59 s) |
| Keyword | — |

**Inspired by:**
- [@selectdata, "Claude + Power BI"](https://www.tiktok.com/@selectdata/video/7636938088559758593): 237K views, 10.8K saves (4.6%).
- [@jennytumay, PBIP for vibecoding reports with AI](https://www.tiktok.com/@jennytumay/video/7669200559345290527): 43K views, 17.9× her median.

**What we took:** AI does a Power BI job, here's how, here are the catches.

**Script:**

> Your boss is about to ask your Power BI data questions in plain English.

> In Microsoft Fabric, the thing that answers is a data agent.

> You point it at up to five sources: semantic models, a warehouse, a KQL database.

> It turns the question into DAX, SQL or KQL, runs it, and answers.

> And you can publish it to Teams, Microsoft 365 Copilot, Copilot Studio, or any AI app that speaks MCP.

> Which means the semantic model you built for reports is now what the AI reads.

> Three catches before you demo it.

> One: it's read-only. It answers questions; it doesn't change data.

> Two: it answers in English, and it isn't on the free trial.

> Three: every question uses capacity. Microsoft's own example question costs about 400 CU-seconds, so watch the bill.

> The skill that matters now is a clean semantic model, because that's what the AI is reading.

> Follow, and next I'll build one live.

**Facts from** (re-checked Oct 22 2026):
- [Data agent concepts](https://learn.microsoft.com/en-us/fabric/data-science/concept-data-agent): up to five sources; NL2SQL, NL2DAX, NL2KQL; read-only queries; no non-English; needs paid F2+ (2026-05-11)
- Publishing: [Microsoft 365 Copilot and Teams](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-microsoft-365-copilot) (preview), [Copilot Studio](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-microsoft-copilot-studio) (preview), [MCP](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-mcp-server)
- [Copilot and AI consumption](https://learn.microsoft.com/en-us/fabric/fundamentals/copilot-fabric-consumption): billed per token; Microsoft's worked example comes to 400 CU seconds

**Changed from the original wording** (the fact-check):
- "every question uses capacity, about 400 CU-seconds" → **"every question uses capacity. Microsoft's own example question costs about 400 CU-seconds"**. Data agents are billed by tokens, not per question.

**Keep exact / check before filming:**
- Two publishing routes are in preview; say "some still in preview" if asked.

**Example cut:** `docs/reels/demo/nine/s5-boss-plain-english.json` → `~/persa-shorts/nine/s5-boss-plain-english/s5-boss-plain-english.mp4` (house style, AI stand-in voice, no face). Shot list:

| # | Say | Picture (example cut) |
|---|---|---|
| 1 | Your boss is about to ask your Power BI data questions in plain English. | First frame (the thumbnail): **PLAIN-ENGLISH / QUESTIONS** · "on your Power BI data" |
| 2 | In Microsoft Fabric, the thing that answers is a data agent. | Text card: What answers? **A data agent.** |
| 3 | You point it at up to five sources: semantic models, a warehouse, a KQL database. | Real screen `agent-sources.png` (MICROSOFT LEARN), phrase boxed |
| 4 | It turns the question into DAX, SQL or KQL, runs it, and answers. | Real demo clip `agent-reasoning.mp4` (Microsoft Learn, CC BY 4.0) |
| 5 | And you can publish it to Teams, Microsoft 365 Copilot, Copilot Studio, or any AI app that speaks MCP. | Real screen `publish.png` (MICROSOFT LEARN · CC BY 4.0) · tag "PUBLISH IT" |
| 6 | Which means the semantic model you built for reports is now what the AI reads. | Text card: Your semantic model is **what the AI reads**. |
| 7 | Three catches before you demo it. | Giant outlined **3** · CATCHES |
| 8 | One: it's read-only. It answers questions; it doesn't change data. | Giant outlined **1** · READ-ONLY · it answers; it doesn't change data |
| 9 | Two: it answers in English, and it isn't on the free trial. | Giant outlined **2** · ENGLISH, NO TRIAL |
| 10 | Three: every question uses capacity. Microsoft's own example question costs about 400 CU-seconds, so watch the bill. | Giant outlined **3** · IT USES CAPACITY · billed by tokens · ~400 CU-seconds in Microsoft's example |
| 11 | The skill that matters now is a clean semantic model, because that's what the AI is reading. | Text card: The skill now: a **clean semantic model**. |
| 12 | Follow, and next I'll build one live. | Call to action: FOLLOW (next: I build one live) |

---

## 6. 3 free things Microsoft gives you to learn Fabric

| | |
| --- | --- |
| Set | Set 2 |
| File | `microsoft-fabric-scripts.md` |
| Length | ~50 s (example cut: 45 s) |
| Keyword | — |

**Inspired by:**
- [@dhany.indraswara, "Need Power BI dashboard ideas? 100+ free files"](https://www.tiktok.com/@dhany.indraswara/video/7660163521614777620): 74K views, 4.4% saves.
- [@mampolokeng_1, green-screen posts about free programs](https://www.tiktok.com/@mampolokeng_1): 477K, 134K and 88K views.

**What we took:** A numbered list of free things, the real page behind you, and "save this".

**Script:**

> Three free things Microsoft gives you to learn Fabric. Save this.

> One: a 60-day Fabric trial, a real capacity you can build on.

> No Copilot or data agents on the trial, but lakehouses, pipelines and Power BI are there to practice on.

> Two: the official practice assessment for the DP-700 exam, free on Microsoft Learn.

> Same style, wording and difficulty as the real questions, and it shows you where you're weak.

> Three: the exam sandbox. You click through the real exam interface before exam day.

> And the exam is 100 minutes, so practice with a timer.

> Already certified? Renewing is free too: an online assessment on Microsoft Learn.

> Save this, and send it to the friend who keeps saying they'll start Fabric next month.

**Facts from** (re-checked Oct 22 2026):
- [DP-700 certification page](https://learn.microsoft.com/en-us/credentials/certifications/fabric-data-engineer-associate/): practice assessment, exam sandbox, "You will have 100 minutes", renewal "at no cost" (10/19/2026)
- [Fabric trial](https://learn.microsoft.com/en-us/fabric/fundamentals/fabric-trial): "free access for 60 days"; Copilot and data agents not supported (2026-08-12)

**Keep exact / check before filming:**
- The trial is an F4 or an F64 capacity now; don't promise a free F64.

**Example cut:** `docs/reels/demo/nine/s6-three-free-things.json` → `~/persa-shorts/nine/s6-three-free-things/s6-three-free-things.mp4` (house style, AI stand-in voice, no face). Shot list:

| # | Say | Picture (example cut) |
|---|---|---|
| 1 | Three free things Microsoft gives you to learn Fabric. Save this. | First frame (the thumbnail): **3 FREE THINGS / TO LEARN FABRIC** · "save this" |
| 2 | One: a 60-day Fabric trial, a real capacity you can build on. | Real screen `trial.png` (MICROSOFT LEARN), phrase boxed · tag "1 · THE TRIAL" |
| 3 | No Copilot or data agents on the trial, but lakehouses, pipelines and Power BI are there to practice on. | Text card: No Copilot or data agents. **Lakehouses, pipelines, Power BI:** yes. |
| 4 | Two: the official practice assessment for the DP-700 exam, free on Microsoft Learn. | Real screen `dp700.png` (MICROSOFT LEARN) · tag "2 · PRACTICE ASSESSMENT" |
| 5 | Same style, wording and difficulty as the real questions, and it shows you where you're weak. | Text card: Same style, wording, difficulty. Shows **where you're weak**. |
| 6 | Three: the exam sandbox. You click through the real exam interface before exam day. | Real screen `dp700-b.png` (MICROSOFT LEARN) · tag "3 · EXAM SANDBOX" |
| 7 | And the exam is 100 minutes, so practice with a timer. | Giant outlined **100** · MINUTES · practice with a timer |
| 8 | Already certified? Renewing is free too: an online assessment on Microsoft Learn. | Text card: Renewing? **Free**: an online assessment. |
| 9 | Save this, and send it to the friend who keeps saying they'll start Fabric next month. | Call to action: SAVE THIS (and send it to a friend) |

---
