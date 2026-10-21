# LinkedIn video plan — the 52-week calendar as short vertical videos

The calendar (`hls-fabric-52-week-calendar.md`) is the WHAT; this file is how each week becomes 9:16 videos on LinkedIn,
powered by the LinkedIn strategy (pillars, funnel, story bank, swipe file). System 1 reads this file every week.

## Every week = 3 short vertical videos (starting point — re-rank after weeks 4, 8 and 13)
| Video | Funnel job | Shape | Length | CTA |
|---|---|---|---|---|
| **A · Reach** | new people find you | the week's lesson as a how-to, a mistake, a myth, or "what changed" (trend weeks) | 30–40 s | comment the week's keyword → the week's freebie |
| **B · Authority** | the people who found you start trusting you | "how I did it": the lab / test / teardown on synthetic data, or a story from `story-bank.md` | 40–60 s | comment the keyword, or a question that invites their version |
| **C · Offer** | buyers see what working with you looks like | the problem → what you do about it → proof (a story or a lab result) → the next step | 30–45 s | the offer CTA from `profile.md` (e.g. "DM me AUDIT") — no freebie |

- Record all three in one sitting. Video A and B can come from the same anchor tutorial the calendar already plans.
- **Offer pillar:** the week's pillar if it is P1–P4. In P5 and trend weeks the offer rotates P1 → P2 → P3 → P4, because
  your buyers are health-system reporting leaders, not research teams.
- **The freebie** is the week's "practical resource" from the calendar. System 2 drafts it as `DELIVERABLE.md` with the
  script; you check it before anyone gets it. It must be real, synthetic-data only, and true on the day it's sent.
