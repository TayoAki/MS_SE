# Can Fabric Apps replace Power BI?
keyword: APPS · format: F3 X vs Y with the title held, modelled on Alex The Analyst "Data Analyst vs Business Analyst"
(215K, 11.3× his Shorts median), numbered cards from F2 (`content-machine/formats.md`) · 150 words · ≈ 53 s
funnel: reach · pillar: P2 · calendar: week 1 video A (recreation RC1) · story: none (docs-led)
recreates: Guy in a Cube "Can Fabric Apps REPLACE Power BI?" (55,987 views, 4.0× channel median) and the same question on
four more channels — `content-machine/recreate-list.md`, inspo board https://claude.ai/artifact/QbNCXv6ohGPRSfjCkpWryF

## Beats
hook: is Power BI done? → bridge: what Fabric Apps is → meat: 3 reasons it won't replace Power BI → mic drop: reports are
for reading the numbers, apps are for changing them → CTA: comment APPS

## Hooks (pick one)
1. "Can Fabric Apps replace Power BI? Short answer: no. Here's why." · on screen: POWER BI / DONE? · shape: the proven
   question (recreation) · score: 4/6 on HOOKS.md (product first, no moment) — kept on purpose: five channels proved this
   exact question · numbers from: —
2. "Your Power BI reports aren't going anywhere. Here's what Fabric Apps is actually for." · on screen: REPORTS STAY ·
   shape: the line people believe · score: 5/6 · numbers from: —
3. "Everyone's asking if Fabric Apps kills Power BI. I read the docs so you don't have to." · on screen: KILLS POWER BI? ·
   shape: the question you can't answer · score: 5/6 · numbers from: — (true only once you've read them)

## Script
Can Fabric Apps replace Power BI? Short answer: no. Here's why.
Fabric Apps lets developers build full apps on Fabric. You write the data model in TypeScript.
It generates the APIs, handles sign-in, and hosts the app for you.
And it reads a lakehouse, a warehouse, a SQL database or a semantic model.
So it's built for people entering and changing data, not just looking at it.
But replace Power BI? Three reasons it won't.
One: it's code. It's built for TypeScript developers, not report builders.
Two: it's in preview, and a tenant admin has to switch it on.
Three: every read and every write bills your Fabric capacity, and it isn't in every region yet.
Reports are for reading the numbers. Apps are for changing them.
In a hospital, that's the Excel tracker your unit emails around. Not the dashboard.
Comment APPS and I'll send you the one-page comparison.

## Facts   (all re-opened on Microsoft Learn 2026-10-21 — re-check the week you film)
| claim | value | source link |
|---|---|---|
| preview, Rayfin SDK, TypeScript data models, generates APIs, handles authentication, provides hosting | "Fabric Apps (preview) is built on the Rayfin SDK… Developers define data models in TypeScript, and Fabric Apps automatically generates APIs, handles authentication, provides hosting" | [Fabric Apps overview](https://learn.microsoft.com/en-us/fabric/apps/overview) (ms.date 2026-09-15) |
| reads lakehouse, warehouse, SQL database, semantic model | "Add typed access to a lakehouse, warehouse, SQL database in Fabric, or semantic model" | same |
| reads and writes | "The client SDK validates queries and mutations" | same |
| tenant admin must enable | "A Fabric tenant administrator must enable the Fabric Apps workload" | same |
| not in every region | "Fabric Apps are not avaiable in all regions yet" | same |
| every read and write uses capacity | "Fabric apps run on Fabric capacity. Every operation that a Fabric app child service performs consumes CUs" · "Every GraphQL query (read) and mutation (write)… consumes CUs" | [Pricing and capacity usage](https://learn.microsoft.com/en-us/fabric/apps/pricing) (ms.date 2026-09-15) |
| can be built with Claude Code | page title "Create a Fabric app with Claude Code" | [Create a Fabric app with Claude Code](https://learn.microsoft.com/en-us/fabric/apps/create-app-with-claude-code) |
⚠ Don't say reports can't write data — Power BI has write-back (field guide: translytical apps with a SQL database in Fabric).
⚠ If Fabric Apps is GA by filming day, rewrite line 8.

## Cover text
FABRIC APPS vs POWER BI. It is the held title (v2), on screen from the first frame to the call to action, so the first
frame is the LinkedIn thumbnail. v1 used POWER BI / DONE? as big first-frame words: `docs/reels/demo/rc1.json`.

## On screen
real 9:16 Microsoft Learn page shots, phrase highlighted on the word (already shot, in `~/persa-shorts/rc1-fabric-apps/
assets/pages/`): overview intro · key features · connectors · queries and mutations · Create a Fabric app with Claude Code ·
tenant admin settings · pricing "How billing works". Best upgrade: 10–15 s of your own screen — the Fabric Apps item in
your demo workspace, or an app you scaffolded — over lines 2–5. Built example: `docs/reels/demo/rc1-v2.json`
(v2: the held title, a numbered card on each reason (#1 IT'S CODE, #2 PREVIEW, #3 BILLS YOUR CAPACITY), keywords in the
accent colour, timed at 3 words a second). v1: `docs/reels/demo/rc1.json`.
Licences (`systems/3-editor/BROLL.md`): the Learn page shots are CC BY 4.0, credited in the post. Fabric Apps is in
preview, so Microsoft's screenshot permission doesn't cover your own screen of it. Filming it relies on fair use: decide
before you record.

## The free thing
DELIVERABLE.md in this folder — Fabric Apps vs Power BI reports, one page.

## LinkedIn post
Can Fabric Apps replace Power BI? No.
It's built for a different job: people entering and changing data.

Fabric Apps (preview) lets developers build full apps on Fabric: data model in TypeScript, APIs, sign-in and hosting
generated for you, reading from a lakehouse, warehouse, SQL database or semantic model.

Why it won't replace your reports:
- It's code, for TypeScript developers
- It's in preview, and a tenant admin has to enable it
- Every read and write bills your Fabric capacity, and it isn't in every region yet

Reports are for reading the numbers. Apps are for changing them.

Comment APPS and I'll send you the one-page comparison.
#MicrosoftFabric #PowerBI

Screens: Microsoft Learn, CC BY 4.0 (cropped, highlighted)
