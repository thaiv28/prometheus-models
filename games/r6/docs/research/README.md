# Research ledger

Every model idea tested, adopted or not, newest first, with its stage-1 and stage-2 numbers. Rules: [tech.md, Model change rules](../steering/tech.md). Count the stage-2 looks.

## Two-stage runs

2026-11-03 stage-1 baseline (`--validate-from 2026-07-01`, so zero stage-2 looks). Report: [`docs/elo_backtest.md`](../elo_backtest.md). 50,153 maps in [2023-01-01, 2026-01-01) (tier1 1,659, tier2 4,707, tier3 43,764); lineups mostly from Liquipedia roster cards (siege.gg fetch in progress). Stage-2 looks: 0.

- player_round_glicko (k 24, τ 0.75, rd_new 280, rd_info 0.0625, fixed new players): map 0.5897, series 0.5756. rd_info chose the grid minimum; widened down to 0.015625, still 0.0625 (all interior). Pinned.
- player_glicko (k 24, rd_new 350, rd_info 0.0625): map 0.5982, series 0.5847. Pinned.
- team_elo (k 64): map 0.6359, series 0.6309. Coin 0.6931.
- Round credit beats binary by 0.0085 map log loss; tier1 is close to coin for every model (0.658 vs 0.693).
