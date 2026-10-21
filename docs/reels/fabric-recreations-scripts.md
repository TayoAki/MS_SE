# Microsoft Fabric recreations — scripts (Persa Shorts edit, 9:16)

Five ~60–75 s scripts that recreate Fabric videos which already beat their channel's median on YouTube (pulled
2026-10-21): the same topic, title shape and structure — our own words, our own screens, facts checked on Microsoft Learn
on 2026-10-21. The list and the evidence: `content-machine/recreate-list.md`, `docs/reels/fabric-health-systems-research.md`.
We couldn't watch the originals (YouTube blocks video pages from the cloud container), so each script delivers the
original's title promise, not its beat order; paste a transcript to recreate one beat for beat.

## The formula these share
- **Hook = the original's title shape:** a direct question ("Can X replace Y?", "What is X?"), a "which one?" choice, a
  test ("We tested X"), or a skeptic's "why people push back".
- **Structure:** answer the question in one line → three concrete points → the catch → one line of opinion → CTA.
- **Length:** the originals run 4–15 min on YouTube; for 9:16 LinkedIn we keep the promise and cut to 60–75 s.
- **CTA:** comment a keyword for a one-page cheat sheet (reference content).

## How to record
Sit a little further back with room above your head. All five in one sitting; repeat any fluffed line. For each "screen"
row, record your own screen on a demo tenant or synthetic data. Then: "Edit ~/content-machine/recordings/<file> with
nextphase-persa-shorts, script: docs/reels/fabric-recreations-scripts.md, RC<n>".

---

## RC1 — "Can Fabric Apps replace Power BI?" (~60 s)

