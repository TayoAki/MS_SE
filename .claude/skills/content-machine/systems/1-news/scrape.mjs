#!/usr/bin/env node
// scrape.mjs — system 1 (the news): pulls what just happened in YOUR niche from free public sources, no keys needed.
//
//   node scrape.mjs --profile ~/content-machine/profile.json [--days 7] [--out ~/content-machine/ideas]
//
// Sources (each one optional, set in profile.json → "sources"):
//   reddit   { "subs": ["Dentistry", "askdentists"], "search": ["teeth whitening"] }   top posts of the week (public RSS)
//   hn       { "search": ["claude code", "open source"] }                               Hacker News stories (tech niches)
//   github   { "search": ["claude skill", "mcp server"] }                               new repos by stars (tech niches)
//   feeds    ["https://openai.com/news/rss.xml", "https://blog.google/technology/ai/rss/"]  any RSS / Atom feed (blogs, news, YouTube
//            channels: https://www.youtube.com/feeds/videos.xml?channel_id=<id>)
// Writes <out>/raw-<date>.json (every find, newest first, with its link and numbers) and remembers what it has shown you in
// <out>/seen.json, so the next run only brings new things. Claude reads the raw file, adds web-search angles for your niche
// (systems/1-news/NEWS.md) and writes the idea list you pick from. Optional: GITHUB_TOKEN (free) raises GitHub's limit.
import { readFile, writeFile, mkdir } from "node:fs/promises";
import { existsSync } from "node:fs";
import path from "node:path";
import os from "node:os";

const arg = (k, d) => { const i = process.argv.indexOf(`--${k}`); return i > 0 ? process.argv[i + 1] : d; };
const expand = (p) => p.replace(/^~(?=$|\/)/, os.homedir());
if (process.argv.includes("--help") || !arg("profile")) {
  console.log("usage: node scrape.mjs --profile ~/content-machine/profile.json [--days 7] [--out ~/content-machine/ideas]");
  process.exit(process.argv.includes("--help") ? 0 : 1);
}
const profile = JSON.parse(await readFile(expand(arg("profile")), "utf8"));
const S = profile.sources || {};
const DAYS = Number(arg("days", S.days || 7));
const OUT = expand(arg("out", path.join(path.dirname(expand(arg("profile"))), "ideas")));
const since = Date.now() - DAYS * 864e5;
const UA = { "user-agent": "content-machine/1.0 (a personal content research script)" };

async function get(url, headers = {}, kind = "json") {
  for (let k = 0; k < 2; k++) {
    try {
      const r = await fetch(url, { headers: { ...UA, ...headers }, signal: AbortSignal.timeout(20000) });
      if (r.status === 429) { await new Promise((s) => setTimeout(s, 4000)); continue; }
      if (!r.ok) throw new Error(`HTTP ${r.status}`);
      return kind === "json" ? await r.json() : await r.text();
    } catch (e) { if (k) throw e; }
  }
  throw new Error("rate limited (try again in a few minutes)");
}
const finds = [], failed = [];
const add = (f) => { if (f.title && f.url) finds.push({ ...f, title: f.title.trim().replace(/\s+/g, " ") }); };
const run = async (name, fn) => { try { await fn(); } catch (e) { failed.push(`${name}: ${e.message}`); } };

// ── Reddit: top posts of the week in your subreddits + a search (Reddit's public RSS; its JSON API now refuses scripts) ─
const redditFeeds = [...(S.reddit?.subs || []).map((s) => [`reddit r/${s}`, `https://www.reddit.com/r/${encodeURIComponent(s)}/top/.rss?t=week`]),
                     ...(S.reddit?.search || []).map((q) => [`reddit search "${q}"`, `https://www.reddit.com/search.rss?q=${encodeURIComponent(q)}&sort=top&t=week`])];
