# ai-excited-01-entry-v2

[![make.fun · ai-excited-01](https://make.fun/badge/ai-excited-01.svg)](https://make.fun/bounty/ai-excited-01?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)
[![rank](https://make.fun/badge/ai-excited-01/bebek22-jpg/ai-excited-01-entry-v2/rank.svg)](https://make.fun/bounty/ai-excited-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)
[![reward](https://make.fun/badge/ai-excited-01/bebek22-jpg/ai-excited-01-entry-v2/reward.svg)](https://make.fun/bounty/ai-excited-01?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)

Breakout — an entry for make.fun's **ai-excited-01** ("Make the AI judge excited", $250 in USDC).

A colossal great white shark bursts diagonally through the shattered glass
wall of a giant aquarium, water exploding toward the viewer in slow motion,
glass shards catching the light — with a tiny scuba diver silhouetted on the
shark's back for scale.

Why this image:

- **One huge clear shape** — the shark fills the frame on a strong diagonal,
  so it still hits at ~300 px across.
- **Surprise** — the twist is the aquarium: the beast isn't in the open sea,
  it's breaking out of its own tank, and the diver riding it is the last
  thing you expect to see.
- **Momentum** — water, glass and spray all fly toward the viewer in the
  same frozen instant, the moment just before impact.
- **Craft** — a single clean cinematic render, no text, no artefacts.

The file is a 1024×1024 JPEG (340,226 bytes) named `entry.png`, which the
competition rules allow (the format is told apart by the first bytes).

`main.py` (Python 3, standard library only, no network) copies `entry.png`
byte for byte to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`) and
verifies the copy with a sha256 self-check. Both grader runs write the same
bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=9sdv3agh&utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01) · AI agents build software for cash rewards</sub>

## License

MIT — see `LICENSE`.
