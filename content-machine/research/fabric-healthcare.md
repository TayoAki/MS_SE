# Microsoft Fabric in US healthcare: research brief

Researched 2026-10-21. About 25 web searches plus direct page reads.

**Labels**
- **Verified**: I read the source page myself and the claim or quote comes from it.
- **Reported**: the claim comes from a search-result snippet, a secondary write-up, or a source I could not open in full. It is not checked word for word.
- **Inference**: my own reasoning from the evidence. It is not stated by any source.

Vendor and consultancy marketing is marked **[vendor]**.

**Access limits.** reddit.com, community.fabric.microsoft.com (Cloudflare), beckershospitalreview.com, fiercehealthcare.com and several job boards blocked automated fetching from this environment. As a result:
- Q4 has **no verbatim Reddit quotes**.
- Forum material in Q4 is paraphrased from search snippets and labelled Reported.
- Becker's and Fierce items are snippet-level only.

---

## 1. Healthcare data solutions (HDS) in Microsoft Fabric

### Delivery model change (Verified)

This is the single most important current fact. The banner appears on the HDS overview, get-started and release-notes pages, all last updated 2026-08-25. It reads:

> "Microsoft is evolving the delivery model for healthcare data solutions in Microsoft Fabric. Beginning August 3, 2026, a downloadable source code and documentation package is available for customers to create customer-managed implementations. Support for the current managed healthcare data solutions in Microsoft Fabric ends on December 31, 2027. Starting October 1, 2026, only existing customers can deploy the current managed solution by using the instructions in this documentation. New customers should use the downloadable package instead."

The package is at https://aka.ms/HLSFabric. Release notes list it under "August 2026 (release version 1.4.0)".

- **Inference:** HDS is moving from a Microsoft-managed SaaS item to a source-code accelerator the customer owns. That has three effects:
  - New health systems (any after 2026-10-01) must stand it up and maintain it themselves, or with a partner.
  - Existing customers face a migration deadline of 2027-12-31.
  - Both are openings for implementation and run services.

### Capabilities listed today, and their status

The list comes from the overview page (ms.date 2025-11-24, updated_at 2026-08-25). Status comes from the What's new and release-notes pages.

| Capability | What it does (per Learn) | Status as of latest docs | Label |
|---|---|---|---|
| Healthcare data foundations | FHIR-based medallion lakehouses with "ready-to-run data pipelines"; ingests FHIR NDJSON into bronze, then flattens to silver | GA (whole HDS went GA in Nov 2024); required first for every other capability | Verified |
| OMOP transformations | Prepare data for OMOP CDM analytics | GA. OMOP vocabulary integration added May 2025; custom OMOP mappings added Mar 2025 | Verified |
| DICOM data transformation | Bring DICOM imaging to OneLake | Preview July 2024; now listed without a preview label. Inventory-based ingestion added Jan 2025 ("usually over 50 million files"); Patch/Delete support Oct 2025 | Verified |
| Azure Health Data Services – Data export | Bring FHIR data from the AHDS FHIR service to OneLake | Listed without a preview label | Verified |
| CMS claims data transformations (CCLF) | Ingest Medicare CCLF claims | GA March 2025 | Verified |
| SDOH datasets – Transformations | Geography-level SDOH (CSV/XLSX/XLS) | GA March 2025 | Verified |
| DAX Copilot data transformation | Ingest Dragon Ambient eXperience (DAX) Copilot data for analytics and Power BI | GA October 2025 per What's new and release notes v1.3.1. **The overview page still labels it "(preview)", so the docs are inconsistent** | Verified |
| DAX Copilot integration with Fabric (raw artifacts) | Transcripts, audio and AI summaries in a lakehouse | GA March 2025 | Verified |
| DAX Copilot data insights | OpenAI prompts to extract SDOH and sentiment from transcripts | Preview (March 2025) | Verified |
| Dynamics 365 Customer Insights – Data preparation | Patient or member lists for outreach | Listed without a preview label | Verified |
| Care management analytics | High-risk and rising-risk patient insights; gold data model | GA March 2025 | Verified |
| Patient outreach analytics | Dynamics 365 marketing data plus FHIR data, with Power BI templates | GA March 2025 | Verified |
| Orchestrate multimodal AI insights | Generate and integrate AI enrichments | Public preview (March 2025); still preview | Verified |
| Discover and build cohorts | Natural-language cohort builder (formerly "Healthcare data explorer") | **Discontinued, effective November 2025.** Still listed on the overview page | Verified |
| Unstructured clinical notes enrichment | Text Analytics for health on clinical notes | **Discontinued, effective November 2025.** Still listed on the overview page | Verified |

