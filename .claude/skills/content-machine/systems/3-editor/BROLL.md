# B-roll: where the pictures come from

Every line in a script's `## On screen` list needs a picture you are allowed to use. Go down this list in order and
take the first source that shows what the line says. Licences were checked on 2026-10-21. Read them again if a source
changes.

| # | Source | Allowed because | Tool | Credit in the post |
|---|---|---|---|---|
| 1 | **Your own screen** in a Fabric trial or demo workspace, on synthetic data | Microsoft's standing permission for screenshots and video (conditions below) | screen recorder on your computer (OBS, Xbox Game Bar, macOS ⌘⇧5) | "Used with permission from Microsoft." |
| 2 | **Microsoft Learn screenshots and diagrams** for Fabric | The Fabric docs (MicrosoftDocs/fabric-docs) are licensed CC BY 4.0. You may crop and resize them if you say so in the credit | `docs/reels/demo/learn_media.py` | "Screens: Microsoft Learn, CC BY 4.0 (cropped)" |
| 3 | **Real 9:16 shots of a page** (a docs page, a release note, the roadmap, a blog post you are answering) | You are showing and discussing the page, with the phrase highlighted | `shoot-page-9x16.py` in the editor | name the page ("Source: Microsoft Learn, Fabric Apps overview") |
| 4 | **Your own data demos**: synthetic tables, counts, charts and SQL | Yours | `docs/reels/demo/synthetic_month.py`, the builders | none needed |
| 5 | **Openly licensed photos of places and objects** | Wikimedia Commons, CC0, public domain or CC BY only (no share-alike) | `docs/reels/demo/commons.py` | the photo's line from `credits.json` |
| 6 | **Free stock video of places and objects** (Pexels, Pixabay) | Their own free licences. Read the licence page once | download on your computer (both block the cloud container) and drop the file into the session | not required. Keep the link in the script |

Never use: a stranger's face (no stock people, no presenters), hospital names or logos, patient screens, another
creator's voice or thumbnail, their footage unless it is licensed (see
Splicing below), Microsoft logos as decoration, or anything from a client without their written OK.

## Your own screen: Microsoft's conditions
Microsoft's permissions page (microsoft.com/en-us/legal/intellectualproperty/permissions) allows screenshots "in
advertising, in documentation…, in videos, or on websites" if you:
- add **"Used with permission from Microsoft."**
- **don't alter the screenshot except to resize it, and don't use portions of it**. Show the whole window, scaled to
  fit, as a floating card over the take. Don't zoom in on one part.
- don't show screens from **beta products or products not yet commercially released**. This rules out preview
  features: Fabric Apps, ontology, anything marked "(preview)". For those, use source 2: Learn's own screenshots
  are CC BY and can be cropped.
- don't show splash screens, third-party content, or an identifiable person, and don't imply Microsoft endorses you.

Zooming in, cropping or showing a preview screen goes beyond that permission and relies on fair use. That is the
creator's call, not the editor's: ask once and note the answer in `~/content-machine/NOTES.md`.

## Finding Learn screenshots for a line
```bash
PY=~/.cache/persa-shorts/py/bin/python; L=~/persa-shorts/_broll-library
$PY -I docs/reels/demo/learn_media.py "search:direct lake" $L/direct-lake        # Fabric pages whose title has the words
$PY -I docs/reels/demo/learn_media.py fabric/iq $L/fabric-iq                      # a whole docs section
$PY -I docs/reels/demo/learn_media.py fabric/apps/overview $L/apps-overview       # one page
```
Each run writes the images, `media.json` (page, alt text, credit) and `sheet-*.jpg`. **Look at the sheets** before you
pick. The tool also:
- keeps Fabric pages only (the docs with the checked licence)
- drops icons
- renders SVG diagrams to PNG

Tall diagrams fill the 9:16 frame best, for example the Direct Lake framing diagram. With a wide screenshot, crop to
the one panel the line is about, so the text is big enough to read on a phone. The library sits outside git, so run the
command again in a new session.

To put a picture on a beat, use a `"kind": "shot"` line in a `docs/reels/demo/build_short.py` spec. Give the crop and
the highlight boxes in the image's own pixels, and the credit prints above the picture. `docs/reels/demo/rc3.json` is
a worked example. Pick crops from the full-size image, not the contact sheet.

## Taking from several videos
**Yes: ideas, questions, structure and facts.** When the same topic won on several channels (RC1's question won on
five), one script can draw on all of them:
- what they agree on
- the question they all answer
- the thing they all skip

