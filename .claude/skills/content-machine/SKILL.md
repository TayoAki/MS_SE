---
name: content-machine
description: >-
  The 5-system short-form content machine: you only sit down and talk, the AI does the rest. System 1 finds the news and
  content ideas for YOUR niche (a scraper + web research), system 2 writes the scripts word for word in your voice (hook,
  value spread through the video, a comment-keyword call to action, your word blacklist), system 3 edits the recording
  (the free Persa Shorts editor: cuts, captions, cut-out, real pages, sound), system 4 makes the cover (one world, one scale
  trick, the same text style; your AI character on Higgsfield if connected) and system 5 posts it with Blotato at the times
  you pick, only after your OK. Use whenever the user says "scrape for me", asks for content ideas, scripts, a reel/short
  edit, a cover/thumbnail, to post or schedule content, to plan their content day/week, or to set up / change their
  content profile, voice or blacklist.
---

# The content machine — 5 systems, one skill

The user records for ~20 minutes a day. Everything before and after that is yours: **ideas → scripts → (they record) →
edit → cover → post.** Each system has its own guide in `systems/`; read the one you are running, every time.

| # | System | They say | Guide |
|---|---|---|---|
| 1 | The news / ideas | "scrape for me", "give me ideas" | `systems/1-news/NEWS.md` |
| 2 | The script | "write the scripts", "script 3 and 5" | `systems/2-script/SCRIPT.md` |
| 3 | The editor | "edit this" + a recording | `systems/3-editor/EDITOR.md` |
| 4 | The cover | "make the cover(s)" | `systems/4-cover/COVER.md` |
| 5 | Posting | "post them", "schedule this week" | `systems/5-post/POST.md` |

Workspace (one folder for everything): `~/content-machine/`
```
profile.md / profile.json   who they are (written at onboarding, edited any time)
voice/                      their recordings / transcripts + voice.md (how they talk) + blacklist.md (words they never say)
ideas/                      raw-<date>.json (scraper) · ideas-<date>.md (the list they pick from) · seen.json
scripts/<date>-<nn>-<slug>/ SCRIPT.md (+ the free file they DM) — one folder per script
recordings/                 their takes (any format)
edits/  covers/             finished shorts and covers
posted.json                 what went out, where, when (system 5)
NOTES.md                    every note they give → a rule (see "Notes become rules")
```

## Step 0 — onboarding (first run, or when ~/content-machine/profile.md is missing)
Ask these as ONE short numbered list, give an example answer for each, then WAIT. Never guess.
1. **Who are you?** Name, what you're known for, your @handle(s).
2. **What do you do?** Your business / offer, and what you want content to bring you (clients, followers, sales, trust).
3. **Who are you talking to?** Your viewer in one sentence (e.g. "people scared of the dentist", "non-technical founders").
4. **Your niche keywords + where your people hang out** (subreddits, blogs, YouTube channels, news sites you read).
   Tech niches: also GitHub / Hacker News topics.
5. **Platforms and posting times** (Instagram, TikTok, Facebook, YouTube Shorts…; e.g. 9:00 · 13:00 · 18:00) and how many
   videos a day (start with 1).
6. **Language** of the videos, and **3–5 recordings or transcripts of you talking naturally** (calls, videos, voice notes)
   so the scripts sound like you — they can add these later in `~/content-machine/voice/`.
7. **Words you never say** (the start of your blacklist) and your usual call to action (e.g. "comment WORD and I'll send
   you…", "follow for more", "book a call").

Then write `~/content-machine/profile.md` (their answers in plain words) and `~/content-machine/profile.json` from
`templates/profile.json` (niche, platforms, times, language, and the scraper `sources` you derive from answer 4 — real
subreddit names, real RSS feed URLs you verified with a fetch). Create the folders above. Tell them it's saved and what
to say next: **"scrape for me"**.

## The day (what "do my content day" means)
1. System 1 → an idea list; **they pick**. 2. System 2 → one script per pick; **they read and approve** (fix any line that
doesn't sound like them; save the fix as a rule). 3. They record all scripts in one go — if they mess up a line they just
say it again; the editor cuts it. 4. System 3 edits every take. 5. System 4 makes each cover. 6. System 5 shows them every
post (video, cover, caption, hashtags, time, platforms) → **only on their explicit yes** it schedules them.

## Rules that hold everywhere
- **Nothing is published, posted, scheduled, sent or uploaded without the user's explicit OK** for that exact item.
- **Real facts only.** Every number and claim in a script has a source link (a fact table in SCRIPT.md); if you can't
  verify it, cut it or mark it. Never invent numbers, quotes, reviews, results or screenshots.
- **Their voice, not yours.** Scripts are checked against `voice/voice.md` and `voice/blacklist.md` every time.
- **No emojis on screen**, nothing on screen they didn't say (the editor enforces this too).
- **Free by default.** Paid things (Higgsfield credits, Blotato plan) are optional and always named before use.
- Use the strongest model for this skill (Claude Code: `/model` → Opus). It is a big job.

## Notes become rules
Every time the user doesn't like something ("too long", "I never say that", "that cover is ugly"), fix it AND write it into
`~/content-machine/NOTES.md` as a dated rule (their words → the rule → which system). Read NOTES.md before running any
system. A word they reject goes straight into `voice/blacklist.md`. This is how the machine gets better every video.
