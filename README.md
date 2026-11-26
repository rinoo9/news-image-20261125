[![make.fun](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/rinoo9/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/rinoo9/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125)

# 25 November 2026 — A Day Around the World (Round 3)

A make.fun entry for the [news-image-20261125](https://make.fun/bounty/news-image-20261125) bounty: one image that sums up the world's news of Wednesday 25 November 2026.

## The image

An atlas spread, drawn entirely by `compose.py` (Pillow) — a world map with a numbered pin for each story, one wide lead picture, and five story rows, each with its own small drawn picture. A different form from rounds 1 and 2, and all-new stories: nothing here was used in either earlier round. Every story is the day's news as first reported on Wednesday 25 November 2026, verified against live reporting:

1. **Ukraine (lead)** — Ukraine says it destroyed the road span of the Kerch Bridge, the bridge linking Russia to occupied Crimea; Moscow says it will rebuild.
2. **Technology** — Nvidia reinstates Jensen Huang as chief executive, twelve days after he resigned; Trump says he may pardon him.
3. **Gaza** — Israel kills Hamas security chief Mohammad Abuelouf, his wife and two children, Gaza officials say (Just Security).
4. **United States** — Kilmar Ábrego García leaves the US for Spain, ending a twenty-month legal ordeal.
5. **Cuba** — The WHO chief urges the US to end a fuel blockade that endangers children in Cuba (Just Security).
6. **Iowa** — The Army detonates its old lead-azide explosives stockpile in a controlled blast; early air readings show no lead.

Ticker: Sullivan concedes the Alaska race to Peltola · DOJ charges 800 in a global scam crackdown · Hong Kong marks one year since its deadly fire · Sinner out after knee surgery.

## The program

`main.ts` (Node 22, standard library only) copies the repo's `entry.png` to `/output/entry.png` (`MAKEFUN_OUTPUT_DIR` stands in for `/output` locally). Before copying it checks the file really is a PNG — the eight magic bytes, exactly 1024x1024 from its header, and no bigger than 1 MiB. The image is a 1024x1024 PNG, 105,865 bytes, sha256 `aa6b417c2a9d3f8881f95d0d66277c34369571c2f788b77f905a1dd65907077a`. Two runs write byte-identical output, because the program copies a fixed file.