- **Trend weeks (T):** pick a verified change 7–14 days before (the calendar's own rule); no relevant change → a current-
  state retest instead. Template: what changed → who it affects → prerequisites → the test → limits → adopt, wait or ignore.
- **Production standards from the calendar apply to every video:** synthetic or approved data only, verify current
  capabilities, disclose test conditions, no compliance or clinical claims, explicit metric definitions.

## Measuring (from the calendar, adapted to LinkedIn)
After weeks 4, 8 and 13, compare video A vs B vs C on: impressions and views (discovery), comments that ask a real
question (learning), and keyword comments, DMs and calls booked (qualified interest). Count one person once. Log the
exact questions people ask in `audience-questions.md` — they are next quarter's best topics.

## The 52 weeks
Type: E evergreen · T trend · A applied lab/clinic. Pillars in `pillars.md`.

| Wk | Week of | Topic | Type | Pillar | Freebie (comment keyword → this) |
|---|---|---|---|---|---|
| 1 | 2026-10-26 | Healthcare Fabric architecture: from source systems to a trusted dashboard | E | P2 | Architecture worksheet |
| 2 | 2026-11-02 | FHIR for analytics: Patient, Encounter, Observation, and the joins that matter | E | P5 | Resource relationship diagram |
| 3 | 2026-11-09 | Ingest synthetic FHIR data into Fabric and verify every stage | E | P5 | Ingestion validation checklist |
| 4 | 2026-11-16 | Healthcare data solutions: what is available now, and what must you build? | T | P5 | Capability and prerequisite matrix |
| 5 | 2026-11-23 | Why patient and encounter counts disagree across dashboards | E | P1 | Reconciliation tests |
| 6 | 2026-11-30 | Build a synthetic patient-access dashboard with explicit metric definitions | A | P1 | Synthetic appointments lab |
| 7 | 2026-12-07 | Your healthcare pipeline is green—why is yesterday’s dashboard stale? | E | P2 | Freshness runbook |
| 8 | 2026-12-14 | Test the latest monitoring change against a missed healthcare data load | T | P2 | Before-and-after test |
| 9 | 2026-12-21 | Patient identity: source identifiers, duplicate records, and linkage uncertainty | E | P1 | Identity mapping worksheet |
| 10 | 2026-12-28 | Size Fabric for an overnight clinical load and a morning reporting peak | E | P3 | Capacity benchmark worksheet |
| 11 | 2027-01-04 | Design an access test matrix before publishing healthcare analytics | E | P4 | Access test matrix |
| 12 | 2027-01-11 | Three current Fabric changes worth testing for a healthcare data team | T | trend/any | HLS release scorecard |
| 13 | 2027-01-18 | Debug a synthetic hospital dashboard: stale data or a broken denominator? | A | P1 | Incident postmortem |
| 14 | 2027-01-25 | Appointment access metrics: request date, booking date, and visit date | E | P1 | Metric glossary and test cases |
| 15 | 2027-02-01 | Claims, encounters, charges, and payments are different data objects | E | P1 | Revenue cycle relationship map |
| 16 | 2027-02-08 | Late-arriving claims: why last month’s numbers keep changing | E | P1 | Snapshot lab |
| 17 | 2027-02-15 | A new interoperability or Fabric ingestion change: test the real impact | T | P5 | Change assessment |
| 18 | 2027-02-22 | Build an incremental load that handles corrections without double counting | E | P2 | Incremental load test harness |
| 19 | 2027-03-01 | Build a synthetic denial-analysis dashboard without claiming dollars recovered | A | P1 | Synthetic denial dataset and definitions |
| 20 | 2027-03-08 | Prior authorization analytics: define timestamps before calculating turnaround | E | P1 | Timestamp dictionary |
| 21 | 2027-03-15 | Do current Fabric security capabilities pass our HLS access tests? | T | P4 | Role and engine test results |
| 22 | 2027-03-22 | Dev to test to prod without pointing a healthcare report at the wrong data | E | P2 | Deployment preflight checklist |
| 23 | 2027-03-29 | Trace a failed source feed to the dashboards it affects | E | P2 | Dependency map |
| 24 | 2027-04-05 | Cost a healthcare analytics workload without hiding the assumptions | E | P3 | Cost worksheet |
| 25 | 2027-04-12 | Which current Fabric features reduce manual healthcare reporting work? | T | P2 | Workflow comparison |
| 26 | 2027-04-19 | Reconcile synthetic claims and encounters: explain the unmatched records | A | P1 | Reconciliation lab |
| 27 | 2027-04-26 | FHIR vs OMOP: different jobs, not competing labels | E | P5 | Research architecture decision sheet |
| 28 | 2027-05-03 | Follow a synthetic patient record from FHIR to OMOP | E | P5 | Source-to-target mapping notebook |
| 29 | 2027-05-10 | Unmapped codes: why an OMOP table can look complete but be analytically wrong | E | P5 | Vocabulary coverage report |
| 30 | 2027-05-17 | Retest current OMOP transformation support against our mapping cases | T | P5 | Mapping regression sheet |
| 31 | 2027-05-24 | Define a reproducible research cohort with inclusion and exclusion rules | E | P5 | Cohort specification |
| 32 | 2027-05-31 | Build a synthetic research-feasibility dashboard—not a recruitment recommendation | A | P5 | Synthetic feasibility lab |
| 33 | 2027-06-07 | Observation windows, follow-up, and missing history in longitudinal analytics | E | P5 | Observation-window examples |
| 34 | 2027-06-14 | Does a new Fabric feature improve cohort reproducibility? | T | P5 | Cohort regression test |
| 35 | 2027-06-21 | Trace a cohort count back to the source records and transformation version | E | P5 | Lineage manifest |
| 36 | 2027-06-28 | Combine synthetic site, milestone, and enrollment data for an operations dashboard | E | P5 | Site operations data contract |
| 37 | 2027-07-05 | DICOM metadata in Fabric: what it can show without interpreting an image | E | P5 | Imaging metadata glossary |
| 38 | 2027-07-12 | Test the current DICOM pipeline with a synthetic imaging study | T | P5 | DICOM test checklist |
| 39 | 2027-07-19 | Why did the cohort count change after yesterday’s refresh? | A | P1 | Cohort investigation |
| 40 | 2027-07-26 | Before healthcare AI, define the data, access boundaries, and expected answers | E | P1 | AI readiness scorecard |
| 41 | 2027-08-02 | Define an encounter, readmission, and active patient before asking AI | E | P1 | Metric glossary |
| 42 | 2027-08-09 | Build a nonclinical healthcare analytics assistant with a fixed test set | E | P1 | Evaluation cases and failure taxonomy |
| 43 | 2027-08-16 | Newest Fabric AI capability: test healthcare analytics answers, not a sales demo | T | P1 | Availability and evaluation matrix |
| 44 | 2027-08-23 | Synthetic data, de-identified data, and identifiable data: do not treat them alike | E | P4 | Data-handling decision worksheet |
| 45 | 2027-08-30 | Build a research-data assistant that cites cohort definitions and declines clinical advice | A | P5 | Research knowledge lab |
| 46 | 2027-09-06 | Turn a failed healthcare pipeline into an incident summary—with human review | E | P2 | Incident assistant rubric |
| 47 | 2027-09-13 | What changed in AI access enforcement? Retest denied-access scenarios | T | P4 | Access regression checklist |
| 48 | 2027-09-20 | Production readiness for healthcare analytics: reliability, access, lineage, recovery | E | P3 | Production readiness checklist |
| 49 | 2027-09-27 | Fabric or Databricks for this HLS workload? Compare requirements, not logos | E | P3 | Workload decision matrix |
| 50 | 2027-10-04 | Explain an HLS data-platform investment without inventing clinical ROI | E | P3 | Business-case worksheet |
| 51 | 2027-10-11 | Healthcare Fabric year in review: what improved, what remains difficult? | T | trend/any | Annual evidence tracker |
| 52 | 2027-10-18 | Audience HLS clinic: rebuild one synthetic or approved workflow end to end | A | trend/any | Capstone implementation package |
