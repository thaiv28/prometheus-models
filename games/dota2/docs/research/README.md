# Research ledger

Every model idea tested, adopted or not, newest first, with its stage-1 and stage-2 numbers. Rules: [tech.md, Model change rules](../steering/tech.md). Count the stage-2 looks.

## Two-stage runs

**Holdout (opened once, 2026-10-30)**: 2026-07-01 – 2026-10-29, 3,835 games, 557 linked series with a tradeable quote; frozen stage-1 parameters and June blend fits; adopted `player_glicko_rw_tier_revert` + form. Report: [`docs/elo_holdout.md`](../elo_holdout.md).

- **Gate (blended series flat ROI after fees, depth-capped, 95% interval above 0): FAIL, narrowly.** +14.5% [−0.4, +31.4], LoL-capped Kelly $50 → $325 (62% drawdown). Unlimited depth: +13.2% [+1.5, +25.2], $50 → $3,310.
- Vs Kalshi, series: blended −0.0290 [−0.0431, −0.0162], raw −0.0263 [−0.0478, −0.0059], both significant; better than Kalshi every month. Tier 3 (289 rows) blended −0.0439 significant, depth-capped ROI +29.6% [+10.7, +49.3]; tier 1 −0.0168 n.s., +3.8%; tier 2 −0.0023 n.s., −19.1%.
- By month (blended, depth-capped): Jul +54.4%, Aug −3.6%, Sep +21.4%, Oct +2.8%. July carries much of the return.
- Games (not in the trade set): blended −0.0001; raw ROI +5.2% n.s.
- Context: base player_glicko blended series −0.0246, depth-capped +10.3% [−5.9, +26.5]; team Elo loses.

2026-10-30 **stage-2 look 2** (ladder survivors + layers; the same run re-displayed paired against the rookie candidate). Report: [`docs/elo_backtest.md`](../elo_backtest.md). Stage-2 looks: 2.

- **Adopted: rookie + tier/online K** (`player_glicko_rookie_weights`: 600 / 800, online 0.75, tier-3 0.75). Stage 1 −0.0122 (every tier); stage 2 −0.0110 [−0.0141, −0.0081] vs base (tier1, tier3 significant; tier2 −0.0073 n.s.). Blended series vs Kalshi −0.0070 (base −0.0042).
- **Adopted: tier-target reversion** (`player_glicko_rw_tier_revert`: 0.1 each October; grid widened down to 0.025, still chose 0.1). Stage 1 −0.00052 [−0.00090, −0.00016] (tier3 significant), just over the 0.0005 bar; stage 2 +0.00038 [−0.00038, +0.00113] n.s. Passes the rules but the weakest adoption.
- **Adopted: form layer** (starters' KDA-per-minute EMA, fitted on stage 1) over reversion: stage 2 −0.00184 [−0.00310, −0.00064], tier3 significant, none worse. Like CS2's layers it is judged on stage 2 (the benchmark scores layers only there): weaker evidence than a stage-1 gain.
- Rejected: reversion to start (−0.00049, below 0.0005); KDA performance bonus (perf_k 3, −0.0002 n.s.); regional layer (−0.00036 n.s. over reversion); calibration (−0.00004).
- Adopted model vs Kalshi, series: blended (473) −0.0080 [−0.0200, +0.0028] n.s.; tier2 −0.0182, tier3 −0.118 (8 rows), n.s. Blended flat ROI +12.1% [−5.7, +32.0], depth-capped +16.0% [−10.8, +46.0]; LoL-capped Kelly $50 → $60. Games: blended +0.0021, lose.
- **Ladder done (plateau, per the playbook).** Trade set fixed before the holdout: series (`KXDOTA2GAME`), all tiers; no game markets; no tier filter (tier 2/3 look best on 33 and 7 bets: too few to select on).

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
