# Brand pillars — what this channel is known for

Five themes, every video belongs to one. Enough range to have a personality, narrow enough that a health-system data
leader who sees three videos knows exactly what you do. Each pillar is tied to what you sell (`fabric-field-guide.md`),
the 52-week calendar (`calendar/`), and the pain people actually report (`research/`, `icp.md`).

| # | Pillar | The promise in one line | Calendar weeks |
|---|---|---|---|
| P1 | **Trusted numbers** | Why your counts disagree, and how to make every metric mean one thing | 5, 6, 9, 13–16, 19, 20, 26, 39–43 |
| P2 | **Fresh, fast, reliable reporting** | Dashboards that are on time, load fast and don't need manual fixes | 1, 7, 8, 18, 22, 23, 25, 46 |
| P3 | **What Fabric really costs — and when it's the right call** | Capacity, licences, hidden costs and platform choices, without surprises | 10, 24, 48–50 |
| P4 | **Governed access to health data** | Who can see which patient data, proven with tests, not promised | 11, 21, 44, 47 |
| P5 | **Healthcare data standards on Fabric** | FHIR, OMOP, DICOM and research cohorts, built so they can be checked | 2–4, 17, 27–38, 45 |
| — | Trend weeks (12, 51) and the clinic (52) | Take the pillar of whatever changed or whatever the audience brings | 12, 51, 52 |

## Why these five (evidence)
- **P3 is the loudest pain in the Fabric community.** In the community research (`research/fabric-community-research.xlsx`,
  96 counted requests, snapshot Oct 21 2026) "capacity, cost and monitoring" is the top topic at 22 of 96 (23%). Your guide's
  "Buying and sizing" and "hidden costs" sections are built for exactly this.
- **P2 maps to the next cluster:** CI/CD and deployment (12), ingestion and orchestration (12), reliability (4). It is also
  your promise word for word: faster loads, fewer manual fixes.
- **P4:** security and governance is 11 of 96. The healthcare-specific example is a team that cannot assemble access
  evidence to answer "who accessed which patient information" for a HIPAA audit (r/MicrosoftFabric, ~Sep 2026).
- **P1:** the healthcare requests in the sample are mostly counting problems — distinct patients across visits, diagnoses
  and care sites; a migrated clinical report that filters care locations wrongly.
- **P5:** the calendar's whole third quarter. Note: research and life-sciences topics reach research-informatics teams
  more than the health-system reporting leaders you sell to — keep the weekly offer video on P1–P4 during that quarter.

These counts describe a purposive sample, not the market (the spreadsheet says so itself). Treat them as direction, and
let your own comments and DMs re-rank the pillars after weeks 4, 8 and 13.

## Each pillar in three funnel shapes
The same topic, said three ways (see `SKILL.md → The funnel`):

| Pillar | Reach — "how to" (new people) | Authority — "how I did it" (trust) | Offer — "how I can do it for you" (buyers) |
|---|---|---|---|
| P1 | 3 reasons two dashboards show different patient counts | The reconciliation test I run before I trust a census number | What a one-week numbers audit looks like |
| P2 | Your pipeline is green — why is the dashboard stale? | How I traced a missed overnight load to the report it broke | Cutting manual report fixes: what we change first |
| P3 | The F64 line: when Power BI viewers stop needing Pro | How I size capacity for an overnight load and a morning peak | A Fabric cost review before your first invoice |
| P4 | 4 people who should NOT see the same report | The access test matrix I build before anything goes live | An access test run on your current reports |
| P5 | FHIR vs OMOP in 40 seconds | Following one synthetic patient from FHIR to OMOP | Standing up healthcare data solutions without guessing |

The offer column is a placeholder until you tell me what you actually sell, in what format and at what price — Step 0
asks. Never promise an outcome you haven't delivered; never name a client without written permission.

## Occasional, not a pillar: behind the work
One video in ten can be you: why you left the old way of building reports, a mistake you made, what a Tuesday looks like.
It makes the other four memorable. Draw it from `story-bank.md`.
