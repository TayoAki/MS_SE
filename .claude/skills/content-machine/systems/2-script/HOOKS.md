# Hooks — name a specific problem, at a specific moment, with a consequence

The hook is the first 1–3 seconds: the spoken line, the words on screen, and the first frame. On LinkedIn the video can
autoplay without sound and the first frame is the thumbnail, so the on-screen words must work alone.

## Why hooks go weak (diagnose before rewriting)
A weak hook names a **topic** ("healthcare data solutions in Fabric", "capacity planning", "data governance"). A strong
hook names a **problem the viewer has had**, in a **moment they recognise**, with a **consequence**, and leaves one
question open that the video answers. The 2026 gap analysis (`research/fabric-content-gap-analysis.html`) found the
same thing for whole videos: generic tutorials overlap heavily; what earns attention is "a better-supported decision or a
specific unresolved task — not simply a topic people ask about."

Common failures:
- **Topic-first / product-first:** the first words are a product name ("Healthcare data solutions in Microsoft Fabric…").
  Product names are long and the viewer doesn't feel anything yet. Put the problem first, the product later.
- **Conditional opener:** "If you use X…" spends the first second filtering people out. Name the moment instead; the
  right people recognise themselves.
- **No consequence:** a date, a feature, a change — but nothing happens to anyone. Who gets the call? What breaks? What
  does it cost? Who is embarrassed in front of whom?
- **Abstract nouns:** "trust", "governance", "transformation", "visibility". Replace with the concrete thing: a census
  number, a refresh that ran green, an auditor's question, an invoice line.
- **Answerable with "no":** "Do you use Fabric?" "Did you know…?" — they say no and swipe.
- **Too long:** more than ~12 spoken words before the tension lands (~3–4 s).

## The specificity ladder — climb to the top rung
| Rung | Example |
|---|---|
| Topic | data quality in healthcare dashboards |
| Problem | dashboards disagree |
| Specific problem | two dashboards show different patient counts |
| **Specific moment + number + consequence** | "Your census says 412 patients. Finance says 398. The CFO wants one number by 9." |

Concrete beats abstract (the "concrete" principle of Heath & Heath, *Made to Stick*, 2007). A precise number reads as
more credible than a round one (UCLA research co-written by Danny Oppenheimer; Berkeley Haas CMR summary, 2024) — but if
a precise number turns out wrong it costs more trust, so every number must be real.

## Where the numbers in a hook come from (the only three places)
1. **A sourced fact** in the script's Facts table (e.g. "more than 12,000 reports each month" — CentraCare, Chartis).
2. **The creator's own story** in `story-bank.md`, as they remember it ("about four hours", not an invented 4h 12m).
3. **The synthetic demo shown in the same video** — the numbers the viewer will see on screen ("412 vs 398" only if the
   demo dataset actually produces 412 and 398). Mark these `[from demo]` until the demo is run.
Never a made-up statistic, never "studies show".

## The open loop
Curiosity comes from a gap in knowledge that the viewer can feel (Loewenstein, "The Psychology of Curiosity", 1994):
they must already know enough to notice what's missing. So: state the part they recognise, withhold the why or the fix,
and pay it off later in the video — not in the first seconds (see SCRIPT.md: value spread through the video). Then
**re-hook** once in the middle ("but that's not the part that breaks it") — the hook-and-rehook structure short-form
creators like Kane Kallaway describe. The hook's promise must match what the video delivers; a bait hook burns trust
with exactly the people you're selling to.

## Ten hook shapes for this niche
Each example names a real, specific problem from `icp.md`, the community research or the gap analysis.
| # | Shape | Example | Pillar |
|---|---|---|---|
| 1 | **Succeeded, and still wrong** | "The pipeline is green. The dashboard still shows yesterday." | P2 |
| 2 | **Two numbers, both right** | "Your census says 412. Finance says 398. Neither one is wrong." [from demo] | P1 |
| 3 | **The scene** (time, role, stakes) | "7:40 a.m. The board deck goes out at 8. The refresh just failed." | P2 |
| 4 | **The question you can't answer** | "An auditor asks who opened this patient's data in your report. Can you show them?" | P4 |
| 5 | **The silent loss** | "Join FHIR lab results to visits with an inner join and some results vanish. No error." | P5 |
| 6 | **The bill nobody launched** | "Nobody built anything new. The capacity still hit 100% at 9 a.m." [story or demo] | P3 |
| 7 | **The line people believe** | "'Fabric is HIPAA compliant' doesn't mean your workspace is." | P4 |
| 8 | **Stop doing X** | "Stop counting patients in the visits table." | P1 |
| 9 | **The real number from the field** | "One health system was producing more than 12,000 reports a month." (Chartis) | P2 |
| 10 | **The dated change, as a consequence** | "New healthcare projects on Fabric start from source code now. Your team maintains it." | P5 |

## Three layers, one promise
- **Spoken:** ≤ 12 words to the tension. No greeting, no "in this video", no "let's talk about".
- **On screen (3–6 words, from the first frame):** the sharpest fragment, not the whole sentence — "412 vs 398",
  "GREEN BUT STALE", "WHO OPENED THIS?". This is also the LinkedIn thumbnail.
- **Visual:** the thing itself — the two numbers side by side, the green pipeline next to yesterday's date, the real
  Microsoft Learn notice. Never a talking head alone for the first second if a real surface exists.

## The scorecard — every hook, before the user sees it
Score each hook 0/1 on six checks and show the score. Ship only 5–6; rewrite anything below.
1. **Specific problem** — a viewer could say "that happened to me last month."
2. **Specific moment or object** — a time, a role, a number, a screen, a report name.
3. **Consequence or tension** — something breaks, someone asks, something contradicts.
4. **Problem before product** — no product name in the first 4 words.
5. **≤ 12 words** to the tension, and the on-screen fragment works with the sound off.
6. **Only we could say it** — a generic Fabric creator couldn't post this exact line; it carries the healthcare context.
Plus the buyer test: would a VP of analytics forward it to their BI manager with "this is us"?

## Banned openers (add to the blacklist test)
"If you…", "In this video…", "Let's talk about…", "Did you know…", "Here's the thing…", "So,…", "Hey guys",
"Have you ever…", a product name as the first word, a question that can be answered "no".
