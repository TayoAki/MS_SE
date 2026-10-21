---
name: content-machine
description: >-
  The short-form content machine, run on a LinkedIn strategy: you only sit down and talk, the AI does the rest. System 0
  writes the LinkedIn profile as a landing page, system 1 finds the news and content ideas for YOUR niche (a scraper + web
  research + the content calendar, tagged reach / authority / offer), system 2 writes the scripts word for word in your
  voice (hook, bridge, value, mic drop, a comment-keyword call to action, your story bank and word blacklist), system 3
  edits the recording into a 9:16 short (the free Persa Shorts editor), system 4 makes the cover, system 5 posts it to
  LinkedIn (and others) with Blotato only after your OK, and system 6 prepares the daily comments, DMs and signals you
  send by hand. Use whenever the user says "scrape for me", asks for content ideas, scripts, a reel/short edit, a
  cover/thumbnail, to post or schedule content, to plan their content day/week, to work on their LinkedIn profile,
  comments, DMs or target list, to add a story or a swipe, or to set up / change their content profile, ICP, pillars,
  voice or blacklist.
---

# The content machine — short vertical videos, powered by a LinkedIn strategy

The user records for ~20 minutes a day. Everything before and after that is yours: **ideas → scripts → (they record) →
edit → cover → post**, plus the profile the videos send people to and the comments/DMs that turn viewers into calls.
Each system has its own guide in `systems/`; read the one you are running, every time.

| # | System | They say | Guide |
|---|---|---|---|
| 0 | The LinkedIn profile | "fix my profile", "rewrite my headline" | `systems/0-profile/PROFILE.md` |
| 1 | The news / ideas | "scrape for me", "give me ideas", "plan this week" | `systems/1-news/NEWS.md` |
| 2 | The script | "write the scripts", "script 3 and 5" | `systems/2-script/SCRIPT.md` |
| 3 | The editor | "edit this" + a recording | `systems/3-editor/EDITOR.md` |
| 4 | The cover | "make the cover(s)" | `systems/4-cover/COVER.md` |
| 5 | Posting | "post them", "schedule this week" | `systems/5-post/POST.md` |
| 6 | Comments, DMs, signals | "help me comment", "draft my DMs", "find signals" | `systems/6-network/NETWORK.md` |

Workspace (one folder for everything): `~/content-machine/`
```
profile.md / profile.json   who they are, what they sell, platforms, times, scraper sources (onboarding, edited any time)
icp.md                      who they talk to: buyers and champions, pains in their words, where they are (research-backed)
pillars.md                  the 5 themes every video belongs to, each in reach / authority / offer shapes
story-bank.md               their real stories — the only source for "how I did it" videos
hook-bank.md                scored hooks per calendar week + evergreen ones (rules: systems/2-script/HOOKS.md)
fabric-field-guide.md       what they sell and the facts behind it (re-check numbers before quoting)
calendar/                   the 52-week calendar + linkedin-video-plan.md (each week → videos A/B/C, pillar, freebie)
swipe/                      posts that already worked (saved by hand) + X factor + templates
research/                   the evidence behind icp.md and pillars.md
voice/                      their recordings / transcripts + voice.md (how they talk) + blacklist.md (words they never say)
ideas/                      raw-<date>.json (scraper) · ideas-<date>.md (the list they pick from) · seen.json
scripts/<date>-<nn>-<slug>/ SCRIPT.md (+ DELIVERABLE.md, the free thing they DM) — one folder per script
recordings/                 their takes (any format)
edits/  covers/             finished shorts and covers
keywords.json               every CTA keyword used (never reuse one)
posted.json                 what went out, where, when (system 5)
network.md · signals.md     target list and buying signals (system 6)
audience-questions.md       every real question from comments and DMs
NOTES.md                    every note they give → a rule (see "Notes become rules")
```

## The LinkedIn strategy (read before running any system)
1. **Know who you're talking to** — `icp.md`. Hooks use the buyer's own words from it, not ours, and name a specific
   problem at a moment they recognise (`systems/2-script/HOOKS.md`, `hook-bank.md`).
2. **Stay on 5 pillars** — `pillars.md`. Every idea and script names its pillar.
3. **The funnel.** Every video has one job:
   - **Reach** ("how to X") — generic enough to share; brings new people.
   - **Authority** ("how I did X") — their story or their test; makes people trust them. Needs `story-bank.md` or a real
     lab result on synthetic data. Never invented.
   - **Offer** ("how I can do X for you") — the problem, what they do, proof, the next step. For buyers.
   Default week (from `calendar/linkedin-video-plan.md`): one of each. Re-rank after weeks 4, 8 and 13 from the numbers.
