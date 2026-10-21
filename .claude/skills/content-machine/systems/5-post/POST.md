# System 5 — posting (Blotato)

Blotato is connected right inside Claude (Claude → Settings → Connectors → add **Blotato**; it has a free trial, then a
paid plan — say so before they sign up). When the videos are ready, the user just says "post them": you write the post
text, and Blotato posts the 9:16 video at the times they picked. **LinkedIn is the main platform** (their personal
profile, and/or a company page); Instagram, TikTok, Facebook, YouTube Shorts are optional extras from `profile.json`.

## The one rule: nothing goes out without their OK
Show EVERYTHING first, for every post: the video file, the cover, the post text, the hashtags, the account (personal
profile or page) and the exact date + time. Post or schedule **only after an explicit "yes"** for that batch. Never change
a scheduled post without asking. If a post fails, tell them; never retry silently into a different time.

## LinkedIn through Blotato (per Blotato's own docs, Oct 2026 — re-check before relying on a limit)
- Posts to the personal profile by default; a company page needs that page's id from Blotato's sub-accounts.
- Post text up to 3,000 characters; video MP4 between 3 s and 30 min, up to 500 MB (our shorts are far inside that).
- Blotato publishes and schedules on LinkedIn but does **not** handle LinkedIn comments, DMs or analytics — those are
  system 6, by hand. Blotato's API/MCP access is listed for paid plans, not the free trial.

## Steps
1. `blotato_list_accounts` → the connected accounts and what each platform needs. Match them to `profile.json →
   platforms` (LinkedIn first; ask once which account if there's a profile AND a page).
2. Upload each finished short (and its cover if the platform takes one) with `blotato_create_presigned_upload_url`, then
   PUT the file to the returned URL; keep the public media URL.
3. Text: LinkedIn = the `## LinkedIn post` section of SCRIPT.md, as approved (hook in the first 2 lines, the same comment
   keyword as the video, at most 3 hashtags). Other platforms: first line = the hook + the CTA, 2–4 short lines, 3–5
   hashtags. No emojis unless the user's own style uses them.
4. Times: the next free slots from `profile.json → times` in their time zone, following `calendar/linkedin-video-plan.md`
   (A reach, B authority, C offer across the week), never two on the same account on the same day unless they ask.
5. Show the table (video · cover · account · time · post text) → wait for **yes** → `blotato_create_post` per account
   with the schedule time → confirm each post's status (`blotato_get_post_status`) → append to
   `~/content-machine/posted.json` (date, account, funnel job, pillar, keyword, link).
6. Remind them: the first hour after it goes live is for system 6 — reply to comments and send the keyword DMs by hand.

A business that records a whole week on one day: schedule the week the same way, one approval for the whole table.
