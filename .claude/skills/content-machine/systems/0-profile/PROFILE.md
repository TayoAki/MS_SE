# System 0 — the LinkedIn profile (your landing page)

Every video sends people to the same place: the little line under your name, then your profile. A buyer who liked a video
reads your headline, and if it says "this person fixes my problem" they click; the profile then has to sell. Treat it as a
landing page for health-system data leaders, not as a CV. Run this once at onboarding, then whenever the offer changes.

Claude never logs into LinkedIn and never edits the profile. It writes the text; the user pastes it in.

## Inputs
- The current profile: the user pastes the text, or saves it as a PDF (profile → More → Save to PDF) and drops it in.
- `~/content-machine/icp.md` (their exact words, what they search for, objections), `pillars.md`, `story-bank.md`,
  `fabric-field-guide.md`, `profile.md` (the offer and CTA).
- **Keyword pass** (the job-description miner, turned toward buyers): web-search 5–10 current job postings at US health
  systems for data/BI/analytics roles that mention Microsoft Fabric, Power BI or the data platform. Extract the terms that
  appear in most of them (tools, data types, outcomes) and rank by how many postings use each. These are the words
  recruiters, partners and buyers type into LinkedIn search. Keep the posting links in `research/keywords-<date>.md`.

## Output — `~/content-machine/linkedin-profile.md`
1. **Headline — 3 options.** Who you help + the result + 2–3 searchable keywords. E.g. the shape "Microsoft Fabric for
   health systems · reliable reporting, faster loads, one governed platform". Short enough to read in a comment
   notification. Recommend one and say why.
2. **Banner line.** One sentence of value + one proof point (a real result from the story bank, or what you do weekly
   on the channel). No quotes, no logos you don't own.
3. **About.** The first 3 lines are the hook (that's all that shows before "see more"): their problem in their words →
   what you do → for whom. Then skimmable blocks: the problems you fix · how you work · proof (stories with approval or
   anonymised) · what to do next (the CTA from profile.md). Use the keyword list naturally; no keyword walls.
4. **Featured.** The current freebie, the best video, one anonymised case write-up ("how we stopped two dashboards
   disagreeing"). Show thinking, not just a link.
5. **Experience.** Results, not duties: "cut the morning report refresh from [X] to [Y]" — real numbers only; unknowns
   stay as [brackets] for the user to fill, never invented.
6. **Skills.** Top skills for the About section; the full Skills list loaded with every relevant keyword from the pass
   (recruiter and buyer search uses it); 3–5 per experience entry at most.
7. **Small fixes.** Custom URL (their name, no numbers), a clear photo, contact info with the booking link if any.

Show it, take notes, save every note as a rule in NOTES.md, and re-run the keyword pass every quarter.
