# Current state

## Status

Playbook phase 4 done 2026-11-03. Adopted `player_round_glicko_rookie` + calibration layer at stage-2 look 1 (one look; [elo_backtest.md](../elo_backtest.md)): stage-2 map 0.5688 vs base 0.5774. It does not beat Kalshi on stage 2 (series +0.0196, blended +0.0061, both n.s.; 244 linked series, tier1/tier2 only). Trade set: series, all tiers, blended (maps never reached 100 rows for a blend fit). Next: Phase 5, open the holdout once.

Phase 2 (data) built and run live 2026-11-02. Phase 0: go (windows in [Product](product.md)). Data: 6,161 Liquipedia pages; 80,762 series and 86,058 maps (0 parse errors, 2021 on: 13–17k series a year); Kalshi 1,438 series and 828 map markets. siege.gg: 1,741 finished pages cached; only IDs below 7000 from 2024 on are valid (older and higher IDs are siege.gg's old numbering), so the rest were skipped. 3,475 lineup sides come from siege.gg, the rest from Liquipedia cards. Links after rebuild: series 669/719, maps 396/414.

## Known limits

- Liquipedia's newer participant lists import rosters from team pages (`import=true`), so their cards are incomplete; siege.gg fills those lineups where its ID is right.
- Many 2023 Liquipedia `siegegg=` IDs now point at unrelated 2026 siege.gg matches; pages more than 48 h from the Liquipedia start are ignored.
- Some Liquipedia team names are template codes (`tl`, `bd`); linking uses siege.gg names for them, so it improves as pages arrive.
- Pages before 2021 are sparse (older wikitext formats); they only feed the seed.

## Future work

- Rebuild once the siege.gg fetch is done; read the remaining link failures (49 "no team match").
- Phase 3: run the baseline benchmark, then record results before selecting any model.
