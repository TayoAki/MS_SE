# Set 3: Data scripts, news × formats (Oct 21 2026)

Brought into this repo on Oct 22 2026 from the summary "All scripts and what inspired them" (`all-scripts-and-inspirations.md`). The wording matches that summary except where the Oct 22 fact-check changed it; each change is listed under its script. The inspiration numbers are from the original TikTok and YouTube research; they were not re-pulled here (TikTok needs the ScrapeCreators key). Example cuts are in the house style (`content-machine/formats.md`) with a free local AI stand-in voice; replace it with your own take.

## 7. Claude builds dashboards on your Databricks data now

| | |
| --- | --- |
| Set | Set 3 |
| File | `data-scripts-2026-10-21.md` |
| Length | ~45 s (example cut: 49 s) |
| Keyword | DASH |

**Inspired by:**
- [@nocode.joshua, "Claude just dropped Claude Dashboards"](https://www.tiktok.com/@nocode.joshua/video/7695498034079108359): 228K views, 3.5% saves (same topic).
- [Pavan Lalwani, "I Created a Full Dashboard in 3 Minutes Using Claude AI"](https://www.youtube.com/watch?v=Rlkkl2wc4pQ): 972K views, 163× channel median.
- [@copilottips, "Copilot built me the work dashboard Microsoft forgot to make"](https://www.tiktok.com/@copilottips/video/7690607180663344416): 513K views.

**What we took:** "AI builds the dashboard", #2 of the top 10 formats; a 3-step layout with you below and product cards above.

**Script:**

> Claude can now build a live dashboard straight from your Databricks data, and you never write the query.

> It's called Claude Dashboards. It came out on October 8th, and it's in beta on paid plans.

> Step one: connect your data. Sources include Databricks, Snowflake, BigQuery, Redshift and ClickHouse.

> Step two: ask in plain English. Something like, how did this month's pipeline compare to last month?

> Claude writes the query and builds the dashboard.

> Step three: it stays current as your data changes.

> And this is the part I'd show your boss. Click any number, and it shows you the query behind it. Every chart also shows when it last refreshed.

> Two catches. Power BI isn't on the list of tools you can send it to. And on Enterprise plans, it's off until your admin turns it on.

> Comment DASH and I'll send you my setup checklist.

**Facts from** (re-checked Oct 22 2026):
- [Anthropic, "Build live dashboards and animate explainers with Claude"](https://claude.com/resources/articles/dashboards-and-motion), Oct 8 2026
- [Get started with Claude Dashboards](https://support.claude.com/en/articles/17454700-get-started-with-claude-dashboards): Pro, Max, Team and Enterprise; Enterprise off by default until an owner turns it on

**Changed from the original wording** (the fact-check):
- "Databricks, Snowflake, BigQuery, Redshift and ClickHouse are all on the list" → **"Sources include Databricks, Snowflake, BigQuery, Redshift and ClickHouse"** (Anthropic gives them as examples).
- "it stays live. When the data changes, the dashboard changes. No asking again." → **"it stays current as your data changes"** (Anthropic doesn't say how it refreshes).

**Keep exact / check before filming:**
- Power BI is in neither the send-to list nor the coming-soon list.

**Example cut:** `docs/reels/demo/nine/s7-claude-dashboards.json` → `~/persa-shorts/nine/s7-claude-dashboards/s7-claude-dashboards.mp4` (house style, AI stand-in voice, no face). Shot list:

| # | Say | Picture (example cut) |
|---|---|---|
| 1 | Claude can now build a live dashboard straight from your Databricks data, and you never write the query. | First frame (the thumbnail): **CLAUDE / DASHBOARDS** · "live, from your Databricks data" |
| 2 | It's called Claude Dashboards. It came out on October 8th, and it's in beta on paid plans. | Real screen `claude-dash.png` (CLAUDE.COM · OCT 8 2026), phrase boxed |
| 3 | Step one: connect your data. Sources include Databricks, Snowflake, BigQuery, Redshift and ClickHouse. | Giant outlined **1** · CONNECT YOUR DATA · Databricks · Snowflake · BigQuery · Redshift · ClickHouse |
| 4 | Step two: ask in plain English. Something like, how did this month's pipeline compare to last month? | Giant outlined **2** · ASK IN PLAIN ENGLISH |
| 5 | Claude writes the query and builds the dashboard. | Text card: Claude **writes the query**. And builds the dashboard. |
| 6 | Step three: it stays current as your data changes. | Giant outlined **3** · IT STAYS CURRENT |
| 7 | And this is the part I'd show your boss. Click any number, and it shows you the query behind it. Every chart also shows when it last refreshed. | Text card: Click any number: **the query behind it**. Every chart: when it last refreshed. |
| 8 | Two catches. Power BI isn't on the list of tools you can send it to. And on Enterprise plans, it's off until your admin turns it on. | Text card: Catches: **no Power BI** export. Enterprise: **off until an admin turns it on**. |
| 9 | Comment DASH and I'll send you my setup checklist. | Call to action: COMMENT “DASH” |

---

## 8. I analysed every complaint New York made to 311 this year

| | |
| --- | --- |
| Set | Set 3 |
| File | `data-scripts-2026-10-21.md` |
| Length | ~50 s (example cut: 54 s) |
| Keyword | NYC |

**Inspired by:**
- [@gourmet.data, "using data science to understand perfumes"](https://www.tiktok.com/@gourmet.data/video/7683919006683680014): 122K views on 5.8K followers (21×), 4.0% saves.
- [The Bald Coder, "I'm a Data Scientist. I Analyzed the ENTIRE Qur'an"](https://www.youtube.com/watch?v=MpWb5YBsVxc): 618K views, 573× channel median.

**What we took:** "A data person analyses something that isn't data", #1 of the top 10 formats (the highest share rate).

**Script:**

> New Yorkers filed almost four million complaints with 311 in the last year.

> I loaded every one of them into Microsoft Fabric and asked it questions in plain English.

> Number one isn't noise. It's illegal parking. Six hundred and eleven thousand complaints.

> Residential noise is second, and noise has a clock.

> Complaints about noisy neighbours peak between ten and eleven at night.

> And the worst day isn't Friday or Saturday. It's Sunday.

> Over half of those are loud music or a party. Most of the rest are banging and pounding.

> Heat is the seasonal one. January had about twenty-two times more heat complaints than August.

> But my favourite part of this data set is the bottom of the list.

> Fifteen complaints about radioactive material. Six about squeegees. And exactly one complaint filed under trapping pigeon.

> Comment NYC and I'll send you the data set and every question I asked.

**Facts from** (re-checked Oct 22 2026):
- [NYC 311 Service Requests from 2020 to Present](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9) (dataset erm2-nwe9, renamed from "2010"), Oct 1 2025 – Sep 30 2026, re-queried Oct 22 2026: 3,963,898 requests; Illegal Parking 611,282; Noise - Residential 432,431; peak hour 10–11 pm (42,705); Sunday 87,909 vs Saturday 82,975; Loud Music/Party 57.3%, Banging/Pounding 34.1%; heat January 79,928 vs August 3,682 (21.7×); Radioactive Material 15, Squeegee 6, Trapping Pigeon 1

**Changed from the original wording** (the fact-check):
- "Noise is second" → **"Residential noise is second"**. All noise types together come to 802,105 and would rank first.

**Keep exact / check before filming:**
- ⚠ Load the data into Fabric and ask those questions before filming; the script says you did.
- Say "trapping pigeon" exactly: pigeon complaints in general are 1,835.

**Example cut:** `docs/reels/demo/nine/s8-nyc-311.json` → `~/persa-shorts/nine/s8-nyc-311/s8-nyc-311.mp4` (house style, AI stand-in voice, no face). Shot list:

| # | Say | Picture (example cut) |
|---|---|---|
| 1 | New Yorkers filed almost four million complaints with 311 in the last year. | First frame (the thumbnail): **4 MILLION / 311 COMPLAINTS** · "NYC Open Data · Oct 2025 – Sep 2026" |
| 2 | I loaded every one of them into Microsoft Fabric and asked it questions in plain English. | Text card: Every one, into **Microsoft Fabric**. Asked in **plain English**. |
| 3 | Number one isn't noise. It's illegal parking. Six hundred and eleven thousand complaints. | Bar chart "Top complaints": Illegal parking 611,282; Residential noise 432,431; Heat / hot water 359,087; Blocked driveway 194,672; Street noise 174,340 |
| 4 | Residential noise is second, and noise has a clock. | Text card: Residential noise is **second**. And noise has **a clock**. |
| 5 | Complaints about noisy neighbours peak between ten and eleven at night. | Giant outlined **10PM** · THE PEAK HOUR · 10–11 pm · 42,705 complaints |
| 6 | And the worst day isn't Friday or Saturday. It's Sunday. | Bar chart "Residential noise by day": Sunday 87,909; Saturday 82,975; Friday 56,168; Monday 53,531; Wednesday 51,514; Tuesday 51,286; Thursday 49,048 |
| 7 | Over half of those are loud music or a party. Most of the rest are banging and pounding. | Bar chart "What the noise is": Loud music / party 247,972; Banging / pounding 147,644; Loud talking 29,669; Loud TV 7,146 |
| 8 | Heat is the seasonal one. January had about twenty-two times more heat complaints than August. | Bar chart "Heat / hot water": January 2026 79,928; August 2026 3,682 |
| 9 | But my favourite part of this data set is the bottom of the list. | Text card: My favourite part: **the bottom of the list**. |
| 10 | Fifteen complaints about radioactive material. Six about squeegees. And exactly one complaint filed under trapping pigeon. | Bar chart "The bottom of the list": Radioactive material 15; Squeegee 6; Trapping pigeon 1 |
| 11 | Comment NYC and I'll send you the data set and every question I asked. | Call to action: COMMENT “NYC” |

---

## 9. Pausing your Fabric capacity doesn't save money if you reserved it

| | |
| --- | --- |
| Set | Set 3 |
| File | `data-scripts-2026-10-21.md` |
| Length | ~35 s + an 8 s text cut (example cut: 39 s) |
| Keyword | PAUSE |

**Inspired by:**
- [@kairadc, "misconception that you need a coding language to land your first data analyst role"](https://www.tiktok.com/@kairadc/video/7671004519790054678): 235K views on 1.1K followers (216×), 5.9% saves.

**What we took:** The myth-bust: the misconception stated flat, then the answer building on screen.

**Script:**

> Pausing your Fabric capacity doesn't save money if you bought a reservation.

> A reservation is a prepaid commitment, used hour by hour.

> An hour you don't use doesn't carry over. So pausing a reserved capacity just throws those hours away.

> Pausing only cuts pay-as-you-go compute, and your storage keeps billing either way.

> And there's a second surprise. When you pause, any smoothed usage still waiting to be billed is added up and charged straight away.

> So before you pause, check two things.

> Is this capacity reserved? And how much smoothed usage is waiting?

> The Capacity Metrics app shows it as carry-forward.

> Comment PAUSE and I'll send you my capacity cost checklist.

**Facts from** (re-checked Oct 22 2026):
- [Save costs with Fabric capacity reservations](https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/fabric-capacity): "applied to CUs on an hourly basis… It doesn't carry over" (Sep 30 2026)
- [Pause and resume your Fabric capacity](https://learn.microsoft.com/en-us/fabric/enterprise/pause-resume): "the remaining cumulative overages and smoothed operations… are summed, and added to your Azure bill" (Aug 14 2026)
- [OneLake consumption](https://learn.microsoft.com/en-us/fabric/onelake/onelake-consumption): "When a capacity is paused, the data stored continues to be billed"

**Changed from the original wording** (the fact-check):
- "A reservation is paid for every hour, whether you use it or not. Microsoft applies it hour by hour…" → **"A reservation is a prepaid commitment, used hour by hour. An hour you don't use doesn't carry over."**
- "Pausing only saves money on pay-as-you-go." → **"Pausing only cuts pay-as-you-go compute, and your storage keeps billing either way."**
- "…how much smoothed usage is waiting? The Capacity Metrics app shows you." → **"The Capacity Metrics app shows it as carry-forward."** It is shown as a percentage, then as a spike when you pause.

**Keep exact / check before filming:**
- The 8 s text cut is `s9b-pausing-text-cut`: three text cards with the voice.

**Example cut:** `docs/reels/demo/nine/s9-pausing-reserved-capacity.json` → `~/persa-shorts/nine/s9-pausing-reserved-capacity/s9-pausing-reserved-capacity.mp4` (house style, AI stand-in voice, no face). Shot list:

| # | Say | Picture (example cut) |
|---|---|---|
| 1 | Pausing your Fabric capacity doesn't save money if you bought a reservation. | First frame (the thumbnail): **PAUSING / DOESN'T SAVE** · "if you bought a reservation" |
| 2 | A reservation is a prepaid commitment, used hour by hour. | Text card: A reservation: **prepaid**, used **hour by hour**. |
| 3 | An hour you don't use doesn't carry over. So pausing a reserved capacity just throws those hours away. | Real screen `reservation.png` (MICROSOFT LEARN), phrase boxed |
| 4 | Pausing only cuts pay-as-you-go compute, and your storage keeps billing either way. | Text card: Pausing cuts **pay-as-you-go** compute only. Storage keeps billing. |
| 5 | And there's a second surprise. When you pause, any smoothed usage still waiting to be billed is added up and charged straight away. | Real screen `pause.png` (MICROSOFT LEARN), phrase boxed |
| 6 | So before you pause, check two things. | Giant outlined **2** · CHECKS |
| 7 | Is this capacity reserved? And how much smoothed usage is waiting? | Stage words in big yellow caps, each on its spoken word: RESERVED? · USAGE WAITING? |
| 8 | The Capacity Metrics app shows it as carry-forward. | Real demo clip `capacity.mp4` (Microsoft Learn, CC BY 4.0) |
| 9 | Comment PAUSE and I'll send you my capacity cost checklist. | Call to action: COMMENT “PAUSE” |

---