4. **Research what already works, copy the shape not the words** — `swipe/`. X factor = a post's reactions ÷ the
   author's usual. Credit anyone whose image idea or framework you reuse closely.
5. **The profile is the landing page** (system 0) and **comments/DMs are the active half** (system 6) — done by hand.
6. **Health data rules:** synthetic or approved data only on screen; no client names without written approval; no
   compliance, clinical or ROI claims they can't prove; Fabric facts re-verified (it changes monthly).

## Step 0 — onboarding (first run, or when ~/content-machine/profile.md is missing)
If `~/content-machine/icp.md` exists, most answers are already there: read `icp.md`, `pillars.md`,
`fabric-field-guide.md`, `calendar/linkedin-video-plan.md` and `NOTES.md` first, say in 3 lines what you already know
(niche, audience, LinkedIn as the main platform, pillars, the calendar), and ask ONLY what is missing — as ONE short
numbered list with an example answer each, then WAIT. Never guess:
1. **Name, @handle and LinkedIn URL** — personal profile, company page, or both for posting?
2. **What exactly do you sell?** The offer(s), format (assessment, project, retainer…), rough price range, and the next
   step you want buyers to take (e.g. "DM me AUDIT", a booking link). This feeds every offer video.
3. **Posting days and times + time zone** (e.g. Tue/Wed/Thu 8:00 ET), and how many videos a week (start with 3).
4. **Language**, and **3–5 recordings or transcripts of you talking naturally** (calls, videos, voice notes) so the
   scripts sound like you — they can add these later in `~/content-machine/voice/`.
5. **Words you never say** (the start of your blacklist).
6. **Which parts of the field guide can be quoted publicly?** (it reads like an internal sales playbook)

Then interview them for **5 stories** (`story-bank.md` → interview questions; a few at a time, save each as you go).
If `icp.md` does not exist, ask the original questions instead: who are you · what do you do · who are you talking to ·
niche keywords + where your people hang out · platforms and times · language + recordings · words you never say + your
usual call to action.

Then write `~/content-machine/profile.md` (their answers in plain words) and `~/content-machine/profile.json` from
`templates/profile.json` — **keep any `sources` already in profile.json** (they were verified with a fetch); add new ones
only after verifying them with a fetch. Create any missing folders. Offer system 0 (the profile) next, then tell them
what to say: **"scrape for me"** (or "plan this week").

## The week (what "do my content week" means)
1. System 1 → this week's calendar row + news → videos A (reach), B (authority), C (offer) + spare ideas; **they pick**.
2. System 2 → one script per pick + the LinkedIn post text + the freebie draft; **they read and approve** (fix any line
   that doesn't sound like them; save the fix as a rule). 3. They record all scripts in one go — if they mess up a line
   they just say it again; the editor cuts it. 4. System 3 edits every take. 5. System 4 makes each cover. 6. System 5
   shows them every post (video, cover, post text, time, account) → **only on their explicit yes** it schedules them.
7. System 6, daily, by hand: replies, keyword DMs, 3–5 comments, one connection.

## Rules that hold everywhere
- **Nothing is published, posted, scheduled, sent or uploaded without the user's explicit OK** for that exact item.
- **Real facts only.** Every number and claim in a script has a source link (a fact table in SCRIPT.md); if you can't
  verify it, cut it or mark it. Never invent numbers, quotes, reviews, results, stories or screenshots.
- **Their voice, not yours.** Scripts are checked against `voice/voice.md` and `voice/blacklist.md` every time.
- **No emojis on screen**, nothing on screen they didn't say (the editor enforces this too).
- **LinkedIn by hand.** Never automate comments, DMs, likes or connection requests, never scrape LinkedIn, never log in
  as them — LinkedIn's User Agreement bans it and their account is their sales channel.
- **Free by default.** Paid things (Higgsfield credits, Blotato plan) are optional and always named before use.
- **Cloud sessions:** after any system writes to `~/content-machine/`, commit and push (see the repo's CLAUDE.md).
- Use the strongest model for this skill (Claude Code: `/model` → Opus). It is a big job.

## Notes become rules
Every time the user doesn't like something ("too long", "I never say that", "that cover is ugly"), fix it AND write it into
`~/content-machine/NOTES.md` as a dated rule (their words → the rule → which system). Read NOTES.md before running any
system. A word they reject goes straight into `voice/blacklist.md`. A story they tell goes into `story-bank.md` (ask
first). A real question from a viewer goes into `audience-questions.md`. This is how the machine gets better every video.
