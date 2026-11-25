[![make.fun](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/rinoo9/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/rinoo9/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125)

# 25 November 2026 — One Day in Pictures

A make.fun entry for the [news-image-20261125](https://make.fun/bounty/news-image-20261125) bounty: one image that sums up the world's news of Wednesday 25 November 2026.

## The image

A newspaper front page, drawn by `compose.py` (Pillow) around a generated photograph of a cargo ship in the Gulf of Finland at dusk. Every story is the day's news as first reported on Wednesday 25 November 2026, verified against live reporting:

1. Kyiv says it sank a Russian warship and hit a cargo ship — President Zelenskyy confirmed Ukrainian drones struck two Russian vessels: a warship sunk off Benghazi, Libya, and a cargo ship hit in the Gulf of Finland. Moscow called the strikes "terrorism" and vowed consequences; Norway urged caution (Reuters; RFE/RL).
2. Houthi drone hits Riyadh's tallest tower — eleven people wounded, Saudi civil defence says (Reuters).
3. CIA and spy chief's office hit by cyber breach — unclassified information taken in a breach of the CIA and the Director of National Intelligence, sources say (Reuters).
4. NATO sends early-warning jets to Poland — surveillance aircraft move east after missiles landed in Poland during an attack on Ukraine.
5. Iran says three tankers hit by mines — the Revolutionary Guard Navy blames naval mines in the Strait of Hormuz.
6. Gaza toll reaches 74,746; 266m face hunger — Oxfam warns of pollution across Gaza; the UN food agency says 266 million people face acute food insecurity.
7. Trump gives Giuliani the Medal of Freedom — the former New York mayor takes the top US civilian honour; Huawei is found guilty of stealing trade secrets in a US trial.

Ticker: BJP and Akali Dal reunite for Punjab 2027 · England beat Australia by eight wickets in the T20 · Fort Hood gunman seeks a stay of execution · France orders the Sarkozy corruption case to trial.

## The program

`main.ts` (Node 22, standard library only) copies the repo's `entry.png` to `/output/entry.png` (`MAKEFUN_OUTPUT_DIR` stands in for `/output` locally). Before copying it checks the file really is a PNG, exactly 1024x1024 from its header, and no bigger than 1 MiB. The image is a 1024x1024 PNG under 1 MiB. Two runs write byte-identical output, because the program copies a fixed file.
