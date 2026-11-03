# Research ledger

Every model idea tested, adopted or not, newest first, with its stage-1 and stage-2 numbers. Rules: [tech.md, Model change rules](../steering/tech.md). Count the stage-2 looks.

## Two-stage runs

2026-11-03 ladder, **stage 1 only** (no stage-2 look), over pinned player_round_glicko (map 0.5897); paired by match.

- **Candidate: rookie discount** (`player_round_glicko_rookie`: penalty 225, maps 3200; grids widened to 75–600 and 400–6400, interior): map 0.5817, −0.0080; series 0.5641. Pinned; awaits stage 2.
- Rookie + tier/online K (penalty 225, maps 1600, tier-3 K 0.75, online K 1.0): −0.0082 [−0.0095, −0.0069] vs base (all, tier2, tier3, domestic significant; tier1 +0.00005 and international −0.0004 n.s.), but only −0.00015 over rookie alone: below the 0.0005 bar. Rejected.
- Tier/online K alone: chose 1.0 / 1.0 (no gain). Rejected.
- Reversion over rookie: to initial rating chose 0 (off); tier-target 0.05 each January −0.00013. Both below 0.0005. Rejected.
- Series temperatures fit by default (benchmark). Regional and calibration layers fit on stage 1 but score only on stage 2: tested at the first stage-2 look.

2026-11-03 stage-1 baseline (`--validate-from 2026-07-01`, so zero stage-2 looks). Report: [`docs/elo_backtest.md`](../elo_backtest.md). 50,153 maps in [2023-01-01, 2026-01-01) (tier1 1,659, tier2 4,707, tier3 43,764); lineups mostly from Liquipedia roster cards (siege.gg fetch in progress). Stage-2 looks: 0.

- player_round_glicko (k 24, τ 0.75, rd_new 280, rd_info 0.0625, fixed new players): map 0.5897, series 0.5756. rd_info chose the grid minimum; widened down to 0.015625, still 0.0625 (all interior). Pinned.
- player_glicko (k 24, rd_new 350, rd_info 0.0625): map 0.5982, series 0.5847. Pinned.
- team_elo (k 64): map 0.6359, series 0.6309. Coin 0.6931.
- Round credit beats binary by 0.0085 map log loss; tier1 is close to coin for every model (0.658 vs 0.693).
