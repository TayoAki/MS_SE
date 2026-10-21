# Hook bank

Hooks written to `.claude/skills/content-machine/systems/2-script/HOOKS.md`: a specific problem, a moment the viewer
recognises, a consequence — problem before product. Score = the six HOOKS.md checks. "Numbers from" says where any number
must come from before recording: **fact** (sourced), **story** (`story-bank.md`), **demo** (the synthetic dataset shown in
the same video — replace `[n]` with what the demo actually produces). Scene hooks are scenarios, not claims that it
happened to a named client.

## Before → after: week 4 (the example hooks were weak)
| Before | Why it was weak | Score |
|---|---|---|
| "If your health system uses healthcare data solutions in Microsoft Fabric, put this date on the wall: December 31st, 2027." | conditional opener; 8-word product name first; a date 14 months away with no consequence | 2/6 |
| "Don't start a healthcare data solutions project the way the docs showed you last year." | vague — which way? what goes wrong? | 2/6 |
| "Microsoft handed its healthcare solution for Fabric back to customers, as source code." | news, no stakes for the viewer | 3/6 |

| After | On screen | Shape | Score | Numbers from |
|---|---|---|---|---|
| "New healthcare projects on Fabric start from source code now. Your team maintains it." | SINCE OCT 1: YOU MAINTAIN IT | dated change → consequence | 6/6 | fact (Microsoft Learn: new customers use the downloadable package since 2026-10-01) |
| "The cohort builder your analysts tested in Fabric? Switched off since November 2025." | COHORT BUILDER: DISCONTINUED | silent loss | 6/6 | fact (Microsoft Learn) |
| "After December 2027, who runs your healthcare pipelines? Microsoft won't." | AFTER 2027: WHO RUNS IT? | the question you can't answer | 5/6 | fact (Microsoft Learn) |

## The next 8 weeks (HLS calendar)
### W1 · Oct 26 · Source systems to a trusted dashboard (P2)
Specific problem: a dashboard number is wrong and nobody knows which handoff broke or who owns it.
Evidence: LifeBridge CIO on "data hygiene at the point of capture" (icp.md); the hospital-analytics-in-Excel thread (R-1g90g5t).
| Hook | On screen | Shape | Score | Numbers from |
|---|---|---|---|---|
| "The census dashboard is wrong. Who gets the 7 a.m. call?" | WHO GETS THE CALL? | scene | 6/6 | — |
| "Five handoffs sit between the EHR and your dashboard. The wrong number started at one." | 5 HANDOFFS · 1 WRONG NUMBER | the silent loss | 5/6 | demo (the architecture map) |
| "Stop fixing the dashboard. The number broke three steps earlier." | IT BROKE 3 STEPS EARLIER | stop doing X | 5/6 | demo |

### W2 · Nov 2 · FHIR for analytics: the joins that matter (P5)
Specific problem: in FHIR R4 `Observation.encounter` is optional (cardinality 0..1, hl7.org — verified 2026-10-21), so an
inner join from lab results to visits drops results with no error.
| Hook | On screen | Shape | Score | Numbers from |
|---|---|---|---|---|
| "Inner-join FHIR lab results to visits and some of them vanish. No error." | LAB RESULTS: GONE | silent loss | 6/6 | fact (FHIR spec) |
| "Every lab result belongs to a visit. In FHIR, it doesn't have to." | NOT EVERY LAB HAS A VISIT | the line people believe | 6/6 | fact (FHIR spec) |
| "Same patients, same month: [n] lab results in one query, [m] in the other." | [n] vs [m] | two numbers | 6/6 | demo |

### W3 · Nov 9 · Ingest synthetic FHIR, verify every stage (P5)
Specific problem: the load reports success while records drop between layers.
| Hook | On screen | Shape | Score | Numbers from |
|---|---|---|---|---|
| "The load succeeded. Silver has [n] fewer patients than bronze." | SUCCESS · [n] MISSING | succeeded, still wrong | 6/6 | demo |
| "Quality asks why [x]% of encounters are missing. Your pipeline never failed." | NEVER FAILED · [x]% MISSING | scene | 6/6 | demo |
| "Prove every record you loaded reached the report. Most pipelines can't." | PROVE IT REACHED THE REPORT | the question you can't answer | 5/6 | — |

### W4 · Nov 16 · Healthcare data solutions: available now vs build (P5, trend)
See "Before → after" above. Re-verify on Microsoft Learn 7–14 days before recording.

