# System 3 — the editor (short form, 9:16)

The edit is done by the free **Persa Shorts** skill (`nextphase-persa-shorts`), shipped inside this kit in
`systems/3-editor/NextPhase-Persa-Shorts/skill/nextphase-persa-shorts/` and installed as its own skill by the install prompt (it has its own setup,
brand questions and 8-second preview). It cuts the mistakes, restarts and long pauses, cuts you out of the background so
you pop out on top of the graphics, puts the real pages/apps you talk about on screen, does word-by-word captions, an
optional film grade and sound effects — and every note you give it is saved so it never makes that mistake again.

## How to run it from the machine
1. The recording: `~/content-machine/recordings/<file>` (one take per script; it's fine to repeat lines — the editor
   keeps the last clean take).
2. Hand it the script from system 2 (`scripts/<…>/SCRIPT.md`: the spoken text, the facts table with links, and the
   "On screen" list of real pages to capture) so it knows the intended words and what to show. Pictures for that list
   come from `systems/3-editor/BROLL.md`: the allowed sources in order, the tools that find them, and the credits.
3. Say: **"Edit ~/content-machine/recordings/<file> with nextphase-persa-shorts, script: <path to SCRIPT.md>"** — or let
   this skill call it the same way. Edit 2–3 recordings in parallel sessions if the computer can take it.
4. The finished short goes to `~/content-machine/edits/<date>-<nn>-<slug>.mp4`; LOOK at its contact sheet before saying
   it's done.

If `nextphase-persa-shorts` isn't installed (`~/.claude/skills/nextphase-persa-shorts/SKILL.md` missing), follow
`systems/3-editor/NextPhase-Persa-Shorts/SETUP-PROMPT.txt` steps 2–6 (the source folder is the one above) (the install prompt of this kit already does it).
Notes on an edit go into that skill's own notes AND `~/content-machine/NOTES.md`.