It works as a roundup: "I watched the five most-watched videos on Fabric Apps. Here's what they agree on, and the one
thing nobody says." To write one:
- pick the videos with niche-scripts (`history.py`; above the channel's median)
- paste their transcripts. YouTube blocks video pages from the cloud container, so the creator copies them from
  YouTube's "Show transcript"
- map each video's beats in a table
- write every line in your own words
- check every fact on Learn
- name the creators in the post. Tagging them is a by-hand choice (system 6)

**Their footage: only when it is licensed** (next section). Never their voice, their face or their thumbnail. If you
name a video on screen, show its title as your own text card.

## Splicing real footage and demos (`docs/reels/demo/yt_clips.py`)
Real product footage moving on screen beats any still. Splice it in when one of these is true:
| Source | Why it's allowed | How to find it |
|---|---|---|
| A YouTube video whose licence reads **"Creative Commons Attribution license (reuse allowed)"** | The uploader licensed it for reuse with credit | YouTube search → Filters → Features → Creative Commons. `yt_clips.py info <url>` reads the licence |
| **Microsoft Learn's animated demos** (.gif screen recordings in the Fabric docs) | Fabric docs are CC BY 4.0 | 51 on 2026-10-22, in the IQ, data-science and warehouse docs: data agents, ontology as context, Planning, the Capacity Metrics app. `learn_media.py` finds them |
| **Your own recording** | Yours | `--licence own` |
| Anything else, with **written permission** from its creator | They said yes | Many creators say yes to a credit and a tag. Record it with `--permission "who, when, where"` |

Creative Commons Fabric videos checked on 2026-10-22:
| Video | Licence | Usable? |
|---|---|---|
| Edu. Inquisitive, "OneLake Security Demo in Fabric" | CC BY | Yes: screen only |
| Abiola David, "Microsoft Fabric Data Pipeline Masterclass" | CC BY | Screen parts |
| Lumio Visuals, "Microsoft Fabric Apps: Everything You Need to Know" | CC BY | Mostly motion graphics |
| Alex The Analyst, "What is Microsoft Fabric?" | CC BY | No: talking head only |
| MadeForCloud, "Microsoft IQ Explained" | CC BY | No: talking head only |

Most YouTube videos are under the standard licence, Microsoft's own channels included. Those need permission.

**The workflow:**
```bash
PY=~/.cache/persa-shorts/py/bin/python
$PY -I docs/reels/demo/yt_clips.py info "<url>"                          # the licence, before anything else
$PY -I docs/reels/demo/yt_clips.py scan "<url or file>" <dir> --every 10  # timecoded frame sheets (+ transcript)
$PY -I docs/reels/demo/yt_clips.py cut "<url or file>" 1:05 5 <out>/assets/clips/x.mp4 --crop x,y,w,h
```
Then put `{"kind": "clip", "src": "assets/clips/x.mp4"}` on the line in the `build_short.py` spec. The credit shows
above the clip, and the post's credit lines are in `assets/clips/credits.json`.

**Cutting rules:**
- **Crop to the part that matters.** A full 16:9 screen is unreadable at 9:16. Aim for text at least 28 px tall in
  the frame, which usually means a 2× zoom.
- **Crop out** faces, profile photos, webcam bubbles, YouTube's interface, watermarks, burned-in captions and logos.
- **Never use their audio.** Your voice runs over the clip.
- **Keep clips short:** 3–6 seconds, one idea each.

**YouTube from the cloud container:** licence checks and listings work, but YouTube refuses the downloads (HTTP 403 or
"confirm you're not a bot"). Do this instead:
1. Download on your computer:
   `yt-dlp -f "bv*[height<=1080][ext=mp4]" --download-sections "*1:00-1:30" "<url>"`
2. Drop the file into the session.
3. Run `cut` on the file with `--source "<url>" --licence "Creative Commons Attribution"`.

**Excerpts without a licence:** a short excerpt (4–6 s, credited) that you are commenting on relies on fair use. That is
your call for each clip; note the decision in `~/content-machine/NOTES.md`. Someone else's recording of the Fabric UI
is still Microsoft's screen, so the screenshot conditions above apply to it too.

## Credits
List every picture and clip you use in the script folder's `## On screen` section: file, source, licence. Then put the credit
lines at the end of the `## LinkedIn post` text, after the hashtags, so system 5 posts them. CC BY needs the credit
in the post. Microsoft's permission needs its line.
