# Fabric Apps vs Power BI reports — one page

Checked on Microsoft Learn on 21 Oct 2026. Fabric changes monthly: check the linked pages before you decide.

| | Fabric Apps | Power BI reports |
|---|---|---|
| **What it is** | Data-driven applications built on Fabric with the Rayfin SDK | Reports and dashboards on a semantic model |
| **Status** | Preview | Generally available |
| **Who builds it** | Developers: data models, client code and app logic in TypeScript (also with GitHub Copilot or Claude Code) | Report builders in Power BI Desktop or the web |
| **What you get for free** | Generated APIs (GraphQL), sign-in, hosting | Visuals, filters, sharing, subscriptions |
| **Data it reads** | A lakehouse, warehouse, SQL database in Fabric, or semantic model | Import, DirectQuery or Direct Lake semantic models |
| **Writes data back** | Yes: queries and mutations | Possible with write-back to a SQL database in Fabric (check current status) |
| **Turning it on** | A Fabric tenant admin must enable the Fabric Apps workload | Available with your Power BI / Fabric licences |
| **Cost** | Runs on Fabric capacity: every operation of its SQL database, GraphQL API, functions and OneLake storage consumes CUs | Fabric/Premium capacity or Pro/PPU licences; below F64, every viewer needs Pro, PPU or a trial |
| **Where** | Not available in all regions yet | Your tenant's region |
| **Access** | Fabric SSO; hosted assets can require Fabric item access or allow anonymous access | Workspace roles, app audiences, row-level security |

## Use which?
- **People need to read and explore the numbers →** Power BI report.
- **People need to enter, edit or approve data (the tracker emailed around every morning) →** Fabric App, once it's out of
  preview for your workloads — or Power BI with write-back if your team doesn't write TypeScript.
- **Both:** the app captures the data, the report reads it from the same Fabric source.

## Before you build one for a health system
- Don't put patient data in a preview feature.
- Decide on anonymous access to hosted pages before any data is connected.
- Watch the app's capacity use in the Fabric Capacity Metrics app; it shares the capacity with your reports.

## Sources
- Fabric Apps overview — https://learn.microsoft.com/en-us/fabric/apps/overview (updated 2026-09-15)
- Pricing and capacity usage for Fabric Apps — https://learn.microsoft.com/en-us/fabric/apps/pricing (2026-09-15)
- Create a Fabric app with Claude Code — https://learn.microsoft.com/en-us/fabric/apps/create-app-with-claude-code
- Fabric licences (F64 viewers) — https://learn.microsoft.com/en-us/fabric/enterprise/licenses
