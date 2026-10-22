#!/usr/bin/env python3
"""shorts.py — the outlier YouTube Shorts of a set of channels, with frames to look at (no API key needed).

    python3 -I shorts.py list <out> <channel_url>...         # every channel's /shorts tab -> <out>/shorts.json
    python3 -I shorts.py frames <out> [--top 40] [--min-x 3]  # 4 frames per outlier -> <out>/sheet-NN.jpg + outliers.json

Filter <out>/shorts.json to the on-topic rows (into a sub-folder) before `frames` when the channels post off-topic too.
Read every sheet and tag each row's format before claiming one (`content-machine/formats.md` is the result of a run).
Needs yt-dlp; `frames` needs Pillow (run it with ~/.cache/persa-shorts/py/bin/python).

x = views ÷ the median views of that channel's listed Shorts. Frames come from i.ytimg.com (frame0 = the first frame,
maxres1-3 = YouTube's automatic frames at about 25/50/75 %), the only pictures YouTube serves to this container.
"""
import json, os, statistics, subprocess, sys, time, urllib.request


def listing(url, n=120):
    r = subprocess.run(['yt-dlp', '--flat-playlist', f'-I1:{n}', '-J', url.rstrip('/') + '/shorts'],
                       capture_output=True, text=True)
    d = json.loads(r.stdout)
    rows = [dict(id=e['id'], views=e.get('view_count') or 0, title=e.get('title') or '') for e in d.get('entries', [])]
    return d.get('channel') or url, d.get('channel_follower_count') or 0, [r for r in rows if r['views']]


def cmd_list(out, urls):
    allr = []
    for u in urls:
        try:
            name, subs, rows = listing(u)
        except Exception as e:
            print(f'  ! {u}: {e}', file=sys.stderr); continue
        if not rows:
            print(f'  ! {u}: no shorts', file=sys.stderr); continue
        med = statistics.median(r['views'] for r in rows)
        for i, r in enumerate(rows):
            r.update(channel=name, subs=subs, median=int(med), x=round(r['views'] / med, 1) if med else 0, rank=i,
                     url=f"https://www.youtube.com/shorts/{r['id']}")
        allr += rows
        print(f'{name}: {len(rows)} shorts, median {int(med):,}, subs {subs:,}', file=sys.stderr)
        time.sleep(1.5)
    json.dump(allr, open(os.path.join(out, 'shorts.json'), 'w'), indent=1)


def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=30).read()


def cmd_frames(out, top, min_x):
    from PIL import Image, ImageDraw
    rows = [r for r in json.load(open(os.path.join(out, 'shorts.json'))) if r['x'] >= min_x]
    rows.sort(key=lambda r: -r['x'])
    rows = rows[:top]
    d = os.path.join(out, 'frames'); os.makedirs(d, exist_ok=True)
    strips = []
    for k, r in enumerate(rows):
        ims = []
        for f in ('frame0.jpg', 'maxres1.jpg', 'maxres2.jpg', 'maxres3.jpg'):
            p = os.path.join(d, f"{r['id']}-{f}")
            if not os.path.exists(p):
                try:
                    open(p, 'wb').write(get(f"https://i.ytimg.com/vi/{r['id']}/{f}"))
                except Exception:
                    continue
            im = Image.open(p).convert('RGB')
            if im.width > im.height:                      # letterboxed vertical frame: keep the middle
                w = round(im.height * 9 / 16); im = im.crop(((im.width - w) // 2, 0, (im.width + w) // 2, im.height))
            ims.append(im.resize((270, 480)))
        strip = Image.new('RGB', (40 + 270 * 4 + 12, 480 + 40), 'white')
        for j, im in enumerate(ims):
            strip.paste(im, (40 + j * 273, 40))
        dr = ImageDraw.Draw(strip)
        dr.text((6, 10), f"{k:02d}", fill='black')
        dr.text((40, 10), f"{r['channel'][:22]} · {r['views']:,} · {r['x']}x · {r['title'][:70]}", fill='black')
        strips.append(strip)
        r['n'] = k
    for s in range(0, len(strips), 4):
        chunk = strips[s:s + 4]
        sheet = Image.new('RGB', (chunk[0].width * 2, chunk[0].height * ((len(chunk) + 1) // 2)), 'white')
        for j, st in enumerate(chunk):
            sheet.paste(st, ((j % 2) * st.width, (j // 2) * st.height))
        sheet.save(os.path.join(out, f'sheet-{s // 4:02d}.jpg'), quality=80)
    json.dump(rows, open(os.path.join(out, 'outliers.json'), 'w'), indent=1)
    for r in rows:
        print(f"{r['n']:02d} | {r['channel'][:24]} | {r['views']:>9,} | {r['x']:>5}x | {r['title'][:80]} | {r['url']}")


if __name__ == '__main__':
    a = sys.argv[1:]
    if len(a) < 2 or a[0] not in ('list', 'frames'):
        sys.exit(__doc__)
    if a[0] == 'list':
        cmd_list(a[1], a[2:])
    else:
        top = int(a[a.index('--top') + 1]) if '--top' in a else 40
        mx = float(a[a.index('--min-x') + 1]) if '--min-x' in a else 3
        cmd_frames(a[1], top, mx)
