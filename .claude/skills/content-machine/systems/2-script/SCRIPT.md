# System 2 — the script

Takes the ideas the user picked and writes each one word for word, ready to read on a teleprompter or from memory.
Read `~/content-machine/profile.md`, `~/content-machine/voice/voice.md`, `~/content-machine/voice/blacklist.md` (and this
folder's `blacklist.md` starter) and `~/content-machine/NOTES.md` before writing — plus `icp.md` (hooks in the buyer's own
words), `hook-bank.md`, `pillars.md`, `story-bank.md`, `swipe/swipe.md` and `fabric-field-guide.md` (re-verify any number you take from it).

## The LinkedIn beats, spoken (every script)
The structure that works in LinkedIn posts, said out loud in a 9:16 video:
**hook (1–3 s) → bridge (the pain or the story, 5–10 s) → meat (the value, in steps) → mic drop (one contrast line:
"we over-invest in X, we neglect Y") → call to action.** By funnel job:
- **Reach:** a how-to, a mistake, a myth. Generic enough to share. CTA: the week's freebie keyword.
- **Authority:** "how I did it" — one `story-bank.md` story or one lab/test on synthetic data, with what they did and what
  changed. No story yet for this topic? Ask for one, or make it a lab ("I tested it"); never invent a client or a result.
- **Offer:** the problem in the buyer's words → what they do about it → proof (a story with approval, or anonymised) →
  the next step from `profile.md` (e.g. "DM me AUDIT"). No freebie, no hype.
A swipe row can lend its shape (beat order, hook pattern, length) — never its words.

## The pattern (every script)
1. **Hook — the first 1–3 seconds.** Read `HOOKS.md` first, every time. One concrete sentence that names a specific
   problem the viewer has had, at a moment they recognise, with a consequence — problem before product, ≤ 12 words to the
   tension. No greeting, no "in this video", no setup paragraph. Write 3 hooks in 3 DIFFERENT shapes from HOOKS.md (e.g.
   succeeded-and-still-wrong, two numbers, the scene, the question you can't answer, stop doing X), each with its
   on-screen fragment (3–6 words) and its scorecard (6 checks). Show only hooks scoring 5–6; let the user pick.
2. **The value — spread through the whole video, not dumped in the first seconds.** If everything is given away at the
   start, people get what they came for and swipe. Reveal the name/answer after the hook, then give the payoff in steps,
   keeping the best bit for late.
3. **The call to action — at the end, always.** Usually: "comment <WORD> and I'll send you <the free thing>". The free
   thing is real (a checklist, prompt, template, link). A video that gives everything away with nothing to come back for
   gets watched, maybe liked, and forgotten: no follow, no subscribe. One keyword per video, never reused
   (`~/content-machine/keywords.json` is the ledger).

Length: short ≈ 100–150 words (≈ 30–40 s) for one idea; list ≈ 190–210 words (≈ 50 s) only when there are 4–5 real items.
Words ÷ speaking pace (≈ 180–230 words/min — measure it from their recordings) = seconds. Mix lengths across a day.

## Sounding like them, not like AI
- **Voice:** build `voice/voice.md` from their recordings/transcripts (`voice/` folder): the words they use often, how
  they start and end sentences, their fillers and phrases, their pace, what they never do. If they dropped audio/video,
  transcribe it (faster-whisper / whisper.cpp / the editor's transcriber) and keep the transcript in `voice/`.
- **Every line that doesn't sound like them → they tell you → you rewrite it → the lesson goes into voice.md.** It gets
  closer to them every script.
- **Blacklist:** never use a word or construction from `voice/blacklist.md` (theirs) or `blacklist.md` (the starter list
  in this folder). A word they reject is added the same minute.
- Plain words, short sentences, spoken rhythm. No markdown, no emojis, no hashtags inside the script.

## Output — `~/content-machine/scripts/<date>-<nn>-<slug>/SCRIPT.md`
```
# <title>
keyword: <WORD> · format: short|list · <words> words · ≈ <seconds> s
funnel: reach|authority|offer · pillar: P1–P5 · calendar: week <n> video A|B|C · story: <story-bank title or "lab">
## Beats             hook → bridge → meat → mic drop → CTA, one line each (the skeleton, before the full text)
## Hooks (pick one)   1. "<spoken>" · on screen: <3–6 words> · shape: <HOOKS.md shape> · score: <n>/6 · numbers from: <fact|story|demo>
                     2. …  3. …
## Script             (the full spoken text, exactly as they'll say it)
## Facts              | claim | value | source link |   ← every number/claim; anything unverified is cut or flagged ⚠
## Cover text         <2–4 words from the script> (system 4)
## On screen          what to SHOW when they SAY… (real pages/apps to capture for system 3)
## The free thing     what people get for commenting → write it as DELIVERABLE.md in the same folder
## LinkedIn post      the text that sits above the video (system 5 posts it as written):
                     lines 1–2 = the hook in words (all that shows before "…more"; it must work on its own) →
                     3–6 short lines of value or the story's turn → the mic drop → the CTA line (same keyword) →
                     at most 3 relevant hashtags. Under 3,000 characters. No emojis unless their own style uses them.
```
Before showing a script: re-read it aloud in your head against voice.md, run the blacklist, check every fact has a link,
check the CTA keyword is new. Then show all scripts of the batch together and ask which to keep / change.
