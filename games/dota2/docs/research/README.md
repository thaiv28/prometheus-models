# Research ledger

Every model idea tested, adopted or not, newest first, with its stage-1 and stage-2 numbers. Rules: [tech.md, Model change rules](../steering/tech.md). Count the stage-2 looks.

## Two-stage runs

2026-10-29 stage-1 baseline, **partial data** (OpenDota per-game top-up 1 of ~8 days: 2023–2026 games without players fall back to last lineups). Stage 1 only (`--validate-from 2026-07-01`, so zero stage-2 looks). 38,131 games, [2023-01-01, 2025-11-01).

- player_glicko (k 24, rd_new 280, rd_info 0.125, new_player fixed): game log loss 0.6294, series 0.6159.
- team_elo (k 32): game 0.6501, series 0.6389. Coin 0.6931.
- rd_new and rd_info chose grid minima: widen both before pinning. Rerun once the top-up is done.
