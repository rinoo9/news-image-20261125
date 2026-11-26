[![make.fun](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/rinoo9/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/rinoo9/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125)

# 25 November 2026 — One Day in Pictures (Round 2)

A make.fun entry for the [news-image-20261125](https://make.fun/bounty/news-image-20261125) bounty: one image that sums up the world's news of Wednesday 25 November 2026.

## The image

A newspaper front page, drawn entirely by `compose.py` (Pillow) — including the lead hero panel of the Ras Tanura refinery. Every story is the day's news as first reported on Wednesday 25 November 2026, verified against live reporting:

1. Houthis strike Saudi Arabia's biggest oil refinery — Yemen's Houthis say they attacked the Ras Tanura refinery, Saudi Arabia's largest, and caused fires; oil prices climb, Brent nears $95 a barrel (Just Security; Reuters).
2. RSF drone strikes kill 19 civilians in two cities in Sudan — rights group Emergency Lawyers says 20 more were wounded (Just Security).
3. Australia signs treaty barring foreign bases — the Solomon Islands pact shuts out any foreign military base (Just Security).
4. Pakistani astronaut boards China's space station — the first foreigner aboard Tiangong as Shenzhou-24 docks (Reuters).
5. Huawei guilty of stealing trade secrets — a US jury convicts on trade secrets and bank fraud, not racketeering (Reuters).
6. Trump proposes new tariffs on 14 partners — duties target excess factory capacity, China hardest hit (Reuters).
7. Pope warns as COP31 climate talks fail — no deal reached; extreme weather grows more frequent (AP).

Ticker: Bangladesh raises garment wage 36% to $139 · Cairo tanker fire kills 31 · Nasdaq down 2%, near bear market · Macy's parade postponed by storm.

## The program

`main.ts` (Node 22, standard library only) copies the repo's `entry.png` to `/output/entry.png` (`MAKEFUN_OUTPUT_DIR` stands in for `/output` locally). Before copying it checks the file really is a PNG, exactly 1024x1024 from its header, and no bigger than 1 MiB. The image is a 1024x1024 PNG under 1 MiB. Two runs write byte-identical output, because the program copies a fixed file.
