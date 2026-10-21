# System 1 — the news (the scraper)

Goal: a short list of content ideas for THIS user's niche, each one real, recent or evergreen-proven, with its source —
they pick the ones they like and system 2 turns them into scripts. The hardest part of posting every day isn't the
editing, it's knowing what to talk about: this system removes that.

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
- Why it works: <one line: who it helps, why now>
- Source(s): <links>
- The free thing to DM (if any): <what they'd send people who comment>
- Format: short (≈30 s) | list (≈50 s) | story / opinion
```
Rules: no idea without a real source; never repeat an idea already in `ideas/seen-ideas.md` (append every idea you show);
mix the angles (not 10 news items); match the profile's audience and goals. Then ask: **"Which ones do you want? (numbers)"**
and hand the picks to system 2.
