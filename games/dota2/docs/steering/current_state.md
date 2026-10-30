# Current state

## Status

Playbook phase: **3 (benchmark)**. Data and benchmark ports are complete; real crawl and database pending. Liquipedia tournaments and Match pages, OpenDota enrichment, and Kalshi Dota 2 loading/linking build offline from caches. Binary team Elo and player Glicko now run the two-stage Dota benchmark with synthetic database coverage; real-data tuning and pins await the DB. Feed, trading and blend delivery remain deferred until the holdout gate passes.

## Known limits

- Liquipedia terms do not address betting/trading use.
- OpenDota's bulk explorer is thin from June 2026; per-game top-ups are rate-limited.
- Games without OpenDota data have no players.
- Players are keyed by Steam account; roster names are only for display.

## Future work

1. Run the real Phase 2 crawl and inspect coverage, orphans, winner conflicts and links.
2. Build the real DB, run stage 1 team Elo vs player Glicko, pin its winner, then validate on stage 2 before opening holdout.
