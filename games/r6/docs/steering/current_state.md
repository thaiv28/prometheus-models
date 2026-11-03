# Current state

## Status

Playbook phase 2 (data) built and run live 2026-11-02; phase 3 (baseline benchmark) next. Phase 0: go (windows in [Product](product.md)). Data: 6,161 Liquipedia pages; 80,762 series and 86,058 maps (0 parse errors, 2021 on: 13–17k series a year); Kalshi 1,438 series and 828 map markets; series links 650/719, map links 380/414. siege.gg pages are still being fetched (5,306 IDs, newest first, ~4 s each).

## Known limits

- Liquipedia's newer participant lists import rosters from team pages (`import=true`), so their cards are incomplete; siege.gg fills those lineups where its ID is right.
- Many 2023 Liquipedia `siegegg=` IDs now point at unrelated 2026 siege.gg matches; pages more than 48 h from the Liquipedia start are ignored.
- Some Liquipedia team names are template codes (`tl`, `bd`); linking uses siege.gg names for them, so it improves as pages arrive.
- Pages before 2021 are sparse (older wikitext formats); they only feed the seed.

## Future work

- Rebuild once the siege.gg fetch is done; read the remaining link failures (49 "no team match").
- Phase 3: port the benchmark and ratings from `../dota2`.