Recreates: [Guy in a Cube, "Can Fabric Apps REPLACE Power BI?"](https://www.youtube.com/watch?v=SStJcXn5vGE) — 55,987 views, 4.0× — and the same question on four more channels ([How to Power BI, 185,454, 3.3×](https://www.youtube.com/watch?v=p0gzrFG868w); [Data Goblins, 52,879, 17.1×](https://www.youtube.com/watch?v=b3dybvW5WdA)).

**Hook (caption + post title):** Can Fabric Apps replace Power BI?

Built as an example cut (real Microsoft Learn page shots, silhouette for the creator): `docs/reels/demo/rc1.json` →
`build_short.py`. Script folder: `content-machine/scripts/2026-10-26-01-fabric-apps-vs-power-bi/`.

| # | Say | Picture | Source |
|---|---|---|---|
| 1 | "Can Fabric Apps replace Power BI? Short answer: no. Here's why." | face; first frame FABRIC APPS vs POWER BI | — |
| 2 | "Fabric Apps lets developers build full apps on Fabric. You write the data model in TypeScript." | 9:16 shot of the Fabric Apps overview | [Fabric Apps overview](https://learn.microsoft.com/en-us/fabric/apps/overview) |
| 3 | "It generates the APIs, handles sign-in, and hosts the app for you." | same page, "Key features" | same |
| 4 | "And it reads a lakehouse, a warehouse, a SQL database or a semantic model." | same page, "Fabric data connectors" | same |
| 5 | "So it's built for people entering and changing data, not just looking at it." | face; display word CHANGE | same (queries and mutations) |
| 6 | "But replace Power BI? Three reasons it won't." | display 3 REASONS | — |
| 7 | "One: it's code. It's built for TypeScript developers, not report builders." | the TypeScript line on the page | same |
| 8 | "Two: it's in preview, and a tenant admin has to switch it on." | the preview note + the tenant-settings step | same |
| 9 | "Three: every read and every write bills your Fabric capacity, and it isn't in every region yet." | the Pricing page, "How billing works" | [Pricing and capacity usage](https://learn.microsoft.com/en-us/fabric/apps/pricing) |
| 10 | "Reports are for reading the numbers. Apps are for changing them." | face; display word CHANGING | — |
| 11 | "In a hospital, that's the Excel tracker your unit emails around. Not the dashboard." | face; hollow word TRACKER | — |
| 12 | "Comment APPS and I'll send you the one-page comparison." | COMMENT APPS + arrow | — |

**Keep exact:**
- "Fabric Apps (preview) is built on the Rayfin SDK… Developers define data models in TypeScript, and Fabric Apps automatically generates APIs, handles authentication, provides hosting, and integrates with Fabric services." (ms.date 2026-09-15)
- "Fabric data connectors – Add typed access to a lakehouse, warehouse, SQL database in Fabric, or semantic model." · "A Fabric tenant administrator must enable the Fabric Apps workload" · "Fabric Apps services consume capacity units" · "Fabric Apps are not avaiable in all regions yet." (same page)
- "Fabric apps run on Fabric capacity. Every operation that a Fabric app child service performs consumes CUs" · "Every GraphQL query (read) and mutation (write)… consumes CUs." (Pricing, ms.date 2026-09-15)
- Line 5 rests on "The client SDK validates queries and mutations" → fallback: "So apps can write data back, not just show it."
- Don't say reports can't write data: Power BI has write-back through translytical task flows with a SQL database in Fabric (`content-machine/fabric-field-guide.md`, use-case table).
- If Fabric Apps is GA by filming day, rewrite line 8.

**Post caption:** Can Fabric Apps replace Power BI? No — it's built for a different job: people entering and changing data.
It's TypeScript, it's in preview, a tenant admin has to enable it, and it runs on your capacity. Reports are for reading
the numbers; apps are for changing them. Comment APPS for the one-page comparison. #MicrosoftFabric #PowerBI

---

## RC2 — "Import, DirectQuery or Direct Lake?" (~70 s)

Recreates: the storage-modes explainer — [Guy in a Cube, "Choosing Import, DirectQuery, or Live Connections Explained"](https://www.youtube.com/watch?v=-ip7mKUdwRg) (428,000, 2021, date approximate) and [Data with Baraa, "Power BI Direct Query (Explained Visually)"](https://www.youtube.com/watch?v=QR03oeguXF8) (40,272, 2026).

**Hook (caption + post title):** Import, DirectQuery or Direct Lake? The difference in 60 seconds.

| # | Say | Picture | Source |
|---|---|---|---|
| 1 | "Import, DirectQuery or Direct Lake? Here's the difference in sixty seconds." | face; first frame IMPORT · DIRECTQUERY · DIRECT LAKE | — |
| 2 | "Import copies your data into the model. That's why it's fast." | your screen: a model's storage mode set to Import | [Semantic model modes](https://learn.microsoft.com/en-us/power-bi/connect-data/service-dataset-modes-understand) |
| 3 | "But it's only as current as the last refresh, and a refresh loads it all into memory again." | the refresh history | same |
| 4 | "DirectQuery imports nothing. Every visual asks the source." | your screen: a DirectQuery model | same |
| 5 | "So it's as fresh as the source, and only as fast as the source." | face | general behaviour (see Keep exact) |
| 6 | "Direct Lake is the third option. It loads Delta tables straight from OneLake." | 9:16 shot of the Direct Lake overview | [Direct Lake overview](https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-overview) |
| 7 | "Queries run on the same engine as Import, so speed is comparable." | same page, the VertiPaq line | same |
| 8 | "And a refresh copies only metadata. It's called framing, and it can take seconds." | same page, "framing"; claim typed in its gutter: REFRESH = SECONDS | same |
| 9 | "One catch: on a SQL analytics endpoint, a view or SQL-based security sends it back to DirectQuery." | same page, the fallback line; hollow word FALLBACK | same |
| 10 | "So: small and simple, Import. Must be live from another system, DirectQuery. Already in OneLake, Direct Lake." | three labels on screen | rule of thumb (opinion) |
| 11 | "That's why a morning census dashboard on Fabric data is a good fit for Direct Lake." | face | opinion — say it as yours |
| 12 | "Comment MODES and I'll send you the one-page cheat sheet." | COMMENT MODES + arrow | — |

**Keep exact:**
- "Import mode replicates the data and creates an entire cached copy… whereas a Direct Lake refresh copies only metadata (known as framing…), which can take a few seconds to complete." (Direct Lake overview, ms.date 2026-09-02)
- "Direct Lake queries are processed by the VertiPaq engine, and thus deliver query performance comparable to Import mode." (same)
- "Direct Lake on SQL analytics endpoints fall back to DirectQuery table storage mode… when the data source is a SQL view or when the warehouse uses SQL-based granular access control." · "Direct Lake on OneLake doesn't fall back to DirectQuery mode." (same) → say "on a SQL analytics endpoint" every time.
- "Model data is only as current as the latest refresh" · "Models developed in DirectQuery mode don't import data." (Semantic model modes, ms.date 2025-02-28)
- Line 5 is general DirectQuery behaviour, not a quote → fallback: "So it's always current — and it depends on that source to be quick."

**Post caption:** Import, DirectQuery or Direct Lake? Import copies the data (fast, as fresh as the last refresh).
DirectQuery asks the source every time. Direct Lake reads Delta tables from OneLake and refreshes metadata in seconds —
watch the DirectQuery fallback on SQL analytics endpoints. Comment MODES for the cheat sheet. #PowerBI #MicrosoftFabric

---

## RC3 — "What is Fabric IQ?" (~60 s)

Recreates: [Guy in a Cube, "What Is Fabric IQ?! Microsoft Fabric's NEW Ontology Explained"](https://www.youtube.com/watch?v=XEyq1qL147M) — 45,307, 3.2× — with the topic repeating on [Microsoft Fabric's own 95 s intro](https://www.youtube.com/watch?v=RjU0slwcZGs) (20,390, 12×).

**Hook (caption + post title):** What is Fabric IQ? Microsoft's new layer, in 60 seconds.

| # | Say | Picture | Source |
|---|---|---|---|
| 1 | "What is Fabric IQ? Microsoft's new layer, in sixty seconds." | face; first frame FABRIC IQ? | — |
| 2 | "It's not more storage. It's shared meaning over the data you already have in OneLake." | 9:16 shot of the Fabric IQ overview | [Fabric IQ overview](https://learn.microsoft.com/en-us/fabric/iq/overview) |
| 3 | "Two core pieces: your semantic models, and an ontology — a map of your business a machine can read." | same page, the two core items | same |
| 4 | "The ontology is still in preview." | the "(preview)" label | same |
| 5 | "On top sit data agents: virtual analysts that answer plain-language questions, grounded in those models." | the data agent row | same |
| 6 | "You can publish them to Microsoft 365, Copilot Studio, Foundry or your own apps." | same row | same |
| 7 | "Plus Planning for forecasts on the same data, and Graph for questions about connections." | the Planning and Graph rows | same |
| 8 | "But an agent is only as right as your definitions." | face; display word DEFINITIONS | opinion |
| 9 | "If 'patient' means three things in your models, the agent gives three answers." | face; hollow word THREE | opinion (our W5 demo shows it) |
| 10 | "So fix the definitions first. Then add the agent." | face | — |
| 11 | "Comment IQ and I'll send you the one-page map of Fabric IQ." | COMMENT IQ + arrow | — |

**Keep exact:**
- "These layers are delivered through two core items in the Fabric IQ workload, ontology (preview) and semantic model, creating shared context over business data in OneLake." (Fabric IQ overview, ms.date 2026-07-08)
- "Ontology (preview) is a shared, machine-understandable representation of your business." (same)
- Data agent: "virtual analysts that connect to your Fabric data sources and answer natural language questions for a specific domain… publishable across Microsoft 365, Foundry, Copilot Studio, and custom apps." (same)
- Planning: "planning, forecasting, and reporting from a single data foundation"; Graph: "Store and query connected data with nodes, edges, and traversals" — the overview links Graph as "(preview)". (same)
- Lines 8–9 are your view → say them as yours.

**Post caption:** What is Fabric IQ? Shared meaning over your OneLake data: semantic models plus an ontology (preview),
with data agents, Planning and Graph on top. An agent is only as right as your definitions — fix those first. Comment IQ
for the one-page map. #MicrosoftFabric #PowerBI
Screens: Microsoft Learn, CC BY 4.0 (cropped, highlighted)

**Built:** `content-machine/scripts/2026-11-09-01-what-is-fabric-iq/` (script, scored hooks, facts, on-screen list,
one-page map). The example cut `docs/reels/demo/rc3.json` puts a real Learn screenshot or diagram on every line from 2
to 7, in place of the page shots in the Picture column above.

---

## RC4 — "We tested Microsoft's Power BI report skill" (~70 s) — **run the test before scripting the results**

Recreates: [Guy in a Cube, "We tested the New Power BI Report Skills"](https://www.youtube.com/watch?v=pDRSXOK6fq0) — 158,069, 11.3× — and [How to Power BI, "The New Power BI Authoring Skills Change Everything"](https://www.youtube.com/watch?v=Mf2ACp74NNQ) (155,075, 2.8×).

**Hook (caption + post title):** I gave an AI agent Microsoft's Power BI report skill and one prompt. Here's what it built.

| # | Say | Picture | Source |
|---|---|---|---|
| 1 | "I gave an AI agent Microsoft's Power BI report skill and one prompt. Here's what it built." | face; first frame the finished report (blurred) | — |
| 2 | "The skill plans, designs, builds and publishes Power BI reports from plain language." | 9:16 shot of the Power BI Report skill page | [Power BI Report skill](https://learn.microsoft.com/en-us/power-bi/developer/agentic/power-bi-report-authoring-skill-overview) |
| 3 | "My prompt: [the exact prompt], on a synthetic patient-access model." | your screen: the prompt | your test |
| 4 | "[n] minutes later: [what it built — pages, visuals]." | your screen recording of the result | your test |
| 5 | "What it got right: [1–2 things]." | the result | your test |
| 6 | "What it got wrong: [1–2 things]." | the result, the mistake highlighted; hollow word WRONG | your test |
| 7 | "And it only works on reports saved as PBIP projects in the PBIR format." | same page, "Considerations" | same page |
| 8 | "[Your verdict in one line]." | face | your test |
| 9 | "Comment SKILL and I'll send you my prompt and checklist." | COMMENT SKILL + arrow | — |

**Keep exact:**
- "The Power BI Report skill (powerbi-report-cli) is a unified AI-agent skill for planning, designing, authoring, validating, and managing Power BI reports." · "It is distributed through the Power BI authoring plugin in the Skills for Fabric marketplace." · "Local report authoring requires PBIP projects that use the PBIR report format." (ms.date 2026-09-18)
- Every bracket is filled from the real run, on synthetic data only. Don't name tools it works with unless the page you open that week says so.
- Release status: the Microsoft page doesn't label it preview in the text read on 2026-10-21; third-party coverage calls it a preview — check before saying either.

---

## RC5 — "Why teams push back on Microsoft Fabric" (~65 s)

Recreates: [Microsoft Hates Greg, "Why Customers are Rejecting Microsoft Fabric"](https://www.youtube.com/watch?v=nxW6gUFzffg) — 33,000, 112× its channel median — with our own evidence instead of opinion.

**Hook (caption + post title):** Why teams push back on Microsoft Fabric. I read 96 real requests for help.

| # | Say | Picture | Source |
|---|---|---|---|
| 1 | "Why do teams push back on Microsoft Fabric? I read ninety-six real requests for help to find out." | face; first frame 96 REQUESTS | your community research |
| 2 | "From Fabric user groups and Reddit, since launch. Not a survey — real people stuck on real things." | your spreadsheet's Summary tab | `research/fabric-community-research.xlsx` |
| 3 | "Number one, by far: capacity, cost and monitoring. Twenty-two of the ninety-six." | the topic chart; display 22 | same |
| 4 | "Then deployment and CI/CD: twelve. Getting data in: twelve." | same | same |
| 5 | "Learning and access: eleven. Security and governance: eleven." | same | same |
| 6 | "Notice what's missing: 'Fabric doesn't work.' It's 'Fabric is hard to run.'" | face; hollow word RUN | opinion |
| 7 | "Healthcare showed up seven times — including counting patients and proving who saw whose data." | the Evidence tab, healthcare rows | same |
| 8 | "So if you're planning a move, plan for cost, deployment and access before features." | face | — |
| 9 | "Comment PUSHBACK and I'll send you the list, with a link to every thread." | COMMENT PUSHBACK + arrow | — |

**Keep exact:**
- 117 discussions reviewed; 96 counted requests (firsthand problems or solution requests since 2023-05-23); topics: capacity, cost and monitoring 22 · CI/CD and deployment 12 · data ingestion and orchestration 12 · learning, access and adoption 11 · security and governance 11; healthcare and life sciences 7. (`content-machine/research/fabric-community-research.xlsx`, snapshot 2026-10-21)
- Say "in this sample" if asked — the spreadsheet itself says the counts describe a purposive sample, not market share.
- Sources: official Fabric Community user groups and r/MicrosoftFabric (Coverage tab).

**Post caption:** Why do teams push back on Microsoft Fabric? In 96 real requests for help from Fabric user groups and
Reddit, the top problem was capacity, cost and monitoring (22), then deployment (12), getting data in (12), learning and
access (11) and security (11). Not "it doesn't work" — "it's hard to run". Comment PUSHBACK for the list with links.
#MicrosoftFabric #PowerBI
