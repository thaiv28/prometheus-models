# Research ledger

Every model idea tested, adopted or not, newest first, with its stage-1 and stage-2 numbers. Rules: [tech.md, Model change rules](../steering/tech.md). Count the stage-2 looks.

## Two-stage runs

**Holdout (opened once, 2026-11-03)**: 2026-07-01 – 2026-11-02, 324 linked series and 81 maps with a tradeable quote; frozen `player_round_glicko_rookie` + calibration, June blend fits (series a 1.09, b 0.35). Report: [`docs/elo_holdout.md`](../elo_holdout.md).

- **Gate failed.** Trade set (series, blended, depth-capped) flat ROI −1.72% [−23.8, +19.4], 48 of 104 bets filled; unlimited depth +1.5% [−15.1, +19.4], Kelly $59.17 from $50.
- Series log loss vs Kalshi: raw +0.0186 [−0.006, +0.045], blended −0.0014 [−0.011, +0.008]; tier2 blended −0.0026, tier1 −0.0004 (n.s.). No month drives it.
- Outside the trade set: maps blended tier1 −0.059 [−0.130, −0.008], flat ROI +64% (26 bets, 14 matches, all August); depth-capped +96% [−5, +200]. Post hoc; not a basis for retuning.

2026-11-03 **stage-2 look 1** (rebuilt DB with 2024+ siege.gg lineups; stage-1 re-search kept both pins). Base, rookie candidate, team_elo, each with none/regional/calibration; re-displayed paired against rookie (same look). Report: [`docs/elo_backtest.md`](../elo_backtest.md). Stage-2 looks: 1.

- **Adopted: rookie discount** (`player_round_glicko_rookie`, 225 / 3200). Stage 1 −0.0080; stage 2 map −0.0078 [−0.0104, −0.0049], series −0.0111 [−0.0147, −0.0075]; tier2/tier3 significant, tier1 +0.0085 and international +0.0032 n.s.
- **Adopted: calibration layer** (tier × online, ridge 4) over rookie: stage 2 map −0.00088 [−0.00165, −0.00019], none worse; series −0.0006 n.s. Judged on stage 2 only (the layer is fit on stage 1): weaker evidence.
- Rejected: regional layer (+0.000001 map).
- vs Kalshi (rookie+calibration, tradeable quote): series 244 rows +0.0196 [−0.016, +0.053]; blended 136 rows +0.0061 (tier1 −0.0046, tier2 +0.0099, n.s.); blended series flat ROI depth-capped −22.8% [−51.7, +5.6]. Maps 109 rows, no blend fit. Kalshi lists only tier1/tier2.
- **Trade set: series, all tiers, blended.** No slice is significant, so none is singled out.

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
