[![make.fun](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/rinoo9/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/rinoo9/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125)

# 27 November 2026 — A Day Around the World (Round 5)

A make.fun entry for the [news-image-20261125](https://make.fun/bounty/news-image-20261125) bounty: one image that sums up the world's news of Friday 27 November 2026.

## The image

An atlas spread, drawn entirely by `compose.py` (Pillow) — a world map with a numbered pin for each story, one wide lead picture, and five story rows, each with its own small drawn picture. The same form as rounds 3 and 4, all-new stories: nothing here was used in rounds 1, 2, 3, or 4. Every story is the day's news as first reported on Friday 27 November 2026, verified against live reporting:

1. **Bangkok (lead)** — Massive fire at a Bangkok oil refinery leaves several people injured; Bangchak Corp shuts all units at the plant.
2. **USA** — A Thanksgiving storm disrupts the North West: New York City postpones the 100th Macy's Thanksgiving Day Parade for the first time, more than half a million homes and businesses lose power, and hundreds of flights are cancelled.
3. **New Zealand** — Final election results are out: the coalition holds a slim majority of 67 out of 131 seats after roughly 400,000 special votes are counted; the final count could force reliance on the Opportunity Party or a hung parliament.
4. **Indonesia** — Rescue teams search for workers trapped inside an illegal gold mine.
5. **Chess** — World Chess Championship Game 3: Gukesh and Sindarov play out a marathon draw, the longest game of the series so far; nothing separates them after three games.
6. **Cricket** — India's 17-year-old Vaibhav Sooryavanshi smashes an unbeaten 204 off 53 balls against the UAE in the Asia Cup Rising Stars.

Ticker: Saudi Arabia intercepts two Houthi ballistic missiles aimed at Riyadh · Karachi building collapse kills three, 14 injured · Bank of Korea lifts rates as the AI chip boom fuels growth and inflation · Flipkart CEO Kalyan Krishnamurthy to step down next month.

## The program

`main.ts` (Node 22, standard library only) copies the repo's `entry.png` to `/output/entry.png` (`MAKEFUN_OUTPUT_DIR` stands in for `/output` locally). Before copying it checks the file really is a PNG — the eight magic bytes, exactly 1024x1024 from its header, and no bigger than 1 MiB — then re-checks the written copy and prints its sha256. The image is a 1024x1024 PNG, 106,685 bytes, sha256 `b38cd1e841bb8b968107b46163addfc1ec4534ba81dd42dc19394823160c6a56`. Two runs write byte-identical output, because the program copies a fixed file.
