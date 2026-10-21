# System 2 — the script

Takes the ideas the user picked and writes each one word for word, ready to read on a teleprompter or from memory.
Read `~/content-machine/profile.md`, `~/content-machine/voice/voice.md`, `~/content-machine/voice/blacklist.md` (and this
folder's `blacklist.md` starter) and `~/content-machine/NOTES.md` before writing.

## The pattern (every script)
1. **Hook — the first 1–3 seconds.** One bold, concrete sentence that stops the scroll. The hook carries the whole context:
   no greeting, no "in this video", no setup paragraph. Write 3 hooks with 3 DIFFERENT feelings and opening shapes (a
   number, a change that just happened, a "you don't need X anymore", a "stop doing X", a surprising claim, a question
   they've asked themselves) and let the user pick.
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
## Hooks (pick one)   1. …  2. …  3. …
## Script             (the full spoken text, exactly as they'll say it)
## Facts              | claim | value | source link |   ← every number/claim; anything unverified is cut or flagged ⚠
## Cover text         <2–4 words from the script> (system 4)
## On screen          what to SHOW when they SAY… (real pages/apps to capture for system 3)
## The free thing     what people get for commenting → write it as DELIVERABLE.md in the same folder
## Caption draft      first line = the hook idea + the CTA; 3–5 hashtags (system 5 finalises)
```
Before showing a script: re-read it aloud in your head against voice.md, run the blacklist, check every fact has a link,
check the CTA keyword is new. Then show all scripts of the batch together and ask which to keep / change.
