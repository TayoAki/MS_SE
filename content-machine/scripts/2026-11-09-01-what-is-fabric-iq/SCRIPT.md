# What is Fabric IQ?
keyword: IQ · format: short · 136 words · ≈ 53 s
funnel: reach · pillar: P1 · calendar: week 3 video A (recreation RC3) · story: none (docs-led; lines 8–10 are your view)
recreates: Guy in a Cube "What Is Fabric IQ?! Microsoft Fabric's NEW Ontology Explained" (45,307 views, 3.2× channel
median), with the same topic on Microsoft Fabric's own 95 s intro (20,390, 12×) and Informatec (45K):
`content-machine/recreate-list.md`, inspo board https://claude.ai/artifact/QbNCXv6ohGPRSfjCkpWryF

## Beats
hook: what is Fabric IQ? → bridge: shared meaning over OneLake → meat: the two core pieces, then what sits on top →
mic drop: an agent is only as right as your definitions → CTA: comment IQ

## Hooks (pick one)
1. "What is Fabric IQ? Microsoft's new layer, in sixty seconds." · on screen: FABRIC IQ? · shape: the proven question
   (recreation) · score: 2/6 on HOOKS.md (it names the product first, and has no problem, moment or tension). Kept for
   the built example because three channels proved this exact title. · numbers from: —
2. "Ask an AI agent how many patients you saw last month. 412? 522? 946?" then "That's the problem Fabric IQ is meant
   to fix. Here it is in sixty seconds." · on screen: PATIENTS: 412? 522? 946? · shape: the number that doesn't add up ·
   score: 6/6 · numbers from: the demo (synthetic month, `docs/reels/demo/synthetic_month.py`: 412 patients, 522 visit
   rows, 946 rows after joining diagnoses)
3. "Your data agent is only as right as your definition of 'patient'." · on screen: DEFINE "PATIENT" · shape: the line
   people believe · score: 5/6 ("data agent" sits in the first 4 words) · numbers from: —
Recommendation: film 1 and 2 in the same sitting and A/B them on two posts. The thumbnail stays FABRIC IQ? either way.

## Script
What is Fabric IQ? Microsoft's new layer, in sixty seconds.
It's not more storage. It's shared meaning over the data you already have in OneLake.
Two core pieces: your semantic models, and an ontology, a map of your business a machine can read.
The ontology is still in preview.
On top sit data agents: virtual analysts that answer plain-language questions, grounded in those models.
You can publish them to Microsoft 365, Copilot Studio, Foundry or your own apps.
Plus Planning for forecasts on the same data, and Graph for questions about connections.
But an agent is only as right as your definitions.
If "patient" means three things in your models, the agent gives three answers.
So fix the definitions first. Then add the agent.
Comment IQ and I'll send you the one-page map of Fabric IQ.

## Facts   (all re-read on Microsoft Learn 2026-10-21; re-check the week you film)
| claim | value | source link |
|---|---|---|
| shared meaning over OneLake data; two core items | "These layers are delivered through two core items in the Fabric IQ workload, ontology (preview) and semantic model, creating shared context over business data in OneLake." | [What is Fabric IQ?](https://learn.microsoft.com/en-us/fabric/iq/overview) (ms.date 2026-07-08) |
| a map a machine can read | "Ontology (preview) is a shared, machine-understandable representation of your business." | same |
| still in preview | the ontology is "(preview)"; the page also calls the whole workload "the IQ (preview) workload" | same |
| data agents: virtual analysts, plain-language questions, grounded in models, where they publish | "Create virtual analysts that connect to your Fabric data sources and answer natural language questions for a specific domain… grounded in semantic models and ontologies, publishable across Microsoft 365, Foundry, Copilot Studio, and custom apps." | same |
| Planning | "Collaborate on planning, forecasting, and reporting from a single data foundation without switching tools." | same |
| Graph | "Store and query connected data with nodes, edges, and traversals." The page links it as "Graph in Microsoft Fabric overview (preview)" | same |
| 412 / 522 / 946 (hook 2 only) | one synthetic month counted three ways | `docs/reels/demo/synthetic_month.py` (seed 20261123) |
⚠ Lines 8–10 are your opinion. Say them as yours ("in my experience…" is fine to add).
⚠ "Not more storage" is a framing, not a quote. OneLake is the foundation, and IQ adds context on top of it.
⚠ If ontology or the IQ workload is generally available by filming day, rewrite line 4.

## Cover text
FABRIC IQ? (the first frame is the LinkedIn thumbnail)

## On screen
Microsoft Learn screenshots and diagrams (MicrosoftDocs/fabric-docs, CC BY 4.0), collected with `learn_media.py` and
cropped. They are already in `~/persa-shorts/rc3-fabric-iq/assets/shots/`, and the built example is
`docs/reels/demo/rc3.json`.
| line | file | what it shows | source page |
|---|---|---|---|
| 2 | layers.png | the Fabric IQ layers, OneLake boxed | [iq/overview](https://learn.microsoft.com/en-us/fabric/iq/overview) |
| 3 (first half) | layers-b.png (copy) | same diagram, ontology and semantic models boxed | same |
| 3 (second half) | ontology-map.png | an ontology's entity types and relationships | [iq/ontology/tutorial-0-introduction](https://learn.microsoft.com/en-us/fabric/iq/ontology/tutorial-0-introduction) |
| 4 | admin-preview.png | the tenant setting "Users can create Ontology (preview) items" | [iq/ontology/overview-tenant-settings](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview-tenant-settings) |
| 5 (first half) | framework.png | the IQ framework, "Empower AI Agents" boxed | [iq/overview](https://learn.microsoft.com/en-us/fabric/iq/overview) |
| 5 (second half) | agent-chat.png | a data agent answering a plain-language question | [iq/ontology/how-to-create-data-agent](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-create-data-agent) |
| 6 | publish.png | the "Publish data agent" dialog | [data-science/data-agent-sharing](https://learn.microsoft.com/en-us/fabric/data-science/data-agent-sharing) |
| 7 (first half) | planning.jpg | a planning sheet, the Planner tab boxed | [iq/plan/infobridge-concept-connected-planning](https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-concept-connected-planning) |
| 7 (second half) | graph-new.png | New item → Graph model | [graph/tutorial-create-graph](https://learn.microsoft.com/en-us/fabric/graph/tutorial-create-graph) |
Licences (`systems/3-editor/BROLL.md`): the post carries the CC BY credit below. Ontology is in preview, so
Microsoft's screenshot permission doesn't cover your own screen of it. Keep these Learn shots, or decide on fair use
before you record your own. Hook 2's numbers on screen are your own demo, so no credit is needed.

## The free thing
DELIVERABLE.md in this folder: Fabric IQ on one page, plus the definitions-first checklist for a health system.

## LinkedIn post
What is Fabric IQ? Microsoft's new layer, in 60 seconds.
It's shared meaning over the data you already have in OneLake.

Two core pieces: your semantic models, and an ontology (still in preview), a map of your business a machine can read.
On top: data agents that answer plain-language questions, publishable to Microsoft 365, Copilot Studio, Foundry or
your own apps. Plus Planning and Graph.

But an agent is only as right as your definitions. If "patient" means three things in your models, you get three
answers.

Fix the definitions first. Then add the agent.

Comment IQ and I'll send you the one-page map of Fabric IQ.
#MicrosoftFabric #PowerBI

Screens: Microsoft Learn, CC BY 4.0 (cropped, highlighted)
