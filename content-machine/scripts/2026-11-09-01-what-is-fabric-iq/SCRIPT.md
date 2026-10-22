# Don't start with the AI agent (What is Fabric IQ?, v2)
keyword: IQ · format: F1 "Don't start with X", modelled on Alex The Analyst "Don't jump into Power BI first" (740K, 38.9×
his Shorts median), numbered cards from F2 · 128 words · ≈ 45 s
funnel: reach · pillar: P1 · calendar: week 3 video A (recreation RC3) · story: none (docs-led; the order is your advice)
topic proof: "What Is Fabric IQ?!" on 3 channels. Guy in a Cube: 45,307 views, 3.2× his median. Microsoft Fabric's
95 s intro: 20,390, 12×. Informatec: 45K. Format proof: `content-machine/formats.md` F1, and
`docs/reels/shorts-formats-research.md`.
v1 (the plain "What is Fabric IQ?" explainer, 2026-10-21) is kept as `docs/reels/demo/rc3.json`. v2 replaces it: the
proven question, recut into the format behind the biggest data Shorts.

## Beats
hook: the warning (don't give your hospital an AI agent before you fix this) → bridge: what Fabric IQ's agents are and
what they answer from → the trap: "patient" means three things, so three answers → meat: #1 one definition, #2 ontology
(preview), #3 then the agent → mic drop: meaning first, agents second → CTA: comment IQ

## Hooks (pick one)
1. "Don't give your hospital an AI agent before you fix this." · held title: DON'T START WITH THE AI AGENT · shape:
   stop doing X (HOOKS.md 8), format F1 · score: 6/6 · numbers from: —
2. "Ask an AI agent how many patients you saw last month. 412? 522? 946?" · on screen: PATIENTS: 412? 522? 946? ·
   shape: two numbers, both right · score: 6/6 · numbers from: the demo (synthetic month, `synthetic_month.py`)
3. "What is Fabric IQ? Microsoft's new layer, in sixty seconds." · on screen: FABRIC IQ? · shape: the proven question
   (v1) · score: 2/6. Its topic is proven but the hook is weak; it stays in v1.
Built with hook 1.

## Script
Don't give your hospital an AI agent before you fix this.
Fabric IQ puts data agents on top of your data: virtual analysts you ask in plain English.
They answer from your semantic models and your ontology.
So if "patient" means three things in your models, you get three answers.
Here's the order that works.
One: agree on one definition per word, and put it in the semantic model.
Two: build the ontology from that model, a map of your business a machine can read.
It's still in preview, so test it on synthetic data.
Three: then add the agent. One domain, tested on questions you already know the answers to.
Meaning first. Agents second.
Comment IQ and I'll send you the one-page map of Fabric IQ.

## Facts   (all re-read on Microsoft Learn 2026-10-21; re-check the week you film)
| claim | value | source link |
|---|---|---|
| data agents are virtual analysts you ask in plain language | "Create virtual analysts that connect to your Fabric data sources and answer natural language questions for a specific domain" | [What is Fabric IQ?](https://learn.microsoft.com/en-us/fabric/iq/overview) (ms.date 2026-07-08) |
| they answer from semantic models and the ontology | "a tailored Q&A experience grounded in semantic models and ontologies" | same |
| build the ontology from the model | "You can create ontology items from scratch or generate them from existing Power BI semantic models" | same |
| a map a machine can read | "Ontology (preview) is a shared, machine-understandable representation of your business." | same |
| still in preview | the ontology is "(preview)"; the page also calls the whole workload "the IQ (preview) workload" | same |
| one domain | "…for a specific domain" | same |
| 412 · 522 · 946 | one synthetic month counted three ways: distinct patients, visit rows, rows after joining diagnoses | `docs/reels/demo/synthetic_month.py` (seed 20261123) |
⚠ The order (#1 → #3) and "meaning first, agents second" are your advice, not Microsoft's. Say them as yours.
⚠ "Puts data agents on top" paraphrases the IQ framework diagram ("Empower AI Agents" is its top layer).
⚠ If ontology or the IQ workload is generally available by filming day, rewrite line 8.

## Cover text
DON'T START WITH THE AI AGENT. It is the held title, so the first frame is the LinkedIn thumbnail.

## On screen
The held title runs from the first frame to the call to action: DON'T START WITH / THE AI AGENT. Captions highlight
the keywords. Learn screenshots (MicrosoftDocs/fabric-docs, CC BY 4.0) are in
`~/persa-shorts/rc3-v2/assets/shots/`, and the built example is `docs/reels/demo/rc3-v2.json`.
| line | picture | card |
|---|---|---|
| 1 | your face, close; the held title | — |
| 2 | framework.png: the IQ framework, "Empower AI Agents" boxed ([iq/overview](https://learn.microsoft.com/en-us/fabric/iq/overview)) | — |
| 3 | layers.png: ontology and semantic models boxed (same page) | — |
| 4 | your face | PATIENTS · 412 · 522 · 946 (on "three") |
| 5 | your face; ORDER as the display word | — |
| 6 | your face | #1 ONE DEFINITION |
| 7 | ontology-map.png ([iq/ontology/tutorial-0-introduction](https://learn.microsoft.com/en-us/fabric/iq/ontology/tutorial-0-introduction)) | #2 ONTOLOGY |
| 8 | admin-preview.png: "Users can create Ontology (preview) items" ([iq/ontology/overview-tenant-settings](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview-tenant-settings)) | — |
| 9 | agent-chat.png: a data agent answering a question ([iq/ontology/how-to-create-data-agent](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-create-data-agent)) | #3 THEN THE AGENT |
| 10 | your face; FIRST as the display word | — |
| 11 | COMMENT "IQ" + arrow | — |
Filming notes (from `formats.md`):
- Sit close to the camera.
- Start on the first word, with no greeting.
- Talk at about 3 words a second.
- On line 4, hold up three fingers.

Ontology is in preview, so Microsoft's screenshot permission doesn't cover your own screen of it. Keep these Learn
shots (`systems/3-editor/BROLL.md`).

## The free thing
DELIVERABLE.md in this folder: Fabric IQ on one page, plus the definitions-first checklist for a health system.

## LinkedIn post
Don't give your hospital an AI agent before you fix this.

Fabric IQ puts data agents on top of your data: virtual analysts you ask in plain English. They answer from your
semantic models and your ontology.
So if "patient" means three things in your models, you get three answers.

The order that works:
1. One definition per word, in the semantic model
2. Build the ontology from that model (still in preview: test on synthetic data)
3. Then the agent, one domain, tested on questions you already know the answers to

Meaning first. Agents second.

Comment IQ and I'll send you the one-page map of Fabric IQ.
#MicrosoftFabric #PowerBI

Screens: Microsoft Learn, CC BY 4.0 (cropped, highlighted)
