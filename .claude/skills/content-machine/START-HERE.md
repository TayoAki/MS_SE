# Content Machine — 5 systems, one free Claude Code skill

You sit down and talk for ~20 minutes. The AI does everything else:

1. **The news** — scrapes your niche (Reddit, blogs and news feeds, YouTube channels; GitHub and Hacker News for tech) and
   researches it on the web (what just changed, the questions people ask, the most common problems, the taboo things),
   then gives you a list of content ideas. You pick the ones you like.
2. **The script** — writes each idea word for word: a hook that stops the scroll, the value spread through the whole video,
   a "comment WORD and I'll send you…" call to action at the end. It learns how you talk from your own recordings and
   never uses the words on your blacklist. Every fact comes with its source.
3. **The editor** — the free Persa Shorts editor (included): cuts your mistakes, restarts and pauses, cuts you out of the
   background, puts the real pages on screen, word-by-word captions, sound effects, your colours.
4. **The cover** — one world, one scale trick, the same text style every time; you (or your AI character on Higgsfield) calm
   in the middle of something crazy. 3–4 versions, you pick one.
5. **Posting** — Blotato inside Claude writes the caption and hashtags and schedules Instagram / TikTok / Facebook at your
   times. Nothing goes out without your OK.

## Install (about 10 minutes)
1. Download the zip and leave it in your Downloads folder.
2. Open Claude Code in any folder, paste everything in `SETUP-PROMPT.txt`, press Enter.
3. In Claude: Settings → Connectors → add **Blotato** (posting) and, if you want your own character on the covers,
   **Higgsfield**.
4. Start a new Claude Code session, type `/model` and pick Opus, then say **"scrape for me"**. The first time, it asks who
   you are, what you do and who you're talking to.

## Tips
- Start with 1 video a day, not 7. Get the system working, then go up.
- Record all your scripts in one go. Mess up a line? Just say it again — the editor cuts it.
- Every time you don't like something, tell Claude and tell it to save it: it becomes a rule and never happens again.
- Read your script before you record and make sure every fact is right — it's your name on the video.

## What's free / what's not
Free: this skill, the scraper (public sources), the script system, the Persa Shorts editor (open-source renderer).
Optional, paid: Blotato (posting; free trial), Higgsfield credits (AI character covers). Claude Code itself needs a Claude
plan. See `systems/3-editor/NextPhase-Persa-Shorts/LICENSE-NOTES.md` for the editor's licences.
