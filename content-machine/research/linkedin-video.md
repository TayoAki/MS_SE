# LinkedIn short vertical video for Microsoft Fabric work with US health systems: research notes

Research date: **2026-10-21**. All fetches were made that day from a cloud container using curl, WebFetch or WebSearch.

Labels:
- **Verified**: I fetched the primary page or feed myself and read the text quoted.
- **Reported**: a credible secondary source states it, or a search summary did and I did not open the page.
- **Inference**: my own reasoning from the verified facts.

LinkedIn Help pages show "Last updated: N ago" instead of a date. I convert that to an approximate date counted back from 2026-10-21.

---

## Part A: LinkedIn video facts

### A1. Organic video specs for personal profiles

| Item | What LinkedIn says | Status / source |
|---|---|---|
| File formats (feed upload) | MP4, MOV, AVI, WEBM, MKV, WMV, VC1, MPEG/MPEG2/MPEG1VIDEO, DVVIDEO, QTRLE, TSCC2 on desktop, iOS and Android. ProRes "may upload but will not process". | Verified: Help a548372 "Video sharing troubleshooting", last updated about 2 years ago (about 2024) |
| File size | Min 75 KB, max **5 GB** | Verified: a548372 |
| Duration | Min **3 s** (desktop) / **2 s** (mobile app); max **15 min** | Verified: a548372 |
| Resolution | 256x144 to 4096x2304 (so 1080x1920 is in range) | Verified: a548372 |
| Aspect ratio | **1:2.4 to 2.4:1**. 9:16 (1:1.78) is within range. | Verified: a548372 |
| Frame rate / bitrate | 10 to 60 fps; 192 kbps to 30 Mbps | Verified: a548372 |
| Safe zones | "Keep the edges (top, bottom, and sides) of your video free of key elements, text, and logos… [so they] aren't overlapped by the LinkedIn user interface." No pixel values are given. | Verified: a548372 |
| A newer "media file types" page | Lists video MP4, MOV, WEBM (desktop and Android), MKV (desktop), with a 100 MB note. This page is about **profile "featured" media samples**, not feed video posts. | Verified: Help a564109, last updated about 4 weeks ago (about Sep 2026) |
| Pages / Career Pages video (not personal profiles) | Max 10 min; AVI/QuickTime/MOV not supported for that surface | Verified: Help a1311816, last updated about 4 years ago |
| Captions: SRT upload | "You must have an associated SRT (SubRip Subtitle) file attached… using the desktop experience." Works for personal accounts and Pages: Share box → Video → Edit → "Select Caption". | Verified: Help a552177, last updated about 5 years ago, so menus may differ now |
| Captions: auto | Auto captions can be turned on at upload, with an optional "review before viewers can see them" step. Editable later from More → Edit captions. Languages: English, Spanish, Portuguese, French, German, Italian, Indonesian, Turkish, Arabic, Dutch. "Available for all LinkedIn members and Pages." For scheduled video posts, captions can be reviewed only after the video posts. | Verified: Help a1327025, last updated about 1 year ago (about late 2025) |
| Autoplay / sound | "Some videos on LinkedIn may play automatically **without sound** as you scroll." Members control this (desktop on/off; mobile never / Wi-Fi only / always). "There is no on/off toggle for **auto-looping on videos under 30 seconds**." | Verified: Help a565326, last updated about 3 weeks ago (about late Sep / early Oct 2026) |
| Autoplay (ads page) | "LinkedIn Video Ads will autoplay in the feed with the sound muted by default." | Verified: business.linkedin.com video-ads page (undated, accessed 2026-10-21) |
| Thumbnails (organic) | **Not verified.** The current "Share photos on LinkedIn" page (a527229) covers photos only. A search summary said an older "Share photos or videos" version listed "upload video thumbnail", but the live page no longer shows it. Ads specs do list "Custom Thumbnail: Optional but recommended" (JPG/PNG). | Verified for ads only (business.linkedin.com video-ads/specs and Help a424737); organic status unknown |
| Ads specs, for reference | 9:16 allowed (min 360x640, max 1080x1920). The ads help page marks **4:5 as "Recommended ratio"**. 3 s to 30 min; 75 KB to 500 MB; MP4; 30 fps recommended; captions must be SRT, text only. | Verified: business.linkedin.com/advertise/ads/sponsored-content/video-ads/specs and Help a424737 (undated pages) |
| Native scheduling | Posts can be scheduled from 10 minutes to 3 months ahead. Events and Jobs cannot be scheduled. | Verified: Help a1347212, last updated about 2 weeks ago |
| Pinned comments | You can pin one comment (yours or another member's) on your own post, including video posts. It shows first in both Most Relevant and Most Recent. | Verified: Help a16666203, last updated about 2 days ago |

**What this means for the creator (Inference):**
- Export **1080x1920 MP4, H.264/AAC, 30 fps, under about 200 MB**. All of that is inside LinkedIn's verified ranges, and MP4 is the one format every page lists.
- Videos autoplay muted, so **burned-in captions are the right default**.
- **Turn auto-captions off** on upload. Otherwise LinkedIn can add a second caption layer over the burned-in one-word captions.
- Optionally attach an SRT on desktop for accessibility. LinkedIn renders it as closed captions viewers can toggle.
- Keep captions and the "big words" away from the bottom and side edges, because the LinkedIn interface sits there.
- Clips **under 30 s auto-loop**, which inflates watch time and replays. The 30 to 60 s range does not loop automatically.
- Personal-profile video has no verified custom-thumbnail control, so **design the first frame to work as the thumbnail**.

### A2. Vertical video feed / "Video" tab: what LinkedIn has said

**Official (Verified): Help a6290168, "Full-screen vertical video on LinkedIn", last updated about 5 months ago (about May 2026).**
- "Full-screen video, the video tab, and the video carousel may not be available to all members at this time."
- "You cannot directly add or post videos to the full-screen vertical video feed or the video tab… Any video you post to LinkedIn may be eligible to appear in the video feed, tab, or carousel **based on relevance and performance**."
- "There are no options to customize this experience or a dedicated process for content selection at this time."
- LinkedIn may use AI to generate titles for video carousels.
- From the player, viewers can follow, open a mini profile, and see a **grid of the creator's other videos**, which then autoplay in sequence. Mobile access: the **Video** item in the bottom navigation bar, any feed video, or "Videos for you".

**Official (Verified): Help a10728043, "Video visibility and quality on LinkedIn", last updated about 6 months ago (about Apr 2026).**
- Distribution is shaped by "automated signals and member feedback". Creators whose videos repeatedly draw strong negative feedback "may be shown less often to members who don't already follow them". The effect is "temporary, not permanent".
- LinkedIn's description of quality: "clear and easy to understand, professional in tone, relevant to the intended audience, and provide helpful or actionable information."

**Timeline (Reported, from secondary press; I found no LinkedIn press release):**
- **2024-03-29**: Engadget reports LinkedIn testing a TikTok-like vertical video feed in a new video tab. "Hasn't been publicly announced… the company confirmed the tests to TechCrunch."
- **2025-01-31**: Digiday says a LinkedIn representative reported total video viewership up **36% YoY** and video creation "growing at twice the rate of other post formats". The article adds that the company reported **+34% YoY video uploads in fiscal Q4 2024** and **+36% YoY viewership in fiscal Q1 2025**.
- **Early 2025** (exact date not extracted): MediaPost and Social Media Today report a full-screen vertical display coming to desktop and web, plus planned average watch time analytics for creators.

**Official LinkedIn guidance on video for B2B (Verified; the pages are undated, accessed 2026-10-21).**
- business.linkedin.com "How to market on LinkedIn":
  - "Videos should be about 1-2 minutes and should capture attention within the first few seconds. Add subtitles for those watching with the sound off."
  - "Live video generates 24x more comments than regular video." (No methodology given.)
- business.linkedin.com Video Ads page:
  - "captions are strongly recommended… Since videos autoplay without sound, captions help ensure your message is clear from the first frame."
  - "Shorter videos are often effective for capturing attention."
  - Claims "Video Ads drive 3x higher engagement than non-video formats" and "Videos are 20x more likely to be shared than any other post". **Weak evidence:** these are marketing claims with no date or method.
- Video Ads best-practices page: "Video Ads earn 30% more comments per impression than static images in the LinkedIn newsfeed." This is ad data, not organic.
- **Inference:** LinkedIn's own organic guidance ("1 to 2 min") is longer than the 30 to 60 s plan. Nothing official says short is penalized, and sub-30 s clips loop by design. The official points that carry over directly are: hook in the first seconds, captions for sound-off viewing, and a professional, helpful tone.

### A3. Performance data: video vs. document/carousel, and posting frequency

None of this is official LinkedIn data except the Digiday figures that a LinkedIn representative supplied (see A2). Everything below is a **third-party analysis**.

**Socialinsider, "2026 LinkedIn Benchmarks"** (third party; Verified by fetching the page on 2026-10-21)
- **Sample:** 1.3M posts from **16,645 LinkedIn company Pages**, Jan 2024 to Dec 2025. Quarterly updates run through Q3 2026. **Personal profiles are not in the sample.**
- **Engagement rate by impressions, 2024 → 2025:** native document 6.10% → **7.00%**; multi-image 6.60% → 6.45%; video 5.60% → **6.00%**; image 4.85% → 5.30%; text 4.00% (2024).
- **Q3 2026:** native documents **6.40%** ("most engaging format"), multi-image 6.40%, **video 5.25%** ("significant engagement rate decrease"), image 4.70%, polls 3.60%, text 3.50%, links 2.50%.
- **Video views:** "across all LinkedIn pages, there's a **36% YoY decline in views**". Average views per video for Pages with 1 to 5K followers: 190 (2025) → 155 (2026); 5 to 10K: 400 → 245; 10 to 50K: 1,000 → 585.
- **Page posting frequency (posts per month), 2024 → 2025:** video 2 → 4; document 1 → 2; image 5 → 7.
- **Caveat (Inference):** these are brand Pages, which reach far less than personal profiles. Use the format ranking (documents and multi-image ≥ video > image > text > link) as directional only.

**Buffer, "How Often Should You Post on LinkedIn in 2026? Data From 2 Million+ Posts"** (third party; Verified by fetch; exact publish date not extracted)
- **Sample:** 2M+ posts from 94,000+ accounts (Buffer users). Analysis by Buffer data scientist Julian Winternheimer, comparing each account's busier weeks with its quieter ones.
- **Results versus posting once a week:**
  - 2 to 5 posts/week: **+1,182 impressions/post** and +0.23 pp engagement rate.
  - 6 to 10 posts/week: +5,001 impressions/post and +0.76 pp.
  - 11+ posts/week: "nearly triple the engagements per post".
- Buffer calls **2 to 5 per week the "sweet spot"**, with diminishing returns above that.
- **Caveat:** observational data from tool users. It shows correlation, not cause.

**Buffer, "How LinkedIn's Algorithm Works in 2026, According to the LinkedIn Team"** (third party relaying LinkedIn staff; Verified by fetch)
- Sources named on the page include LinkedIn News' Senior Director / Executive Editor. Advice: "Avoid engagement bait — posts that ask for likes, shares, or comments in a spammy way can hurt your reach." Buffer also says links in comments "do not appear to have a negative impact".
- This is **Reported**: Buffer's paraphrase, not a LinkedIn document.

**Richard van der Blom, "Algorithm Insights" report** (third party; **weak evidence**: I could only reach secondary summaries)
- Reported as the **7th edition**, analysing 1.3M posts from H1 2026. A podcast summary claims reach is "down 60% for active creators over the last two years". It also describes a shift from a relationship graph to an interest graph.
- Sources: kokasexton.com summary and the Creator Science podcast page. The report itself is gated at sales.richardvanderblom.com, which I did not open.
- Do not quote these numbers as fact.

**Bottom line (Inference):** No source gives a clean, recent, personal-profile, B2B-specific comparison of video and document posts. The defensible plan:
- Post **2 to 5 times a week**.
- Lead with short captioned vertical video. LinkedIn is pushing video surfaces, and the Video tab and creator grid only surface video.
- Add **document/carousel posts**, which third-party data consistently ranks at or near the top for engagement rate.
- Judge success from the creator's own analytics. All members have creator analytics with an export (Verified: Help a704175).

### A4. Rules that matter

| Topic | Official text | Status / source |
|---|---|---|
| Automation of comments, DMs, connection requests, likes | User Agreement §8.2: you agree not to "Use bots or other unauthorized automated methods to access the Services, add or download contacts, **send or redirect messages, create, comment on, like, share, or re-share posts**, or otherwise drive inauthentic engagement". Also prohibits scraping and "manipulating algorithms". | Verified: linkedin.com/legal/user-agreement, "Effective on November 3, 2025" |
| Third-party tools / extensions | "We don't permit the use of any third party software, including 'crawlers', bots, browser plug-ins, or browser extensions that scrape, modify the appearance of, or **automate activity** on LinkedIn's website… [or] fake engagement… including any tools or services that try to manipulate LinkedIn's content algorithms." Accounts risk being "restricted or shut down". | Verified: Help a1341387 "Prohibited software and extensions", last updated about 2 years ago |
| Engagement pods | Professional Community Policies: "Don't do things to artificially increase engagement with your content. Respond authentically to others' content and **don't agree with others ahead of time to like or re-share each other's content**." The word "pod" is not used, but this describes one. | Verified: linkedin.com/legal/professional-community-policies (accessed 2026-10-21) |
| Promotional invitations | "Do not use our invitation feature to send promotional messages to people you don't know." | Verified: same page |
| Spam / engagement bait | LinkedIn "may remove or limit the distribution of content designed to artificially increase engagement". Examples: emoji/reaction polls; misrepresenting platform features; chain-letter content requesting likes, reactions and shares; "**Excessive, irrelevant, or repetitive comments or messages**". | Verified: Help a1338787 "Spam", last updated about 2 years ago |
| "Comment WORD and I'll DM you" | **No official LinkedIn statement found** that names this format, either allowing or banning it. Third-party blogs (Hootsuite, SocialPilot, Dataslayer and others, 2026) claim LinkedIn demotes engagement bait. One attributes a quote to LinkedIn's Tim Jurka, but I found no primary source. | Reported / unverified |

**Inference for the comment-keyword call to action:**
- The format is not on LinkedIn's own spam example list. The nearest listed example is "chain letter… requesting likes, reactions, and shares".
- The real risks are:
  1. **Automating** the DMs or comment replies (for example auto-DM tools). That clearly breaches §8.2 and a1341387.
  2. Sending identical DMs at volume, which risks "excessive… repetitive… messages".
  3. Possible ranking demotion if the system classifies the post as engagement bait. Treat that as a risk, not a confirmed rule.
- Safer pattern:
  - The call to action should ask a **real, specific question**, or offer a genuinely useful resource.
  - **Reply and DM by hand** with personalised text.
  - Put the resource in a **pinned comment** as well, so nobody *has* to comment to get it.
- Posting and scheduling through LinkedIn's native scheduler is explicitly supported (a1347212). Third-party schedulers are a separate question: §8.2 bans "unauthorized automated methods", so check that any tool posts through LinkedIn's official API.

---

## Part B: Who posts about Microsoft Fabric and/or healthcare data

I only list people and accounts whose content I could fetch on 2026-10-21. LinkedIn profile pages returned HTTP 429 to curl, so they are cited only when a public post URL loaded.

| # | Who | What they post | Format | URL (verified) | Status |
|---|---|---|---|---|---|
| 1 | **Adam Saxton & Patrick LeBlanc**, Guy in a Cube | Power BI and Fabric how-tos. Newest upload 2026-10-21 "How to Use Direct Lake Calculated Columns in Power BI". **11 of the last 15 uploads are YouTube Shorts**; 7 of 15 titles mention Fabric (e.g. "Stop Updating Microsoft Fabric Workspaces One by One", 2026-08-28). | YouTube long-form + Shorts | https://www.youtube.com/@GuyInACube | Verified (channel page names both; feed fetched) |
| 2 | **Reza Rad**, RADACAD | Power BI, Fabric and AI "straight from real consulting work". Channel says "Microsoft Regional Director" and long-time MVP. Newest 2026-10-21 "Microsoft IQ Explained: Work IQ, Fabric IQ, Foundry IQ and Web IQ". **8 of 15 recent uploads are #shorts**; 12 of 15 mention Fabric. | YouTube long-form + Shorts | https://www.youtube.com/@RADACAD | Verified |
| 3 | **Will**, "Learn Microsoft Fabric with Will" | "I teach Microsoft Fabric full-time." Recent: "Applying top AI researcher's idea to agentic Fabric development" (2026-10-19), "Can I use Open Mirroring for my Microsoft Fabric project?" (2026-04-25). Surname not shown on the channel page. | YouTube long-form | https://www.youtube.com/@FabricFrontiers | Verified (channel); surname not verified |
| 4 | **Marco Russo & Alberto Ferrari**, SQLBI | DAX and semantic modelling for Power BI / Fabric. Short "SQLBI Whiteboard" clips. Newest 2026-10-20 "Continuous axis for any Date table in Power BI". | YouTube + Shorts + articles | https://www.youtube.com/@SQLBI · https://www.sqlbi.com/ | Verified |
| 5 | **Chris Webb**, Chris Webb's BI Blog | Deep Power BI / Fabric semantic-model performance posts, about weekly. Newest 2026-10-18 "Monitoring The Impact Of Full-Text Indexing On Semantic Model Refresh In Power BI". Works at Microsoft on the Fabric team (Reported, not verified here). | Blog (long-form text) | https://blog.crossjoin.co.uk/ | Verified (blog); role Reported |
| 6 | **Arun Ulag**, Microsoft Fabric executive | Fabric launch and strategy posts on LinkedIn, e.g. 2023-05-23 post sharing TechCrunch's Fabric launch story. Title (CVP, Azure Data) not verified here. | LinkedIn text + link posts | https://www.linkedin.com/posts/arunulag_microsoft-launches-fabric-a-new-end-to-end-activity-7066833730736164864-Go1F | Verified (post) |
| 7 | **Microsoft Fabric** (company Page) | Product announcements, including 2024-03-12 "Introducing healthcare data solutions in Microsoft Fabric". | LinkedIn link posts | https://www.linkedin.com/posts/microsoftfabric_introducing-healthcare-data-solutions-in-activity-7173331936147390464-jVj5 | Verified (post); a brand account, not a person |
| 8 | **Microsoft Fabric** (official YouTube) | Keynotes and customer stories (e.g. "FabCon+SQLCon Europe Keynote", 2026-10-05). No Shorts in the last 15 uploads. | YouTube long-form | https://www.youtube.com/channel/UCH0gDiJ1RSn3kkxRQnQaH1w | Verified |
| 9 | **Jim Novak** | Talks on "Healthcare Data Solutions in Microsoft Fabric": one on the Level Up Your Data channel, and a "Cloud Data Driven" session dated 2025-02-13 on DataDrivenCommunity. Role not verified. | YouTube talks | https://www.youtube.com/watch?v=l81yHEntd1w · https://www.youtube.com/watch?v=SL54I15KtNg | Verified (videos exist); role unverified |
| 10 | **"Microsoft Healthcare and Life Blog Videos"** (YouTube) | Healthcare data solutions in Fabric overview and lakehouse tutorial (e.g. https://www.youtube.com/watch?v=QVpP8-pkx3E). Recent uploads have shifted to Copilot topics (newest 2026-07-24). | YouTube demos | https://www.youtube.com/@microsofthealthcareandlife5580 | Verified (channel); appears Microsoft-run, ownership not confirmed |
| 11 | **Chester King** | One LinkedIn post (2023-08-30) about the Power BI connector for Epic EHR audit data, so healthcare-adjacent only. | LinkedIn post | https://www.linkedin.com/posts/chesterkingeagleridge_set-up-a-connector-to-import-epic-ehr-data-activity-7102684195419787264-pW4W | Verified (post); weak fit |

**Excluded after checking:**
- BI Elite / Parker Stevens: last upload in the feed is 2022.
- KINETIQ Data: had a "[Healthcare Series] … within Microsoft Fabric" video, but the channel now targets supply chain.
- LinkedIn profiles that surfaced in search (e.g. a Microsoft healthcare seller, a health-system nurse-informaticist): I could not load them or confirm what they post.

**Landscape read (Inference):**
- Fabric education content is crowded and Microsoft-centred (Guy in a Cube, RADACAD, SQLBI, Will, Microsoft's own channels). Mostly YouTube, increasingly Shorts.
- I found **no verified individual who posts short vertical videos about Fabric specifically for US health systems on LinkedIn**. Healthcare Fabric content is mostly Microsoft demos and conference talks.
- That gap is the consultant's opening: a healthcare-operator lens (Epic Clarity/Caboodle, quality measures, revenue cycle, HIPAA) on top of Fabric.

---

## Part C: Free public feeds for the RSS/Atom scraper

See the **Verified feeds** table below. Notes:

- **Microsoft Fabric blog.** `https://blog.fabric.microsoft.com/en-us/blog/feed/` and the `/en-US/` variant both 200, **redirecting** to the community board RSS `https://community.fabric.microsoft.com/t5/s/rss/board?board.id=fbc_fabricupdatesblogs` (title "Fabric Updates Blog articles"). Use the final URL directly. Item links point to community.fabric.microsoft.com.
- **Power BI blog.** `https://powerbi.microsoft.com/en-us/blog/feed/` redirects to `…board.id=fbc_pbiupdatesblog` ("Power BI Updates Blog articles").
- **Microsoft Industry Blogs, Health & Life Sciences.** The old `/en-us/industry/blog/healthcare/feed/` returns **404**: it redirects to `/microsoft-cloud/blog/healthcare/feed/` as HTML. `/industry-healthcare/feed/` is a comments feed with 0 items. **Working: `https://www.microsoft.com/en-us/microsoft-cloud/blog/industry/healthcare/feed/`**, titled "Healthcare | The Microsoft Cloud Blog". It posts infrequently (newest 2026-09-30).
- **Microsoft Learn "What's new in Fabric": no native feed found.**
  - The Learn search RSS (`https://learn.microsoft.com/api/search/rss?search=…`) returns 200 but lists doc pages by relevance, not a changelog. Not useful.
  - The GitHub commits Atom for `MicrosoftDocs/fabric-docs` could **not be checked**: GitHub is blocked for this session ("GitHub access to this repository is not enabled for this session").
  - Alternatives: the **Azure updates RSS** (`https://www.microsoft.com/releasecommunications/api/v2/azure/rss`, 200, 200 items, 2 with "Fabric" in the title today; filter on "Fabric"), and the monthly "Power BI … Feature Summary" posts in the Power BI feed.
- **Reddit.** All three subreddit feeds returned Atom with a browser User-Agent. Keep the request rate low; Reddit rate-limits.
- **Healthcare IT News.** `/home/feed` and `/feed` return **403 with a Cloudflare "Just a moment…" challenge** from this container.
  - Fallback that works: **Google News RSS** `https://news.google.com/rss/search?q=site:healthcareitnews.com+when:7d&hl=en-US&gl=US&ceid=US:en` (200, 33 items, newest 2026-10-19).
  - Google News links are redirect wrappers. Without `when:7d` the results are relevance-sorted and include items from 2025.
- **Becker's.**
  - The section feeds (`/healthcare-information-technology.feed`, `/healthcare-information-technology/feed/`, `/category/…/feed/`) all return **403**.
  - **`https://www.beckershospitalreview.com/feed/`** works: all topics, 10 items. Filter by link path (e.g. `/healthcare-information-technology/`).
  - A Google News `site:beckershospitalreview.com "health IT"` feed also works.
- **Fierce Healthcare.**
  - **`https://www.fiercehealthcare.com/rss/xml`** works: 25 items. Quirks: titles are wrapped in an HTML `<a>` element, so take the inner text; `pubDate` is non-RFC (e.g. "Oct 21, 2026 10:30am"); items are not strictly date-ordered.
  - Section feeds (`/rss/health-tech/xml`, `/rss/digital-health/xml`, `/rss/ai-and-machine-learning/xml`) return valid RSS with **0 items**.
- **YouTube.** Channel IDs were taken from each channel page's `externalId` and confirmed by fetching the feed: Microsoft Fabric `UCH0gDiJ1RSn3kkxRQnQaH1w`, Guy in a Cube `UCFp1vaKzpfvoGai0vE5VJ0w`. Extras: SQLBI `UCcc21gBGNJwZM_eDEByeN-Q`, RADACAD `UCsOfIwAXj1fT6LDqEDEAb4g`, Learn Microsoft Fabric with Will `UCrvoIYkzS-RvCEb0x7wfmwQ`, Microsoft Healthcare and Life Blog Videos `UCFHGcKtofw8IQZRVFpTBjEw`.
- **Hacker News.**
  - `https://hnrss.org/newest?q=%22Microsoft+Fabric%22` works (20 items; Fabric stories are rare, newest 2026-09-30).
  - The Algolia JSON API also works: `https://hn.algolia.com/api/v1/search_by_date?query=%22microsoft%20fabric%22&tags=story`.
  - Suggested extra queries (not tested): `"OneLake"`, `"Direct Lake"`, `"Power BI"`, `"FHIR"`, `"Epic Systems"`.
- **GitHub search terms** (Inference; **not verified**, because GitHub is blocked in this session):
  - `topic:microsoft-fabric`
  - `"microsoft fabric" in:name,description,readme`
  - `fabric lakehouse notebook`
  - `"healthcare data solutions" fabric`
  - `FHIR OMOP fabric`
  - `semantic-link`
  - `fabric-cicd`
  - Sort by `updated`. GitHub supports `releases.atom` feeds per repo, but none were tested here.
- **Bonus blog feeds** (verified): SQLBI `https://www.sqlbi.com/feed/` (200, 30 items) and Chris Webb `https://blog.crossjoin.co.uk/feed/` (200, 10 items).

### Verified feeds

All fetched 2026-10-21 with a desktop Chrome User-Agent. Newest item is by date as the feed reports it (UTC).

| Name | URL | HTTP | Items | Newest item (date, title) |
|---|---|---|---|---|
| Microsoft Fabric Updates Blog | https://community.fabric.microsoft.com/t5/s/rss/board?board.id=fbc_fabricupdatesblogs (via https://blog.fabric.microsoft.com/en-us/blog/feed/) | 200 (after redirect) | 20 | 2026-10-21, "Simplify Teradata migrations with Fabric Migration Assistant (Preview)" |
| Power BI Updates Blog | https://community.fabric.microsoft.com/t5/s/rss/board?board.id=fbc_pbiupdatesblog (via https://powerbi.microsoft.com/en-us/blog/feed/) | 200 (after redirect) | 20 | 2026-10-19, "Fabric Data Warehouse integration with Fabric User Data Functions (Preview)" |
| Microsoft Cloud Blog, Healthcare | https://www.microsoft.com/en-us/microsoft-cloud/blog/industry/healthcare/feed/ | 200 | 10 | 2026-09-30, "Accelerating human capacity across healthcare with AI" |
| Azure updates (filter "Fabric") | https://www.microsoft.com/releasecommunications/api/v2/azure/rss | 200 | 200 | 2026-10-20, "[In preview] Public Preview: Disable VNet peering route" |
| r/MicrosoftFabric top/week | https://www.reddit.com/r/MicrosoftFabric/top/.rss?t=week | 200 | 25 | 2026-10-20, "Anyone using the Microsoft Fabric MCP server? Seeing real productivity gains?" |
| r/PowerBI top/week | https://www.reddit.com/r/PowerBI/top/.rss?t=week | 200 | 25 | 2026-10-21, "Data Analyst skillset before vs now" |
| r/healthIT top/week | https://www.reddit.com/r/healthIT/top/.rss?t=week | 200 | 11 | 2026-10-21, "Greedy to ask about second Epic cert before starting first?" |
| Healthcare IT News (direct) | https://www.healthcareitnews.com/home/feed | **403** (Cloudflare) | n/a | n/a |
| Healthcare IT News via Google News | https://news.google.com/rss/search?q=site:healthcareitnews.com+when:7d&hl=en-US&gl=US&ceid=US:en | 200 | 33 | 2026-10-19, "Use of clinical AI for treatment planning spikes, MGB study shows" |
| Becker's Hospital Review (all topics) | https://www.beckershospitalreview.com/feed/ | 200 | 10 | 2026-10-21, "Only 1 medical school requires students to take national patient safety exam" |
| Becker's Health IT section (direct) | https://www.beckershospitalreview.com/healthcare-information-technology.feed | **403** | n/a | n/a |
| Becker's "health IT" via Google News | https://news.google.com/rss/search?q=site:beckershospitalreview.com+%22health+IT%22&hl=en-US&gl=US&ceid=US:en | 200 | 100 | 2026-10-21, "What Amazon pays for 12 health tech jobs, from $131K to $313K" |
| Fierce Healthcare (all) | https://www.fiercehealthcare.com/rss/xml | 200 | 25 | Oct 21, 2026 10:30am, "Baba nabs $40M series A, backed by FirstMark Capital and CVS Health Ventures…" |
| Fierce Healthcare health-tech section | https://www.fiercehealthcare.com/rss/health-tech/xml | 200 but **0 items** | 0 | n/a |
| YouTube: Microsoft Fabric | https://www.youtube.com/feeds/videos.xml?channel_id=UCH0gDiJ1RSn3kkxRQnQaH1w | 200 | 15 | 2026-10-15, "Microsoft's People Team (HR) Engineering Excellence with Fabric" |
| YouTube: Guy in a Cube | https://www.youtube.com/feeds/videos.xml?channel_id=UCFp1vaKzpfvoGai0vE5VJ0w | 200 | 15 | 2026-10-21, "How to Use Direct Lake Calculated Columns in Power BI" |
| YouTube: RADACAD (Reza Rad) | https://www.youtube.com/feeds/videos.xml?channel_id=UCsOfIwAXj1fT6LDqEDEAb4g | 200 | 15 | 2026-10-21, "Microsoft IQ Explained: Work IQ, Fabric IQ, Foundry IQ and Web IQ" |
| YouTube: SQLBI | https://www.youtube.com/feeds/videos.xml?channel_id=UCcc21gBGNJwZM_eDEByeN-Q | 200 | 15 | 2026-10-20, "Continuous axis for any Date table in Power BI" |
| YouTube: Learn Microsoft Fabric with Will | https://www.youtube.com/feeds/videos.xml?channel_id=UCrvoIYkzS-RvCEb0x7wfmwQ | 200 | 15 | 2026-10-19, "Applying top AI researcher's idea to agentic Fabric development" |
| YouTube: Microsoft Healthcare and Life Blog Videos | https://www.youtube.com/feeds/videos.xml?channel_id=UCFHGcKtofw8IQZRVFpTBjEw | 200 | 15 | 2026-07-24, "Publish Copilot Prompts to Your Whole Org in Minutes: Organizational Prompts" |
| Hacker News "Microsoft Fabric" | https://hnrss.org/newest?q=%22Microsoft+Fabric%22 | 200 | 20 | 2026-09-30, "Daxis – a cross-platform desktop editor for Microsoft Fabric semantic models" |
| SQLBI blog | https://www.sqlbi.com/feed/ | 200 | 30 | 2026-10-20, "Continuous axis for any Date table in Power BI" |
| Chris Webb's BI Blog | https://blog.crossjoin.co.uk/feed/ | 200 | 10 | 2026-10-18, "Monitoring The Impact Of Full-Text Indexing On Semantic Model Refresh In Power BI" |
| MS Learn "What's new in Fabric" | none found (Learn search RSS is relevance-based, not a changelog) | n/a | n/a | n/a |

---

## Sources

All accessed 2026-10-21. LinkedIn Help dates are approximate, counted back from the page's "Last updated N ago".

**LinkedIn (official)**
- Video sharing troubleshooting (specs), about 2024: https://www.linkedin.com/help/linkedin/answer/a548372
- Media file types supported on LinkedIn, about Sep 2026: https://www.linkedin.com/help/linkedin/answer/a564109
- Video specifications for Pages and Career Pages, about 2022: https://www.linkedin.com/help/linkedin/answer/a1311816
- Add Closed Captions to Videos on LinkedIn (SRT), about 2021: https://www.linkedin.com/help/linkedin/answer/a552177
- Auto captions for videos on LinkedIn, about late 2025: https://www.linkedin.com/help/linkedin/answer/a1327025
- Manage video autoplay settings, about Sep/Oct 2026: https://www.linkedin.com/help/linkedin/answer/a565326
- Full-screen vertical video on LinkedIn, about May 2026: https://www.linkedin.com/help/linkedin/answer/a6290168
- Video visibility and quality on LinkedIn, about Apr 2026: https://www.linkedin.com/help/linkedin/answer/a10728043
- Share photos on LinkedIn: https://www.linkedin.com/help/linkedin/answer/a527229
- Schedule posts: https://www.linkedin.com/help/linkedin/answer/a1347212
- How to pin a comment: https://www.linkedin.com/help/linkedin/answer/a16666203
- View your creator analytics: https://www.linkedin.com/help/linkedin/answer/a704175
- Video ads advertising specifications: https://www.linkedin.com/help/linkedin/answer/a424737
- Prohibited software and extensions, about 2024: https://www.linkedin.com/help/linkedin/answer/a1341387
- Spam, about 2024: https://www.linkedin.com/help/linkedin/answer/a1338787
- User Agreement, effective 2025-11-03: https://www.linkedin.com/legal/user-agreement
- Professional Community Policies: https://www.linkedin.com/legal/professional-community-policies
- LinkedIn Marketing Solutions, How to market on LinkedIn (undated): https://business.linkedin.com/advertise/ads/how-to-market-on-linkedin
- LinkedIn Marketing Solutions, Video Ads (undated): https://business.linkedin.com/advertise/ads/sponsored-content/video-ads
- LinkedIn Marketing Solutions, Video Ads specs (undated): https://business.linkedin.com/advertise/ads/sponsored-content/video-ads/specs
- LinkedIn Marketing Solutions, Video Ads best practices (undated): https://business.linkedin.com/advertise/ads/sponsored-content/video-ads/best-practices

**Press (secondary)**
- Engadget, 2024-03-29: https://www.engadget.com/linkedin-is-testing-a-tiktok-like-feed-for-vertical-video-233454044.html
- Digiday, 2025-01-31: https://digiday.com/media/linkedins-video-push-appears-to-be-working-in-2025/
- MediaPost (early 2025, date not extracted): https://www.mediapost.com/publications/article/403132/linkedin-takes-on-tiktok-with-new-vertical-video-f.html
- Social Media Today (early 2025, date not extracted): https://www.socialmediatoday.com/news/linkedin-video-presentation-discovery-updates/739214/

**Third-party data**
- Socialinsider, 2026 LinkedIn Benchmarks (includes Q3 2026): https://www.socialinsider.io/social-media-benchmarks/linkedin
- Buffer, How often to post on LinkedIn (2026): https://buffer.com/resources/how-often-to-post-on-linkedin/
- Buffer, How LinkedIn's algorithm works in 2026: https://buffer.com/resources/linkedin-algorithm/
- Van der Blom summaries (weak evidence): https://kokasexton.com/insights/richard-van-der-blom.html · https://podcast.creatorscience.com/richard-van-der-blom-2/
- Engagement-bait blogs (unverified claims): https://blog.hootsuite.com/linkedin-algorithm/ · https://www.socialpilot.co/blog/linkedin-algorithm · https://www.dataslayer.ai/blog/linkedin-algorithm-february-2026-whats-working-now · https://www.indiehackers.com/post/linkedin-engagement-bait-is-a-lead-gen-goldmine-if-youre-not-the-one-posting-it-UOuNrVQjbN3HqgZFXlML

**People and channels**
- https://www.youtube.com/@GuyInACube
- https://www.youtube.com/@RADACAD
- https://www.youtube.com/@FabricFrontiers
- https://www.youtube.com/@SQLBI
- https://blog.crossjoin.co.uk/
- https://www.linkedin.com/posts/arunulag_microsoft-launches-fabric-a-new-end-to-end-activity-7066833730736164864-Go1F (2023-05-23)
- https://www.linkedin.com/posts/microsoftfabric_introducing-healthcare-data-solutions-in-activity-7173331936147390464-jVj5 (2024-03-12)
- https://www.youtube.com/channel/UCH0gDiJ1RSn3kkxRQnQaH1w
- https://www.youtube.com/watch?v=l81yHEntd1w
- https://www.youtube.com/watch?v=SL54I15KtNg
- https://www.youtube.com/@microsofthealthcareandlife5580
- https://www.youtube.com/watch?v=QVpP8-pkx3E
- https://www.linkedin.com/posts/chesterkingeagleridge_set-up-a-connector-to-import-epic-ehr-data-activity-7102684195419787264-pW4W (2023-08-30)

**Feeds:** see the Verified feeds table above.
