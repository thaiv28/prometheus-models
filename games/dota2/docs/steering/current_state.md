# Current state

## Status

Playbook phase: **2 (data)**. Phase 2 code done; real crawl pending. Liquipedia tournaments and Match pages, OpenDota enrichment, and Kalshi Dota 2 loading/linking build offline from caches. Phase 3 rating and benchmark code remains CS2's; its test modules are skipped until ported to games. Feed, trading and blend delivery remain deferred until the holdout gate passes.

## Known limits

- Liquipedia terms do not address betting/trading use.
- OpenDota's bulk explorer is thin from June 2026; per-game top-ups are rate-limited.
- Games without OpenDota data have no players.
- Players are keyed by Steam account; roster names are only for display.

## Future work

1. Run the real Phase 2 crawl and inspect coverage, orphans, winner conflicts and links.
2. Phase 3: port the benchmark to binary game outcomes; baseline team Elo vs player Glicko.
