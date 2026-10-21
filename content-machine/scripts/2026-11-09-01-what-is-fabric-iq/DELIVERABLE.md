# Fabric IQ on one page

Checked on Microsoft Learn on 21 Oct 2026 ([What is Fabric IQ?](https://learn.microsoft.com/en-us/fabric/iq/overview),
updated 2026-07-08). Fabric changes monthly, so open the linked pages before you decide anything.

## What it is
Fabric IQ gives people and AI agents the meaning of your data, not just the tables. It is Microsoft's "context on
business entities and data". It is part of Microsoft IQ, alongside Work IQ, Foundry IQ and Web IQ. In Fabric it is a
workload that Microsoft marks **(preview)**.

## Three layers, two core items
| Layer | What it is | Core item |
|---|---|---|
| Operational intelligence | A shared, machine-readable description of your business: entity types, properties, relationships, rules and metrics, bound to live data | **Ontology (preview)** |
| Business intelligence | Curated analytics: measures, hierarchies, dimensions | **Power BI semantic model** |
| Unified data | One governed copy of your data, across clouds and on-premises (shortcuts, mirroring, the OneLake catalog) | OneLake, the foundation (not an item in the workload) |

You can generate an ontology from a semantic model that is already in production. The model's calculated columns and
DAX measures come across as metrics.

## The other items in the IQ workload
| Item | What it does | Use it when |
|---|---|---|
| Data agent | A "virtual analyst" that answers plain-language questions for one domain, grounded in semantic models and ontologies. It can be published to Microsoft 365, Foundry, Copilot Studio and custom apps | People need answers without building a report |
| Operations agent | Watches real-time data, spots anomalies and recommends or triggers governed actions | Something live needs watching (Real-Time Intelligence) |
| Planning | Planning, forecasting and reporting on the same data, with no code; it reads your semantic models for plan versus actuals | Budgets and forecasts live in spreadsheets today |
| Graph (preview) | Stores and queries connected data: nodes, edges, traversals, shortest paths | The question is "what is connected to what" (impact chains, dependencies) |
Preview status: ontology, Graph and the IQ workload are marked preview on the overview page. For the other items,
check each one's own page before you rely on it.

## How they fit
Semantic models hold the trusted numbers. The ontology names what those numbers mean, so reports and agents use the
same words. Graph follows the connections. Planning turns the numbers into a plan. Agents answer questions on top of
all of it.

## Definitions first: a checklist for a health system
These steps are our advice, not Microsoft's. Use synthetic data for every test.
1. **List the five words every report uses.** For example: patient, visit or encounter, admission, provider, location.
2. **Count each one in every model that has it.** In our synthetic month, "patients" came out three ways: 412 distinct
   patients, 522 visit rows, and 946 rows after joining diagnoses. An agent asked "how many patients?" will pick one.
3. **Agree on one definition with one owner** for each word, and write it into the semantic model as a measure with a
   description.
4. **Then generate the ontology from that model**, so the agent inherits the agreed definition rather than guessing.
5. **Then add one data agent for one domain.** Test it with questions whose answers you already know, before anyone
   else uses it.
6. **Keep patient data out of preview items** until your security and compliance teams have signed off.

## Sources
- What is Fabric IQ? https://learn.microsoft.com/en-us/fabric/iq/overview
- What is ontology (preview)? https://learn.microsoft.com/en-us/fabric/iq/ontology/overview
- Fabric data agent concepts: https://learn.microsoft.com/en-us/fabric/data-science/concept-data-agent
- What is planning in Fabric? (linked from the overview)
- Graph in Microsoft Fabric overview (preview), linked from the overview
- The synthetic month: `docs/reels/demo/synthetic_month.py` in this repository
