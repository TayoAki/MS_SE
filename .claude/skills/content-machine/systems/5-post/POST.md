# System 5 — posting (Blotato)

Blotato is connected right inside Claude (Claude → Settings → Connectors → add **Blotato**; it has a free trial, then a
paid plan — say so before they sign up). When the videos are ready, the user just says "post them": you write the caption
and hashtags, and Blotato posts to Instagram, TikTok, Facebook (and more) at the times they picked — so they don't have to
be on their phone at 9, then at 1, then at 6. No opening three apps, no copying the caption three times.

## The one rule: nothing goes out without their OK
Show EVERYTHING first, for every post: the video file, the cover, the caption, the hashtags, the platforms/accounts and the
exact date + time. Post or schedule **only after an explicit "yes"** for that batch. Never change a scheduled post without
asking. If a post fails, tell them; never retry silently into a different time.

## Steps
1. `blotato_list_accounts` → the connected accounts and what each platform needs (e.g. Instagram reel `mediaType`, TikTok
   privacy flags, YouTube title). Match them to `profile.json → platforms`. Ask once if an account is ambiguous.
2. Upload each finished short (and its cover if the platform takes one) with `blotato_create_presigned_upload_url`, then PUT
   the file to the returned URL; keep the public media URL.
3. Caption per platform: first line = the hook idea + the call to action from the script (the same comment keyword!),
   2–4 short lines of value, then 3–5 relevant hashtags (no hashtag walls, no emojis unless the user's own style uses them).
4. Times: the next free slots from `profile.json → times` (e.g. 09:00 / 13:00 / 18:00 in their time zone), one video per
   slot, never two on the same platform at the same minute.
5. Show the table (video · cover · platforms · time · caption) → wait for **yes** → `blotato_create_post` per platform
   with the schedule time → confirm each post's status (`blotato_get_post_status`) → append to `~/content-machine/posted.json`.

A business that records a whole week on one day: schedule the week the same way, one approval for the whole table.