### W5 · Nov 23 · Why patient and encounter counts disagree (P1)
Specific problem: distinct patients counted across visits, diagnoses and care sites (Fabric Community, 2025-04-04,
F-4638608); the gap analysis's healthcare pilot ("why patient counts and visit counts disagree").
| Hook | On screen | Shape | Score | Numbers from |
|---|---|---|---|---|
| "Your census says [n] patients. The visit report says [m]. Both are right." | [n] vs [m] · BOTH RIGHT | two numbers | 6/6 | demo |
| "The CFO asks how many patients you saw last month. You have three answers." | 3 ANSWERS · 1 QUESTION | scene | 6/6 | demo |
| "Stop counting patients in the visits table. Every readmission counts them twice." | STOP COUNTING HERE | stop doing X | 6/6 | — (true by construction; show it in the demo) |

### W6 · Nov 30 · Patient-access dashboard with explicit definitions (P1)
Specific problem: "wait time" depends on which timestamp you start from — request, booking or visit (calendar W14).
| Hook | On screen | Shape | Score | Numbers from |
|---|---|---|---|---|
| "'Average wait time' can mean three different numbers. Which one is on your dashboard?" | WAIT TIME = ? | the question you can't answer | 6/6 | — |
| "Two managers bring 'days to appointment' to the same meeting. Same data. Different numbers." | SAME DATA · 2 ANSWERS | scene | 6/6 | demo |
| "Start the clock at booking and your access numbers look better than they are." | THE CLOCK STARTS TOO LATE | the line people believe | 5/6 | — |

### W7 · Dec 7 · The pipeline is green — why is the dashboard stale? (P2)
Specific problem: "Refresh Succeeds but Does Not Pick Up Latest Data" (Fabric Community thread title).
| Hook | On screen | Shape | Score | Numbers from |
|---|---|---|---|---|
| "The pipeline is green. The dashboard still shows yesterday." | GREEN · BUT YESTERDAY | succeeded, still wrong | 6/6 | — |
| "7:40 a.m. Bed meeting at 8. Every job says success. The numbers are from yesterday." | EVERY JOB: SUCCESS | scene | 6/6 | — |
| "Every job succeeded. So why is the ED dashboard [n] hours old?" | [n] HOURS OLD | two numbers | 6/6 | demo or story |

### W8 · Dec 14 · Test the latest monitoring change against a missed load (P2, trend)
Template until the change is chosen: "[the change] says it catches [the missed load]. We broke a load on purpose to see."
· on screen WE BROKE IT ON PURPOSE · shape: the test · numbers from: demo.

## Evergreen hooks (from the gap analysis's healthcare themes and the ICP)
| Hook | On screen | Pillar | Evidence | Numbers from |
|---|---|---|---|---|
| "One patient, two visits, three diagnoses. Your measure counted [n]." | 1 PATIENT · COUNTED [n] | P1 | gap W13 · F-4638608 | demo |
| "An auditor asks who opened this patient's data in your report. Can you show them?" | WHO OPENED THIS? | P4 | gap W29 · R-1wojllh | — |
| "You moved the clinic report to Power BI. Now the location filter shows every clinic." | EVERY CLINIC. AGAIN. | P1 | gap W30 · F-4271215 | demo |
| "This Power Query step lives in [n] workbooks. Change it once, fix it [n] times." | FIX IT [n] TIMES | P2 | gap W50 · R-1g90g5t | story or demo |
| "Nobody built anything new. Capacity still hit 100% at 9 a.m." | 100% AT 9 A.M. | P3 | community top topic: capacity/cost (22 of 96) | story or demo |
| "Below F64, every report viewer needs a Pro licence. At F64, they don't." | F32 vs F64 | P3 | Microsoft Learn licences page | fact |
| "'Fabric is HIPAA compliant' doesn't mean your workspace is." | COMPLIANT ≠ CONFIGURED | P4 | BAA covers Microsoft's side (research, Reported) | fact (verify) |
| "One health system was producing more than 12,000 reports a month." | 12,000 REPORTS / MONTH | P2 | Chartis 2025-01-03 (CentraCare) | fact |
| "Your report opens for you. What can the night-shift manager see?" | WHAT CAN THEY SEE? | P4 | gap W05/W18 ("the report opens — what can that identity read?") | — |
| "An incremental load can succeed and still miss changed rows." | SUCCESS · ROWS MISSING | P2 | gap W03 | demo |
