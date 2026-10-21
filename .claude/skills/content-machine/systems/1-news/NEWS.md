# System 1 — the news (the scraper)

Goal: a short list of content ideas for THIS user's niche, each one real, recent or evergreen-proven, with its source —
they pick the ones they like and system 2 turns them into scripts. The hardest part of posting every day isn't the
editing, it's knowing what to talk about: this system removes that.

## 0 · Start from the plan, not from a blank page
**Recreate first.** While the channel is new, the week's ideas start with `~/content-machine/recreate-list.md`: posts that
already beat their channel's normal, recreated in our words with checked facts (scripts in `docs/reels/`). Calendar
topics fill the rest. A pasted transcript of a winner → map its beats and rewrite every line (never reuse its words).
Read `~/content-machine/calendar/linkedin-video-plan.md` (this week's row: topic, type, pillar, freebie), `pillars.md`,
`icp.md` (the pains and words), `swipe/swipe.md` (shapes that worked), `audience-questions.md` (what people asked) and
`NOTES.md`. The week's three videos — A reach, B authority, C offer — come first; the news and research below sharpen
them and fill the spare slots. Trend weeks: pick a verified change from the last 7–14 days (step 1–2); none relevant → a
current-state retest. LinkedIn itself is never scraped: public posts found through web search can be opened and read one
by one; good ones go into the swipe file by hand.

## 1 · Scrape what just happened (free sources, no keys)
```bash
node ~/.claude/skills/content-machine/systems/1-news/scrape.mjs --profile ~/content-machine/profile.json --days 7
```
Reads `profile.json → sources` (subreddits + Reddit searches, Hacker News and GitHub topics for tech niches, any RSS/Atom
feeds: blogs, news sites, YouTube channels via `https://www.youtube.com/feeds/videos.xml?channel_id=<id>`), keeps only what's
new since last time (`ideas/seen.json`) and writes `ideas/raw-<date>.json` with every find's link and numbers.
- A source that fails is listed as `failed (skipped)` — Reddit rate-limits bursts: wait a few minutes, or open the
  subreddit with your own web fetch instead. X/Twitter has no free feed: use web search for "<topic> site:x.com" if the
  user's niche lives there.
- A free `GITHUB_TOKEN` in the environment raises GitHub's limit (tech niches only).

## 2 · Research the niche (web search — this is what makes it work for ANY niche)
Run web searches for the user's niche and audience (profile.md) in these angles, and read the best results:
1. **What just changed** — news, launches, new rules/laws/prices, studies, trends this week.
2. **The questions people actually ask** — "people also ask", forums, the subreddit threads from step 1, Quora.
3. **The most common problems / procedures** in the niche (a dentist: the most common teeth problems, the most common
   surgeries; a coach: the most common mistakes).
4. **The taboo things** — what professionals in the niche know but rarely say out loud; myths worth busting.
5. **Free things to give away** — a checklist, a template, a tool, a prompt the viewer can get by commenting.
Keep the link of everything you use.

## 3 · Write the idea list → `ideas/ideas-<date>.md`
10–20 ideas, best first, each as:
```
## 7 · <the idea in plain words>                         angle: questions | problem | taboo | news | myth | free-thing
- Funnel: reach | authority | offer · Pillar: P1–P5 · Calendar: week <n> video A|B|C (or "spare")
- The specific problem: <one sentence a viewer could say happened to them — not a topic> · evidence: <community ID, ICP quote, thread>
- The proof we can show: <the synthetic demo, test, real page or story that resolves it — the gap analysis's rule>
- Draft hook: <one line in a HOOKS.md shape>; system 2 sharpens it
- Hook shape: <a swipe row it borrows its shape from, if any>
- Story / proof: <the story-bank entry or lab result an authority/offer idea stands on — none yet? say so, don't invent>
- Why it works: <one line: who it helps (a role from icp.md), why now>
- Source(s): <links>
- The free thing to DM (if any): <what they'd send people who comment>
- Format: short (≈30 s) | list (≈50 s) | story / opinion
```
Rules: no idea without a real source; never repeat an idea already in `ideas/seen-ideas.md` (append every idea you show);
mix the angles (not 10 news items); match the profile's audience and goals; the list opens with this week's A/B/C from
the calendar; every idea has a funnel job and a pillar; an authority idea with no story or lab result behind it is
flagged, not padded. Then ask: **"Which ones do you want? (numbers)"**
and hand the picks to system 2.
