# NextPhase · Persa Shorts — a free Claude Code skill

Turn a vertical talking-head recording into a finished **9:16 short** (Reels, TikTok, YouTube
Shorts) in the **persa** look:

- **The camera is the frame.** Your take runs full-bleed; everything is composited INTO it.
- **One-word captions** that hard-cut on and off on a single line, at the same spot all video.
- **Big display words with your head in front of them** — your cut-out is painted back over the
  type, so the words read as written behind you.
- **Real apps and screen recordings own the frame** while you drop into a rounded camera card
  at the bottom, your head breaking its top edge.
- **A warm film grade** — optional; "clean natural" is one answer away.
- Your colours, fonts, look and niche. Free, local, no watermark.

## What you need
- **Claude Code** (any plan).
- A Mac or Linux computer (Windows works through WSL).
- Free tools the setup checks for you: Node.js 22+, ffmpeg, Python 3.9+. The renderer
  (HyperFrames, open source) runs through `npx` — nothing to sign up for.
- About 1 GB of disk for the tools and models (more if you pick the "best" cut-out).

## Install in 3 steps
1. **Download** `NextPhase-Persa-Shorts.zip` and leave it in your Downloads folder.
2. **Open Claude Code** in any folder, paste everything in `SETUP-PROMPT.txt`, press Enter.
   Claude installs the skill, checks the tools, asks you 9 quick questions (colours, dark or bright,
   fonts, film grade, niche, how much research it should do, how many tokens to spend, sound,
   cut-out), saves your brand and renders an 8-second preview in your style.
3. **Start a new Claude Code session** so the skill loads.

## How to use it
Record vertically, then say something like:
> "Edit ~/Desktop/take.mov as a persa short. The product is <your app/site>, here's my screen
> recording: ~/Desktop/demo.mov."

Claude transcribes it, checks the facts (as deeply as you chose), finds or asks for the real
screenshots and clips, shows you the beat plan, builds it, renders it, looks at the frames, adds
the sound pass, and opens the finished file for you. It never posts anything.

Other things to ask:
- "Switch my persa colours to green and the bright look, then show me the preview."
- "Set research to 2 and budget to lean."
- "Re-cut the hook — put the payoff word on 'free'."

## The one thing this style needs: a real demo
Persa is built around **~15 seconds of a real product, app, website or process on screen** — a
screen recording that keeps moving while you talk. If your script has nothing to show, Claude
will tell you before it builds and offer options. Two recording tips:
- **Sit a little further back**, with room above your head (your head ≈ 15% of the frame height).
- **Record your screen** while you use the thing you talk about. That recording is the spine.

## What's included
- `skill/nextphase-persa-shorts/` — the skill: the method (measured style rules, the 13 display
  type roles, the blacklist of things that get cuts rejected), the engine that turns a beat map
  into a HyperFrames composition, and every script (transcribe with a dropped-speech check,
  cut-out + head measuring, film grade, page shots, density gate, contact sheets, sound mix).
- A royalty-free sound palette, **synthesised in code** on your machine at setup.

## What's NOT included (on purpose)
- **No music.** A licence to use a track is not a licence to redistribute it. Turn music on and
  point it at a track you own or have licensed.
- **No third-party sound packs, logos, screenshots, mascots or footage.** Your videos use real
  surfaces of the products YOU talk about, captured fresh.
- **No fonts files** — the fonts are free Google Fonts, loaded at render time.

See `LICENSE-NOTES.md` for the details.
