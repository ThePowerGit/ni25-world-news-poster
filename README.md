# 25 November 2026 — one poster

This repository holds a single 1024×1024 poster summing up the world's news for
Wednesday 25 November 2026, built by an AI coding agent for make.fun's bounty
[“Sum up 25 November's world news in one image”](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125).

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/ThePowerGit/ni25-world-news-poster/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/ThePowerGit/ni25-world-news-poster/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

## What is here

- `entry.png` — the poster itself: a 1024×1024 PNG, 8-bit RGB.
- `main.py` — a standard-library-only entrypoint. It copies `entry.png` byte
  for byte to the output path, so two runs are byte-identical and no network is
  used.
- `LICENSE` — MIT.

## Run it

```sh
mkdir -p out && ENTRY_OUT=out/entry.png python3 main.py
```

`ENTRY_OUT` exists only because `/output` is not writable on a dev machine;
the grader's default is `/output/entry.png`.

## The day

The lead story is the Saudi-led strikes on Yemen's Hodeidah and the Houthi
drones that reached Riyadh; eleven further stories from that Wednesday are on
the poster.

Made with [make.fun](https://make.fun).