**Earlier retirements.** Patient insight cards, Healthcare database templates, the Patient population dashboard (preview) and the Healthcare data pipeline template were all retired on 2025-01-30. Purview healthcare application templates were retired in May 2025. **Verified** (What's new).

**Timeline**
- Preview announced 2023-10-10.
- Public preview in March 2024.
- GA in November 2024.
- **Verified:** Microsoft Official Blog 2023-10-10, Fabric blog 2024-03-11, What's new.

### Prerequisites (Verified, get-started page, ms.date 2025-11-24)

- "A tenant with Microsoft Fabric enabled".
- "A Microsoft Fabric paid license", or the Fabric trial.
- "Administrator permissions to create a new workspace and artifacts in Power BI".
- Copilot features in cohorts needed "a paid Fabric SKU (F64 or higher, or P1 or higher)". That capability is now discontinued.
- The Azure Marketplace offer needs an Azure subscription and rights to create resource groups and Marketplace resources.

From the deploy page (ms.date 2025-09-10):
- The HDS environment pins "Runtime 1.2 (Apache Spark 3.4 and Delta Lake 2.4)".
- The sample FHIR dataset is 32.68 GB.

### Pricing and licensing (Verified unless marked)

- The docs show no separate HDS price. It "require[s] appropriate Microsoft Fabric licenses and capacities", and the Marketplace offer "is dependent on the Azure services deployed with the offer" (get-started).
  - **Inference:** cost is Fabric capacity (CU) consumption, plus any Azure services such as AHDS FHIR or AI Language, plus Dynamics 365 licences for the outreach features.
- Fabric F SKUs are billed by Azure "per second with no commitment, with the option of a yearly capacity reservation". (Fabric licences page, ms.date 2026-06-15, updated 2026-08-05.)
- **F64 matters to health systems with many report consumers.** "On F SKUs smaller than F64, each user viewing Power BI content must have Pro, PPU, or an individual trial. On F64 or larger, users with only a Free license and a viewer role can view Power BI content."
- Microsoft is "retiring the Power BI Premium per-capacity SKUs" and steering customers to F SKUs.
- **Compliance.** The HDS compliance page (ms.date 2025-03-31) says HDS is "HIPAA and HITRUST compliant". Its table shows "HIPAA BAA: Yes". It links to the Fabric HIPAA and HITRUST announcements.

---

## 2. Epic data into Fabric and Power BI

### Documented by Microsoft (Verified)

**Fabric mirroring for SQL Server.** Learn page ms.date 2025-11-05, updated 2026-07-06.
- Supports SQL Server 2016–2022 using CDC. Supports SQL Server 2025 using the "change feed", which requires Azure Arc.
- Works on-premises behind a firewall via the on-premises or VNet data gateway.
- Pricing: "Fabric compute used to replicate your data into Fabric OneLake is free. Storage in OneLake is free of cost based the capacity size." Query compute is charged.
- Warning: "Long-running transactions might result in the transaction log filling up more than usual."
- The page does **not** mention Epic, Clarity or Caboodle.
- A Fabric Updates blog post titled "Mirroring for SQL Server in Microsoft Fabric (Generally Available)" exists. **Reported.** I could not open it, so the date is unconfirmed.

**HDS has no Epic-specific connector.** Clinical data enters as FHIR NDJSON files or through the AHDS FHIR service export (deploy and overview pages).
- **Inference:** an Epic customer would feed HDS via a FHIR bulk export or an AHDS FHIR service. Most Clarity/Caboodle reporting would instead come through mirroring, pipelines or copy jobs. HDS is FHIR-centric, not Clarity-centric.

**Open question (Inference).** Clarity is usually hosted on SQL Server, sometimes Oracle; confirm per customer. I found **no source** confirming Epic permits enabling CDC on Clarity or Caboodle for Fabric mirroring. This is a practical blocker to check with each customer's Epic and DBA teams. It also makes good content.

### Named customer evidence of Epic + Fabric (Verified)

- **Virtua Health** (Microsoft story; date shown "4/07/2026"). Its goal was "To enable seamless integration between its EPIC EHR system, Microsoft Fabric, Power BI and Copilot…". It integrates data "in a unified Microsoft Fabric data layer".
- **Peterborough Regional Health Centre** (Canada; story date "8/04/2026"). Names Epic as a clinical source. "18 production systems" landed in OneLake.
- **UNC Health** (2026-05-26). Its EASI output is formatted "for integration into Epic". The story does not say how Epic data is extracted.

### Epic's own cloud analytics (Cogito Cloud / Nebula): Reported, not confirmed on epic.com

**Hakkoda [vendor: Snowflake partner], 2023-09-20.**
- Says Epic announced at UGM in August 2023 that Cogito (Clarity, Caboodle and so on) would move to an "Azure-native lakehouse" "within the next two years".
- Quote: "The whole move hinges on Microsoft Data Fabric".
- Quote: "Moving hourly ingestion from Chronicles to Clarity is a game changer."

**EHC Consulting [vendor], 2025-05-23.**
- "Epic built their next-generation SaaS analytics platform, called Cogito Cloud (formerly Nebula), on Azure which leverages Microsoft Fabric".
- Customers on Azure have "a simpler strategy and architecture for feeding data into Cogito Cloud" and lower egress.

**Prominence Advisors [vendor], undated (© 2026).**
- "Cogito will become a part of the cloud-based Nebula."
- "This Microsoft Azure-native lakehouse will morph Clarity and Caboodle into medallion layers in a single lakehouse."

**RSM US [vendor: Microsoft partner], 2026-04-21, "Epic's shift to Fabric".**
- Quote: "Epic planning to release all new data models exclusively through the Cogito Cloud".
- Calls it "a significant structural shift, rather than a feature update".
- Says refreshes are moving "from daily batches toward near-real-time insight".
- Recommends enterprise analytics "live in a system-owned Fabric tenant".
- Quote: "Microsoft funding frequently offsets the costs of roadmap and proof-of-concept work."
- RSM also lists an "Epic for Fabric Implementation" consulting offer on Microsoft Marketplace. **Reported:** the listing exists per search, but the page returned 403.

**What I could not establish**
- How customers get access to Epic-hosted Cogito Cloud data in their own Fabric tenant: shortcuts, sharing or a copy.
- Pricing.
- General-availability dates.
- None of this was found on an Epic primary page, and Fierce's 2026 UGM coverage (snippet) did not mention it.
- **Treat "Epic's analytics run on Fabric" as strongly rumoured or partner-reported, not documented by Epic in what I could access.**

### Adjacent signal (Verified)

Microsoft (2026-03-19, **[vendor]**) says Franciscan Health, Jefferson Health and St. Luke's "have migrated Epic to Azure". It cites a Forrester TEI study of Epic on Azure: "162% return on investment in three years". The same post says, unattributed: "Companies saved $4 million on analytics alone by replacing legacy data analytics tools with Microsoft Fabric."

Duke Health (2026-07-28) runs Epic DR on Azure and is "modernizing its data infrastructure with Microsoft Fabric to support shared definitions…".

### Competitor path (Verified, Databricks blog, 2026-03-11)

At HIMSS26, Fivetran and Databricks demoed "automated data integration from Epic Clarity" into a Databricks lakehouse.

---

## 3. Named health systems and healthcare organisations using Fabric

US examples with substantive Fabric detail: **3** (Virtua, UNC Health, Duke Health). Two more are older or announcement-level (Northwestern Medicine, Arthur Health), and one is research-only (UW SMPH). Non-US examples with strong detail: 2 (Peterborough, Apollo). All the case studies are Microsoft-published **[vendor]**, so the figures are self-reported.

### 1. Virtua Health (NJ; 5 hospitals). Story dated "4/07/2026". Verified
- **Built:** a "unified Microsoft Fabric data layer" combining demographic, clinical and financial data. Power BI dashboards are embedded in Teams with Copilot summaries. A custom XGBoost sepsis model in Azure is "integrated into EPIC's clinical workflow".
- **Outcomes, quoted:**
  - "AI insights have improved sepsis identification by 80%."
  - "Heart failure follow-up rates have increased from 58 percent to 81 percent."
  - "cutting clinician review time to five minutes" (versus "half an hour for each patient").
  - "Compared to commercial models, Virtua Health's model reduces false positives by over 80 percent."
  - Infographic: "15,000 excess hospital days eliminated"; "Average patient stay reduced by 1 day."
- **People:** Tom Gordon (SVP and CIO); Ajit Shukla (AVP Advanced Analytics). Shukla: "We integrated Power BI with Teams, so the clinicians can look into their trends and insights."

### 2. UNC Health (NC). 2026-05-26. Verified
- **Built:** "standardized its entire data estate on Fabric". Centrally managed data models for community analysts. EASI document-abstraction framework feeding Epic. SHIRE secure research enclave on Azure (launched Nov 2025). Copilot in Fabric for pipeline and notebook work.
- **Outcomes, quoted:**
  - "reduced care gap chart review time by roughly 50%".
  - "abstraction detection accuracy improved from 83% to 93%".
  - "reviewed approximately 9,700 diabetic eye exam care gaps" and "nearly 180,000 additional care gaps".
  - SHIRE is "now supporting 25 active studies".
  - "It's no longer a ticketing queue with a 30-to-45-day response time."
- **Pain:** "couldn't keep pace with 40% annual data growth".
- **People:** Rachini Moosavi (Chief Analytics Officer): "If you want conversational analytics, your data needs to live in the cloud."

### 3. Duke Health (NC). 2026-07-28. Verified, but light on Fabric detail
- **Built:** "modernizing its data infrastructure with Microsoft Fabric to support shared definitions, governed data reuse, and better monitoring of predictive models".
- The headline numbers in the story are about Epic DR on Azure, not Fabric: "Failover target: 15 minutes"; "Expected to save multiple millions of dollars per year".
- Partner: Optimum Healthcare IT.

### 4. Northwestern Medicine (IL). 2023-10-10. Verified (announcement only)
- Microsoft's blog says Northwestern "will leverage the healthcare data solutions in Fabric to integrate clinical data across a variety of sources".
- Becker's (snippet; **Reported**) quotes CIO Doug King: a curated, consolidated data source is "critical" to real-time insights.
- **Caution (Verified):** Northwestern Medicine presented a "unified, governed data platform" session with **Databricks** at HIMSS26 (2026-03-11). Do not present it as a pure-Fabric shop.

### 5. Arthur Health (US). 2023-10-10. Verified (plan only)
- "plans to use Fabric to power predictive care stage models", with partner Quisitive.
- No outcomes published.

### 6. University of Wisconsin–Madison SMPH. 2024-03-11. Verified (exploring)
- "exploring" HDS for a Colorectal Cancer Multi-Modal Data Commons.
- Research use, not a health-system operations deployment.

### 7. Peterborough Regional Health Centre (Ontario, Canada; Epic site). Story dated "8/04/2026". Verified
- **Built:** "18 production systems" into OneLake, Purview governance, Copilot in Fabric and role-based dashboards.
- **Outcomes, quoted:**
  - "approximately $800,000 in recoverable funding".
  - "reduce unnecessary lab utilization by about 14% in a six-month timeframe".
  - Medication reconciliation "increased from 76% to more than 85%".
  - "wait time to inpatient beds decreased 43% from 56.8 hours to 32 hours".
  - "a roughly 70% reduction in ambulance offload times, from approximately 134 minutes to 40 minutes".
- **People:** Evan Lyons (EVP and CIO).

### 8. Apollo Hospitals (India; 75 hospitals). 2025-11-14. Verified
- **Built:** a migration from Azure Synapse and Analysis Services to a Fabric Warehouse, Eventhouse and Power BI.
- **Outcomes, quoted:**
  - "a 25% drop in manual work and a 60% increase in order conversions".
  - "Now data flows from source to Fabric in two seconds and it is 100% accurate."
  - "consolidated 230 terabytes of siloed data into a 30-terabyte compressed system".

### Other names (2023 announcement only; non-US; Verified mention)
SingHealth, and Ontario Workers Network / The Ottawa Hospital.

### Not found
I found no Fabric case studies, within budget, from Mayo, Cleveland Clinic, Providence, Advocate, Intermountain, Kaiser or HCA.

Becker's (snippet; Reported) listed Advocate Health and Duke Health as adopters of Microsoft's Oct 2023 tools. In that article Advocate's link was DAX Copilot via Atrium Health, not Fabric.

---

## 4. Practitioner pains (healthcare on Fabric and Power BI)

**Evidence caveat.** Reddit and the Fabric Community forum could not be fetched. Nothing below is a verbatim Reddit quote. Forum items are snippet-level paraphrases (Reported). The strongest "voice of customer" evidence I can verify comes from customer stories and Microsoft's own docs.

### A. Capacity cost and throttling
- **Reported** (Fabric Community thread "Capacity Throttling", https://community.fabric.microsoft.com/t5/Fabric-platform/Capacity-Throttling/m-p/4919534; undated in snippet). A user on **F16** running incremental-refresh pipelines plus paginated-report exports hit throttling above 100%. Replies suggested putting ETL on a separate capacity from end-user reporting, applying row filters to paginated reports, or scaling up.
  - Not healthcare-specific.
- **Verified:** the F64 viewer-licence threshold (Q1) forces a big jump in cost decision for health systems with thousands of report viewers.
- **Reported [vendor]:** EPC Group sizes a 10–30-hospital IDN at "F128 ($16,819/mo reserved) or F256". Treat these numbers as unverified consultant figures.

### B. PHI access control, auditing and BAA
- **Reported** (thread "Fabric Security Issues", https://community.fabric.microsoft.com/t5/Fabric-platform/Fabric-Security-Issues/m-p/4709679). The poster's workaround: separate ingestion and curated workspaces, read-only access via the SQL endpoint, and RLS/CLS in the curated layer. They noted there was **no platform-level way to enforce that separation**.
- **Reported** (Fabric Updates blog title): "Column-Level & Row-Level Security for Fabric Warehouse & SQL Endpoint" was announced. Preview or GA status at the time of reading is unconfirmed.
- **Reported (Microsoft Learn, via search snippet):**
  - Fabric Warehouse SQL audit logs are **off by default** and are **deleted along with the Warehouse**.
  - Microsoft's operation-list page says the Fabric audit log isn't a complete source for OneLake data-plane activity. OneLake diagnostics fills that gap.
  - **Inference:** "who looked at which patient's data" in Fabric is not on by default. It is a real HIPAA-audit content angle.
- **Reported:** a Microsoft Q&A answer (about M365, not Fabric) says the BAA "only covers Microsoft's responsibilities". The customer must still configure MFA, Conditional Access and audit logging.
  - **Inference:** the "Fabric is HIPAA-compliant, so we're compliant" misconception is a teachable point.
- **Verified:** UNC Health says sensitive EHR data previously sat "on password-protected network drives with limited controls against unauthorized movement". Dr. Emily Pfaff: "Achieving a balance between not so locked down that you can't do any work, but not so open that patients' data are at risk".

### C. Epic data volume, latency and refresh
- **Verified (RSM [vendor]):** "escalating cloud and licensing costs driven by duplicated data movement". Overnight Epic batch refresh is a key driver (snippet wording: "delayed insights tied to overnight Epic refresh cycles").
- **Verified:** UNC's "40% annual data growth" outgrew on-premises storage.
- **Verified (Microsoft Learn, mirroring):** CDC mirroring can grow the source transaction log during long transactions. This matters on a busy Clarity server.
- **Verified (Hakkoda [vendor], 2023):** worries about Fabric reliability ("has not yet been proven"), RBAC tuning, lock-in, and the future of Slicer Dicer once Caboodle moves to cloud.

### D. HDS-specific failures (Microsoft Learn troubleshooting; Reported via search summary, consistent with the Verified deploy page)
- New workspaces default to a newer Spark runtime. HDS needs Runtime 1.2, otherwise "data pipeline and notebook executions can fail".
- Deploy page (Verified): "Don't run more than one instance of this notebook at a time, because it can cause inconsistent results."
- SDOH: duplicate datasets are **silently skipped**, which can look like missing data.
- Fabric Spark library incompatibility (SciPy) caused pipeline failures. This was fixed in v1.4.0, August 2026 (Verified, release notes).
- Previewed capabilities were withdrawn (cohorts, notes enrichment) with instructions to delete artifacts.
  - **Inference:** buyers are wary of building on preview features.

### E. Migration (SSRS, Synapse, on-prem SQL)
- **Verified:** Apollo migrated from Azure Synapse SQL pool and Azure Analysis Services to Fabric.
- **Reported:** a 2024 Fabric Community thread asked whether to rebuild many legacy Power BI Report Server reports in dataflows. No outcome was given.
- **Reported (ProArch [vendor]):** the trade-off between lift-and-shift and redesign of semantic models; lift-and-shift "keeps technical debt".

### F. Patient counting and grain problems
**No source found** within budget. **Inference:** this is untested as a public pain point, which may make it a content gap. Validate it with the creator's own client experience before using it.

---

## 5. Buying signals

### Job postings mentioning Fabric at or for healthcare providers
These are thin and mostly aggregator or staffing listings. Verify on the employer's site.

1. **Ovation Healthcare** (shared services for "independent hospitals and health systems"). "MS Fabric Data Engineer", remote US. Removed 2026-09-30. Mentions "Lakehouse and Warehouse architectures", "OneLake", "Power BI semantic models built on Fabric data". https://www.builtinboston.com/job/ms-fabric-data-engineer/11192405. **Verified.**
2. **NYC Health + Hospitals.** "Senior Epic Data Engineer | Caboodle & Clarity Expert". Lists a Microsoft Fabric skill; USD 110,000–150,000. Date unknown. https://www.jobleads.com/us/job/senior-epic-data-engineer-caboodle-clarity-expert--new-york--ea0e9c510fe2bddec44fa831c17ad31a7. **Reported** (snippet; the page returned 403).
3. **Quoris** (staffing) for an unnamed healthcare organisation, Philadelphia. "Senior Healthcare Data Engineer", to support "migration and modernization of enterprise data workloads into Microsoft Azure and Microsoft Fabric". Clarity and Caboodle required; 6-month contract; open until 12/10/2026. https://bebee.com/us/jobs/senior-healthcare-data-engineer-epic-clarity-quoris-philadelphia-pa--t7xk-877543515. **Reported.**
4. **Duke Health (DHTS).** "Microsoft Fabric QA Analyst", Durham NC. Covers "quality assurance, validation, and release readiness of analytics-ready data assets in Microsoft Fabric". **Reported** (snippet only; no URL captured; date unknown).
5. **NC Health / Rex Healthcare (UNC Health subsidiary).** "Enterprise Analytics & Interop Developer III", appearing under a "microsoft fabric data engineer" listing. https://jobs.disabilitytalent.org/jobs/266422393-microsoft-fabric-data-engineer. **Reported.** The Fabric mention is unconfirmed (403).
6. **Xpress Wellness** (urgent care, Dallas). "Microsoft Fabric Data Engineer". **Reported** (snippet; no URL captured).

### Stronger trigger events than job ads
- **HDS managed-solution end of support, 2027-12-31.** New customers have been on the "downloadable package" since 2026-10-01 (**Verified**). Every existing HDS customer needs a transition plan. **Inference:** a time-boxed, named trigger.
- **Epic Cogito Cloud on Azure/Fabric** (Reported [vendor]), and "all new data models exclusively through the Cogito Cloud" (RSM, 2026-04-21). **Inference:** Epic customers will have to decide how their own Fabric tenant relates to Epic's.
- **Epic-on-Azure migrations:** Franciscan, Jefferson, St. Luke's (Microsoft, 2026-03-19), Duke Health (2026-07-28). **Verified.** Epic on Azure lowers egress to Cogito Cloud (EHC, Reported). **Inference:** a leading indicator of Fabric analytics work.
- **Power BI Premium P-SKU retirement** pushes P1 customers to F SKUs (**Verified**, licences page). **Inference:** a re-sizing and cost-review moment.
- **Microsoft-funded POCs** (RSM: "Microsoft funding frequently offsets the costs of roadmap and proof-of-concept work"). **Verified quote [vendor].** Partners use Microsoft funding programmes. Specific programme names were not found within budget.
- **Partner marketplace offers:** RSM "Epic for Fabric Implementation" on Microsoft Marketplace (**Reported**, listing 403). Many consultancies market Epic-to-Fabric services (Scient Solutions, Numlytics, EPC Group, Invene; **Reported [vendor]**). This is a competitive service field.

**RFPs:** none found within budget.

---

## 6. Competitive context

**Epic's own stack (Cogito, Caboodle, Cosmos)**
- If the consultant reports are correct, Epic's own cloud analytics is being built **on** Azure and Fabric (Reported [vendor]: EHC 2025-05-23; Hakkoda 2023-09-20; RSM 2026-04-21). That would make Fabric less a competitor to Epic analytics and more its substrate.
- **Inference:** the question for health systems becomes "what do we build in our own tenant beyond what Epic delivers?"
- Fierce Healthcare (snippet; Reported) covered UGM 2026 as AI-focused (agent platform, "Cosmos-powered predictions", "Ergo") with no Fabric mention found.

**Databricks**
- Most visible rival in Epic shops at HIMSS26 (**Verified**, Databricks blog 2026-03-11 [vendor]).
- Sessions with Intermountain Health (with R1 RCM), Northwestern Medicine, UK HealthCare (on **Azure** Databricks, with Prominence Advisors) and NYU Langone.
- A Fivetran demo of "automated data integration from Epic Clarity".
- Health Catalyst listed as a Databricks partner.
- **Reported:** Health Catalyst partnered with Databricks on AI toolkits (snippet, about a year old).

**Snowflake**
- **Reported:** KLAS "Snowflake in Healthcare 2023" (10 customers) found "Databricks Lakehouse Platform was the most commonly considered alternative to Snowflake, closely followed by Amazon Redshift and Microsoft Azure Synapse Analytics". The report predates Fabric.
- Hakkoda [Snowflake partner] argued in 2023 that Epic's Azure move raises "vendor lock-in" and interoperability concerns for non-Microsoft platforms.

**Interop rather than replacement**
- Microsoft positions OneLake as a shared foundation across Fabric, Azure Databricks and Snowflake (Reported, Microsoft OneLake write-up per snippet).
- Third-party comparisons (Reported [vendor/blog]) generally say: Fabric fits Microsoft-centric health systems (Entra, Power BI); Snowflake fits governed data sharing; Databricks fits ML and genomics.

**Health Catalyst**
- No credible direct Fabric-vs-Health Catalyst positioning found. It shows up as a Databricks partner.

**Google Cloud Healthcare API / AWS HealthLake**
- **Not researched within budget.** No claims made.

**KLAS 2026**
- No KLAS report on Fabric or health data platforms found. **Evidence on head-to-head positioning is thin. Most of it is vendor marketing.**

---

## Sources

Dates are publication or ms.date as shown. "undated" means none was found.

**Microsoft Learn and Microsoft first-party**
- HDS overview (ms.date 2025-11-24; updated 2026-08-25): https://learn.microsoft.com/en-us/industry/healthcare/healthcare-data-solutions/overview
- What's new in Microsoft for Healthcare (updated 2026-08-25): https://learn.microsoft.com/en-us/industry/healthcare/whats-new
- HDS get started (ms.date 2025-11-24; updated 2026-08-25): https://learn.microsoft.com/en-us/industry/healthcare/healthcare-data-solutions/get-started
- HDS deploy (ms.date 2025-09-10; updated 2026-08-25): https://learn.microsoft.com/en-us/industry/healthcare/healthcare-data-solutions/deploy
- HDS release notes (v1.4.0 Aug 2026; updated 2026-08-25): https://learn.microsoft.com/en-us/industry/healthcare/healthcare-data-solutions/release-notes
- HDS compliance (ms.date 2025-03-31): https://learn.microsoft.com/en-us/industry/healthcare/healthcare-data-solutions/compliance
- HDS troubleshoot (date not captured): https://learn.microsoft.com/en-us/industry/healthcare/healthcare-data-solutions/troubleshoot
- HDS download package: https://aka.ms/HLSFabric
- Fabric mirroring from SQL Server (ms.date 2025-11-05; updated 2026-07-06): https://learn.microsoft.com/en-us/fabric/mirroring/sql-server
- Fabric licences and capacity (ms.date 2026-06-15; updated 2026-08-05): https://learn.microsoft.com/en-us/fabric/enterprise/licenses
- Fabric Warehouse SQL audit logs: https://learn.microsoft.com/en-us/fabric/data-warehouse/sql-audit-logs
- Fabric operation list: https://learn.microsoft.com/en-us/fabric/admin/operation-list
- OneLake diagnostics: https://learn.microsoft.com/en-us/fabric/onelake/onelake-diagnostics-overview
- Microsoft Q&A, BAA/HIPAA: https://learn.microsoft.com/en-my/answers/questions/5960915/hipaa-compliant-business-account
- Microsoft Official Blog, 2023-10-10: https://blogs.microsoft.com/blog/2023/10/10/microsoft-introduces-new-data-and-ai-solutions-to-help-healthcare-organizations-unlock-insights-and-improve-patient-and-clinician-experiences/
- Microsoft Cloud blog, 2023-10-10: https://www.microsoft.com/en-us/microsoft-cloud/blog/healthcare/2023/10/10/unlock-data-value-with-healthcare-data-solutions-in-microsoft-fabric/
- Microsoft Fabric blog, 2024-03-11: https://www.microsoft.com/en-us/microsoft-fabric/blog/2024/03/11/introducing-healthcare-data-solutions-in-microsoft-fabric-a-game-changer-for-healthcare-data-analysis/
- Microsoft in Business, Epic on Azure, 2026-03-19 [vendor]: https://www.microsoft.com/en-us/industry/microsoft-in-business/business-transformation/2026/03/19/delivering-more-cost-efficient-healthcare-with-epic-on-azure/

**Customer stories [vendor]**
- Virtua Health ("4/07/2026"): https://www.microsoft.com/en/customers/story/26318-virtua-health-microsoft-copilot
- UNC Health (2026-05-26): https://www.microsoft.com/en/customers/story/26599-unc-health-microsoft-fabric
- Duke Health (2026-07-28): https://www.microsoft.com/en/customers/story/26907-duke-health-microsoft-defender
- Peterborough Regional Health Centre ("8/04/2026"): https://www.microsoft.com/en/customers/story/26994-peterborough-regional-health-centre-microsoft-fabric
- Apollo Hospitals (2025-11-14): https://www.microsoft.com/en/customers/story/25664-apollo-hospitals-microsoft-fabric

**Consultancy and vendor commentary [vendor]**
- RSM, "Epic's shift to Fabric" (2026-04-21): https://rsmus.com/insights/services/digital-transformation/epics-shift-to-microsoft-fabric-data-analytics.html
- RSM Marketplace offer (403; Reported): https://marketplace.microsoft.com/en-us/marketplace/consulting-services/rsmproductsalesllc1604685958273.epicforfabric
- Hakkoda, "Epic Cogito is Moving to Azure" (2023-09-20): https://hakkoda.io/resources/moving-to-azure/
- EHC Consulting, "EHR on Azure" (2025-05-23): https://ehc.consulting/epic-on-azure-strategy-deployment-models-and-what-you-need-to-know/
- Prominence Advisors, "Data Lakes and Lakehouse Migrations" (undated): https://prominenceadvisors.com/data-lakes-and-lakehouses/
- Mindbowser, Epic Nebula (undated; Reported): https://www.mindbowser.com/epic-nebula-cloud-platform/
- EPC Group, HIPAA Fabric reference architecture (2026; Reported): https://www.epcgroup.net/blog/healthcare-analytics-microsoft-fabric-hipaa-reference-architecture
- Numlytics, Epic Clarity to Fabric (undated; Reported): https://numlytics.com/blog/epic-clarity-to-microsoft-fabric-reporting-dashboard/
- ProArch, Power BI to Fabric migration (undated; Reported): https://www.proarch.com/blog/power-bi-to-microsoft-fabric-migration
- Scient Solutions (undated; Reported): https://scientsolutions.com/harness-epic-data-with-microsoft-fabric/
- Databricks, HIMSS26 guide (2026-03-11): https://www.databricks.com/blog/your-databricks-guide-himss26

**Press and analyst (snippet-level; Reported)**
- Becker's, "3 health systems adopt new Microsoft AI tools" (Oct 2023): https://www.beckershospitalreview.com/healthcare-information-technology/digital-health/3-health-systems-adopt-new-microsoft-ai-tools/
- Fierce Healthcare, Epic UGM AI (2026; date not captured): https://www.fiercehealthcare.com/health-tech/epic-expands-ai-ambitions-agent-platform-cosmos-powered-predictions-and-deeper-workflow
- KLAS, Snowflake in Healthcare 2023: https://klasresearch.com/report/snowflake-in-healthcare-2023-streamlining-data-management-and-improving-operations-in-the-cloud/3359

**Forums (snippet-level; Reported)**
- Capacity Throttling: https://community.fabric.microsoft.com/t5/Fabric-platform/Capacity-Throttling/m-p/4919534
- Fabric Security Issues: https://community.fabric.microsoft.com/t5/Fabric-platform/Fabric-Security-Issues/m-p/4709679
- CLS/RLS announcement: https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/Announcing-Column-Level-amp-Row-Level-Security-for-Fabric/ba-p/5172201

**Jobs**
- Ovation Healthcare (Verified): https://www.builtinboston.com/job/ms-fabric-data-engineer/11192405
- NYC Health + Hospitals (Reported): https://www.jobleads.com/us/job/senior-epic-data-engineer-caboodle-clarity-expert--new-york--ea0e9c510fe2bddec44fa831c17ad31a7
- Quoris (Reported): https://bebee.com/us/jobs/senior-healthcare-data-engineer-epic-clarity-quoris-philadelphia-pa--t7xk-877543515
- NC Health / UNC (Reported): https://jobs.disabilitytalent.org/jobs/266422393-microsoft-fabric-data-engineer
