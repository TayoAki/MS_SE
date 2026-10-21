# System 4 — the cover (reel thumbnail)

On reels the cover is what people see on your profile, so it matters. Every cover is **3 things: one world, one scale
trick, and the same text style, every single time.** The world changes every post (you next to a giant city, inside a
museum, in a supermarket — everything around you going crazy: a crowd, a flood, people jumping) while YOU stay calm,
standing there, looking at the camera. That contrast stops the scroll. The text never changes (same layout, same colours),
so the grid looks creative but still reads as one brand. The words come straight from the script (`## Cover text`).

## The recipe
1. **The world = a metaphor for the script's claim**, and an EVENT, not a location. Push one thing to an extreme:
   colossal scale (you a giant over a miniature city, or tiny beside an everyday object) · being inside an object (a
   phone screen, a washing machine, a cereal bowl) · a material swap (clay, paper-craft, LEGO, oil paint) · weather / an
   event (a flood of paper, a blizzard, a crowd mid-jump) · a borrowed genre (a 90s soda ad, a film noir, a nature doc).
   Test: with all the text removed, would the image still stop you? If not, push harder.
2. **You are the still point.** Calm, neutral, arms loose, looking straight down the lens. The energy lives in the world
   and the crowd, never in your face. Natural 50 mm look — no fisheye, no warped face.
3. **The text block (locked — design it ONCE in onboarding, then never change it):** top of the frame, one left-aligned
   block, very large: line 1 = the tool/topic in your ONE accent colour, then the use-case word in white, repeated 2–3
   times fading (100 % → 50 % → 20 %). The text sits BEHIND your head (your hair/shoulders cover part of the lower lines).
   Save the exact spec in `~/content-machine/profile.md → Cover style`.
4. **A named tool or brand → its real logo as a physical object in the scene** (held in the hand, embossed on a prop, a lit
   emblem in the light), never a flat sticker. No invented branding, prices or handles — check every render for fake text.
5. **9:16, text away from the edges** so the 4:5 profile grid never cuts it off. Exposure: alternate bright and dark worlds
   so the grid doesn't go monotone. One accent colour only.

## Making it
- **With Higgsfield connected (Claude → Settings → Connectors) — recommended:** create your AI character ONCE from 10–20
  photos of you (Higgsfield's character / Soul ID / reference element), so you never need a photo shoot. For each cover:
  generate **3–4 versions** (a strong image model with good text, e.g. GPT Image or Nano Banana Pro, 9:16) with your
  character's reference + the world + the text block spec; the user picks one. It uses Higgsfield credits — say how many
  before generating, and never re-roll without asking.
- **Without Higgsfield:** any image model the user has, or a real photo of them cut out and placed into a generated world;
  the same recipe applies. Or make the cover from a frame of the edit with the locked text block on top.
- Save to `~/content-machine/covers/<date>-<nn>-<slug>.png`, next to the edit.
