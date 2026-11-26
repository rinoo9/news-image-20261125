[![make.fun](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/rinoo9/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/rinoo9/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125)

# 26 November 2026 — A Day Around the World (Round 4)

A make.fun entry for the [news-image-20261125](https://make.fun/bounty/news-image-20261125) bounty: one image that sums up the world's news of Thursday 26 November 2026.

## The image

An atlas spread, drawn entirely by `compose.py` (Pillow) — a world map with a numbered pin for each story, one wide lead picture, and five story rows, each with its own small drawn picture. The same form as round 3, all-new stories: nothing here was used in rounds 1, 2, or 3. Every story is the day's news as first reported on Thursday 26 November 2026, verified against live reporting:

1. **Kyiv (lead)** — Russian ballistic missiles strike Kyiv overnight, hitting a shopping centre in the Desnianskyi district; seven people wounded.
2. **Gaza** — Israeli strikes kill nine in Gaza, including Khaled Abu Nada, the Hamas-appointed deputy education minister, in Deir al-Balah. A different specific event from round 3's killing of Hamas security chief Abuelouf.
3. **Space** — The US FCC approves SpaceX's plan for up to one million satellites for orbital data centres.
4. **North Korea** — Pyongyang expels Switzerland's top diplomat and orders its newly reopened office closed, five weeks after the mission resumed.
5. **South Africa** — A court throws out the report behind the impeachment push against President Ramaphosa.
6. **DR Congo** — Ebola cases pass 12,000 in the country's worst outbreak.

Ticker: EU leaders meet over a €2 trillion budget · King tides flood California's coast · Memory-chip shortage triples some RAM prices · China investigates Shanghai party chief Chen Jining.

## The program

`main.ts` (Node 22, standard library only) copies the repo's `entry.png` to `/output/entry.png` (`MAKEFUN_OUTPUT_DIR` stands in for `/output` locally). Before copying it checks the file really is a PNG — the eight magic bytes, exactly 1024x1024 from its header, and no bigger than 1 MiB — then re-checks the written copy and prints its sha256. The image is a 1024x1024 PNG, 102,032 bytes, sha256 `64fd18c38cef0f1fafa4214343ed4344b311df02fd9d757aeffc6d51334312f6`. Two runs write byte-identical output, because the program copies a fixed file.
