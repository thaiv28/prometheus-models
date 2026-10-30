# Research ledger

Every model idea tested, adopted or not, newest first, with its stage-1 and stage-2 numbers. Rules: [tech.md, Model change rules](../steering/tech.md). Count the stage-2 looks.

## Two-stage runs

2026-10-30 ladder, **stage 1 only** (no stage-2 look), over pinned player_glicko; paired by match.

- **Candidate: rookie + tier/online K** (`player_glicko_rookie_weights`: penalty 600, maps 800, online K 0.75, tier-3 K 0.75; all interior after widening): games −0.0122 [−0.0139, −0.0106] (tier1 −0.0136, tier2 −0.0110, tier3 −0.0115, all significant); series −0.0281 [−0.0319, −0.0243]. Awaits stage 2.
- Rookie alone: −0.0105, wants maps 1,600 (grid max). Weights alone: chose online K 1.0, tier-3 K 1.0 (no gain), as CS2 without rookie.
- Regional and calibration layers fit on stage 1 and score only on stage 2: tested in the next look.

2026-10-30 **stage-2 look 1**: base pinned after the full OpenDota top-up (95% of 2022–2026 games have players). Report: [`docs/elo_backtest.md`](../elo_backtest.md).

- Stage 1 (38,138 games): widened RD grids; player_glicko k 24, rd_new 280, rd_info 0.0625 (interior), fixed new players: game 0.6216, series 0.5991; team_elo 0.6501 / 0.6388.
- Stage 2 outcomes (9,328 games): player_glicko 0.6108 vs team_elo 0.6463.
- Vs Kalshi, series (621; 528 tier 1, 85 tier 2, 8 tier 3): raw −0.0008 [−0.0165, +0.0139]; blended (473) −0.0042 [−0.0124, +0.0036], n.s.; tier 2 blended −0.0129 n.s. Games (434): raw +0.0102 n.s., blended +0.0055 n.s.
- Returns after fees: raw series flat +2.5% [−10.6, +15.8], LoL-capped Kelly $50 → $61; blended series +11.8% [−13.5, +39.3], $50 → $88 (depth-capped +12.3%, $75); games lose raw (−6.6%).
- Kalshi's stage-2 Dota rows are nearly all tier 1; low-tier EPL leagues are listed from Sep 2026 (holdout).

2026-10-29 stage-1 baseline, **partial data** (OpenDota per-game top-up 1 of ~8 days: 2023–2026 games without players fall back to last lineups). Stage 1 only (`--validate-from 2026-07-01`, so zero stage-2 looks). 38,131 games, [2023-01-01, 2025-11-01).

- player_glicko (k 24, rd_new 280, rd_info 0.125, new_player fixed): game log loss 0.6294, series 0.6159.
- team_elo (k 32): game 0.6501, series 0.6389. Coin 0.6931.
- rd_new and rd_info chose grid minima: widen both before pinning. Rerun once the top-up is done.
