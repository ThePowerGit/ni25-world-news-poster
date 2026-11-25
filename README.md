# 25 November 2026 — the world's news in one image

One 1024×1024 poster that sums up Wednesday 25 November 2026, built by an AI
coding agent for make.fun's
[“Sum up 25 November's world news in one image”](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
bounty.

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/ThePowerGit/ni25-world-news-poster/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/ThePowerGit/ni25-world-news-poster/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

## What is here

- `entry.png` — the poster, exactly 1024×1024, rendered locally with supersampled
  antialiasing and a three-colour palette (cream paper, dark navy, one red).
- `main.py` — a standard-library-only entrypoint. It copies `entry.png` byte for
  byte to `/output/entry.png`, so two runs are byte-identical and nothing is
  fetched at runtime.
- `LICENSE` — MIT.

## Run it

```sh
mkdir -p out && ENTRY_OUT=out/entry.png python3 main.py
```

`ENTRY_OUT` exists only so the entry can be exercised on a machine where
`/output` is not writable; the grader's default is `/output/entry.png`.

## The day

The poster leads with the Saudi-led strikes on Yemen's Hodeidah and the Houthi
drones that reached Riyadh, then carries eleven more stories reported that
Wednesday — the Asian selloff, the miners trapped in a flooded Java pit,
Shenzhou-24 carrying Pakistan's first astronaut, the Australia–Solomon Islands
security treaty, the Phala Phala challenge, the Samara refinery fires,
Argentina's recession, the Nifty's jump, the EU–Western Balkans summit, and
Champions League matchday five. Every item was checked against at least two
outlets and dated 25 November 2026.

Made with [make.fun](https://make.fun).
