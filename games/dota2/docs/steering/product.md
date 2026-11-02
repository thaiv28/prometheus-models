# Product

## Goal

Price Dota 2 series before they start well enough to beat Kalshi's prices after fees, then trade them. Edge comes from a better rating model, as in Prometheus, cs2-model and valorant-model. Built by following Prometheus's `docs/playbooks/new_game.md`.

## Markets

- `KXDOTA2GAME`: series winner. Listed from Nov 2025; about 1,900 series through Oct 2026, now ~300 a month (live API holds markets settled from late Aug 2026; older ones are on the historical endpoints).
- `KXDOTA2MAP`: game winner by slot. Listed from Mar 2026.
- Also listed, not collected: `KXDOTA2GAME3WAY`, `KXDOTA2SPREAD`, `KXDOTA2TOTALMAPS`, `KXDOTA2MBH`, `KXDOTA2MPH`, `KXDOTA2`, `KXEWCDOTA2`.
- 2026-10-29 sample (59 settled series): 12% of volume trades before the scheduled start; median pregame volume $606 (quartiles $64 / $2,454). Biggest Kalshi events since Sep: EPL World Series SEA, EPL Masters, European Pro League, PGL Wallachia, BLAST Slam. Streamer events (BetBoom Streamers Battle, 1win Streamers League) are listed too.

## Model

Plan: player game Elo with RD (Glicko-style) over binary game outcomes, then the playbook's ladder (rookie discount, tier K, series temperature, reversion, form, KDA performance bonus, regional, calibration, online K), then calibration and market blend.

## Trading rules

League's limits ($250 per order and fixture, $1k exposure, $2k per day, same Kelly settings) from a $50 seed. No new orders once seed + settled profit − open stakes is $0 or less. Candidate-only run before live.

## Data

- **Liquipedia** (`liquipedia.net/dota2/api.php`, `action=query` only): tournaments, tiers, rosters, series (teams, date, best-of) and each game's Dota match ID. Tier-3 pages hold games inline with winner, length and heroes; tier-1/2 brackets keep matches on `Match:` namespace pages with match IDs only.
- **OpenDota** (`api.opendota.com`): game winner, ten players (account IDs, heroes, KDA, GPM/XPM), teams and league. Bulk by month through the SQL explorer (`matches`, `player_matches`), which has ~2,400 games/month through May 2026 but only 400–700 since and lacks some Kalshi leagues (European Pro League, EPL World Series SEA); fill gaps one game at a time with `/matches/{id}` (free tier: 2,000 calls/day, 60/min).
- **Kalshi** public API.

## Windows

Seed: before 2023. Stage 1: 2023-01-01 to 2025-11-01 (outcomes only). Stage 2: 2025-11-01 to 2026-07-01 (eight Kalshi months). Holdout: 2026-07-01 on (~1,000 Kalshi series by Oct 2026), opened once.
