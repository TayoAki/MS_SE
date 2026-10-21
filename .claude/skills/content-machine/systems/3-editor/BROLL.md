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
creator's footage, voice or thumbnail, Microsoft logos as decoration, or anything from a client without their written OK.

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

**No: their footage, voice, face or thumbnail.** That includes clips cut together into a montage. If you name a video
on screen, show its title as your own text card.

**Creative Commons videos on YouTube** (search filter: Features → Creative Commons) are legally reusable with credit.
They still break "copy formats, not content", the uploader may not own everything in them, and they show someone
else's face or voice. Leave them out unless the creator says otherwise for one exact clip.

## Credits
List every picture you use in the script folder's `## On screen` section: file, source, licence. Then put the credit
lines at the end of the `## LinkedIn post` text, after the hashtags, so system 5 posts them. CC BY needs the credit
in the post. Microsoft's permission needs its line.