// ── Hacker News (tech niches) ───────────────────────────────────────────────────────────────────────────────────────
for (const q of S.hn?.search || []) await run(`hn "${q}"`, async () => {
  const j = await get(`https://hn.algolia.com/api/v1/search?query=${encodeURIComponent(q)}&tags=story&numericFilters=created_at_i>${Math.floor(since / 1000)}`);
  for (const h of j.hits) add({ source: `hacker news "${q}"`, title: h.title, url: h.url || `https://news.ycombinator.com/item?id=${h.objectID}`,
                                date: h.created_at, numbers: { points: h.points, comments: h.num_comments } });
});
// ── GitHub: new repos by stars (tech niches) ────────────────────────────────────────────────────────────────────────
const gh = process.env.GITHUB_TOKEN ? { authorization: `Bearer ${process.env.GITHUB_TOKEN}` } : {};
const day = new Date(since).toISOString().slice(0, 10);
for (const q of S.github?.search || []) await run(`github "${q}"`, async () => {
  const j = await get(`https://api.github.com/search/repositories?q=${encodeURIComponent(q)}+created:%3E${day}&sort=stars&order=desc&per_page=15`,
                      { accept: "application/vnd.github+json", ...gh });
  for (const r of j.items || []) add({ source: `github "${q}"`, title: `${r.full_name} — ${r.description || ""}`, url: r.html_url,
                                       date: r.created_at, numbers: { stars: r.stargazers_count } });
});
// ── RSS / Atom feeds (blogs, news sites, YouTube channels) ──────────────────────────────────────────────────────────
const unesc = (s) => s.replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&quot;/g, '"').replace(/&#39;|&#x27;/g, "'").replace(/&amp;/g, "&");
const tag = (x, t) => { const m = x.match(new RegExp(`<${t}[^>]*>([\\s\\S]*?)</${t}>`, "i"));
  return m ? unesc(m[1].replace(/<!\[CDATA\[|\]\]>/g, "")).replace(/<[^>]+>/g, " ").replace(/submitted by\s+\/u\/\S+|\[link\]|\[comments\]/g, "").trim() : ""; };
const BROWSER = { "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36" };
for (const [label, feed] of [...redditFeeds, ...(S.feeds || []).map((u) => [`feed ${new URL(u).hostname}`, u])]) await run(label, async () => {
  if (label.startsWith("reddit")) await new Promise((s) => setTimeout(s, 1500));   // be gentle: Reddit rate-limits bursts
  const x = await get(feed, label.startsWith("reddit") ? BROWSER : {}, "text");
  const items = x.match(/<item[\s\S]*?<\/item>|<entry[\s\S]*?<\/entry>/gi) || [];
  for (const it of items.slice(0, 20)) {
    const link = tag(it, "link") || (it.match(/<link[^>]*href="([^"]+)"/i) || [])[1];
    const date = tag(it, "pubDate") || tag(it, "published") || tag(it, "updated");
    add({ source: label, title: tag(it, "title"), url: link, date: date ? new Date(date).toISOString() : null,
          summary: (tag(it, "description") || tag(it, "summary") || tag(it, "content") || tag(it, "media:description")).replace(/&[a-z#0-9]+;/g, " ").replace(/\s+/g, " ").slice(0, 400) });
  }
});

// ── new since last time, newest first ───────────────────────────────────────────────────────────────────────────────
await mkdir(OUT, { recursive: true });
const seenFile = path.join(OUT, "seen.json");
const seen = new Set(existsSync(seenFile) ? JSON.parse(await readFile(seenFile, "utf8")) : []);
const fresh = [], urls = new Set();
for (const f of finds) {
  if (urls.has(f.url) || seen.has(f.url)) continue;
  if (f.date && Date.parse(f.date) < since) continue;
  urls.add(f.url); fresh.push(f);
}
fresh.sort((a, b) => (Date.parse(b.date || 0) || 0) - (Date.parse(a.date || 0) || 0));
const stamp = new Date().toISOString().slice(0, 10);
await writeFile(path.join(OUT, `raw-${stamp}.json`), JSON.stringify({ niche: profile.niche, days: DAYS, failed, finds: fresh }, null, 1));
await writeFile(seenFile, JSON.stringify([...seen, ...urls]));
const by = fresh.reduce((m, f) => ((m[f.source] = (m[f.source] || 0) + 1), m), {});
console.log(`${fresh.length} new finds from the last ${DAYS} days → ${path.join(OUT, `raw-${stamp}.json`)}`);
for (const [s, n] of Object.entries(by)) console.log(`  ${String(n).padStart(3)}  ${s}`);
if (failed.length) console.log(`failed (skipped): ${failed.join(" · ")}`);
