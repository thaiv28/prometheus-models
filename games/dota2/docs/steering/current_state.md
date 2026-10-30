# Current state

## Status

Playbook phase: **2 (data)**. 2026-10-29: Phase 0 verdict go (see Product). Scaffolded from cs2-model `origin/main` (75bab17): Kalshi collector, Liquipedia crawler, linker and benchmark code are still CS2's and are being converted. Feed, trading and blend code were left out until the holdout gate passes.

## Known limits

- Liquipedia terms do not address betting/trading use.
- OpenDota's bulk explorer is thin from June 2026; per-game top-ups are rate-limited.

## Future work

1. Phase 2: Dota 2 data layer (Liquipedia tournaments and `Match:` pages, OpenDota games and players, Kalshi `KXDOTA2GAME`/`KXDOTA2MAP`, linking).
2. Phase 3: port the benchmark to binary game outcomes; baseline team Elo vs player Glicko.
