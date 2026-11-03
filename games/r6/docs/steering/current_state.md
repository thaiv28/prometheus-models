# Current state

## Status

**Phase 5 gate failed (H4), 2026-11-03.** Holdout opened once ([elo_holdout.md](../elo_holdout.md)): 2026-07-01 on, frozen `player_round_glicko_rookie` + calibration, June blend fits. Trade set (series, blended, depth-capped) flat ROI −1.72% [−23.8, +19.4]: interval includes 0. Blended series log loss vs Kalshi −0.0014 [−0.011, +0.008] (324 rows; raw +0.0186). Maps (not in the trade set) look better: blended tier1 −0.059 log loss, 26 bets, August alone. **H4 decision (user, 2026-11-03): keep the model frozen and recheck the same gate later.** Don't retune and reopen. Phase 4: adopted rookie + calibration at stage-2 look 1 (one look; [elo_backtest.md](../elo_backtest.md)).

Phase 2 (data) built and run live 2026-11-02. Phase 0: go (windows in [Product](product.md)). Data: 6,161 Liquipedia pages; 80,762 series and 86,058 maps (0 parse errors, 2021 on: 13–17k series a year); Kalshi 1,438 series and 828 map markets. siege.gg: 1,741 finished pages cached; only IDs below 7000 from 2024 on are valid (older and higher IDs are siege.gg's old numbering), so the rest were skipped. 3,475 lineup sides come from siege.gg, the rest from Liquipedia cards. Links after rebuild: series 669/719, maps 396/414.

## Known limits

- Liquipedia's newer participant lists import rosters from team pages (`import=true`), so their cards are incomplete; siege.gg fills those lineups where its ID is right.
- Many 2023 Liquipedia `siegegg=` IDs now point at unrelated 2026 siege.gg matches; pages more than 48 h from the Liquipedia start are ignored.
- Some Liquipedia team names are template codes (`tl`, `bd`); linking uses siege.gg names for them, so it improves as pages arrive.
- Pages before 2021 are sparse (older wikitext formats); they only feed the seed.

## Future work

- Recheck the Phase 5 gate after about three more settled months (from 2027-02): refresh the Liquipedia crawl, siege.gg (IDs below 7000 from 2024 on, plus new ones) and Kalshi (historical endpoints cover settled markets; no R6 collection is scheduled), rebuild, and rerun `evaluate_elo.py --holdout --layers none,calibration` with the model, trade set (series, blended) and June blend fits unchanged. Report the new months separately.
- If the recheck fails too: per-player stats (check whether siege.gg match pages carry them) would be the next model idea, judged on a fresh holdout.
