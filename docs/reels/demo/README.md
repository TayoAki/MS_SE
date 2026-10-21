# Example: Script 3 as a finished 9:16 short (before recording)

`build_example.py` builds "We counted the same patients three ways" in the Persa Shorts brand: the three numbers come
from real queries on the synthetic month (`synthetic_month.py`, seed 20261123), the screens are a stand-in SQL editor
until the creator records their own Fabric screen, a silhouette stands in for the creator, and real, openly licensed
photos own the frame on the lines that name a place.

```bash
O=~/persa-shorts/example-patient-counts
python3 -I docs/reels/demo/commons.py get $O/assets/broll "File:A waiting room at a medical healthcare clinic, doctor's office, hospital.jpg" waiting-room
python3 -I docs/reels/demo/commons.py get $O/assets/broll "File:Corridor on the second level - NÄL hospital 3.jpg" corridor   # optional: the hook
python3 -I docs/reels/demo/build_example.py --out $O
npx --yes hyperframes check $O && npx --yes hyperframes render $O -o $O/example-patient-counts.mp4 -q draft
```

`commons.py` searches Wikimedia Commons and keeps only licences that allow commercial reuse without share-alike (CC0,
public domain, CC BY 2.0–4.0), writes thumbnails and a contact sheet to look at before choosing, and records every
credit in `credits.json`. Wikimedia rate-limits bursts; the tool waits as asked. Places and objects only — no
recognisable people (the editor's BLACKLIST: no strangers, no stock people) and no hospital names or logos.

## Photo credits (CC BY needs the credit in the post)
| File | Photo | Licence | Source |
|---|---|---|---|
| waiting-room.jpg | Harrison Keely, "A waiting room at a medical healthcare clinic, doctor's office, hospital" | CC BY 4.0 | https://commons.wikimedia.org/wiki/File:A_waiting_room_at_a_medical_healthcare_clinic,_doctor%27s_office,_hospital.jpg |
| corridor.jpg (if fetched) | W.carter, "Corridor on the second level – NÄL hospital 3" | CC0 | https://commons.wikimedia.org/wiki/File:Corridor_on_the_second_level_-_N%C3%84L_hospital_3.jpg |

## Real Fabric screenshots and diagrams (Microsoft Learn, CC BY 4.0)
`learn_media.py` collects the screenshots and diagrams from the Fabric docs. You can give it a section (`fabric/iq`),
a single page, or `"search:<words>"` (Fabric pages whose title has those words). It writes `media.json` with the
credit and contact sheets to look at. SVG diagrams are rendered to PNG, and icons are dropped.
```bash
~/.cache/persa-shorts/py/bin/python -I docs/reels/demo/learn_media.py "search:direct lake" ~/persa-shorts/_broll-library/direct-lake
```
Credit in the post: "Screens: Microsoft Learn, CC BY 4.0 (cropped)". For which source to use for each kind of picture
and the rules, see `.claude/skills/content-machine/systems/3-editor/BROLL.md`.
