# Product

## Goal

Price Rainbow Six Siege series before they start well enough to beat Kalshi's prices after fees, then trade them. Edge comes from a better rating model, as in Prometheus and the other games here. Built by following Prometheus's `docs/playbooks/new_game.md`.

## Markets

Phase 0 study, 2026-11-02 (Kalshi public API, live and historical endpoints):

- `KXR6GAME`: series winner. First listed 2025-11-15 (two Munich Major series), steadily from Jan 2026; 719 series through Oct 2026, about 60 a month (Sep 2026: 219, Stage 2 of every regional league).
- `KXR6MAP`: map winner by slot, from Feb 2026; 414 events.
- Also listed, not collected: `KXR6SPREAD`, `KXR6TOTALMAPS`, `KXR6`, `KXEWCRB6`, `KXEWCRSS`, `KXEWCRAINBOW6SEIGE`.
- Nearly all tier 1: the four regional leagues (NA, EU-MENA, SA, APAC with its sub-regions) and their Kickoffs, Six Invitational and LCQs, BLAST Majors, Esports World Cup; a few Challenger League, CN League and EML Challenger series.
- Sample of 71 settled series: 25% of volume trades before the scheduled start; median pregame volume $1,607 (quartiles $323 / $4,048).
- Tradeable quote (first hourly bid/ask ≥30 min after listing, ≥2 h before start, spread ≤0.06): Apr 35/72, May 39/47, Jun 110/110, Jul 56/59, Aug 34/38, Sep 206/210, Oct 57/61. Nov 2025 – Mar 2026 rules give a date without a time (120 series); their starts come from Liquipedia.

## Model

Plan: player map Elo with RD (Glicko-style) over map outcomes, round margins available, then the playbook's ladder (rookie discount, tier K, series temperature, reversion; form and KDA only if per-player stats appear), then calibration and market blend.

## Trading rules

League's limits ($250 per order and fixture, $1k exposure, $2k per day, same Kelly settings) from a $50 seed. No new orders once seed + settled profit − open stakes is $0 or less. Candidate-only run before live.

## Data

- **Liquipedia** (`liquipedia.net/rainbowsix/api.php`, `action=query` only): tournaments, tiers, series (teams, date with timezone, best-of), maps with rounds by side (`t1atk`, `t1def`, overtime), vetoes, operator bans, substitutions, and each match's siege.gg ID. Results are inline from tier 1 (2026 Major, regional leagues) to tier 4 (Rebellion Cup 2026); checked back to 2022 (Charlotte Major, NAL 2022, SI 2023). Newer participant lists import rosters from team pages (`import=true`), so wikitext alone lacks full lineups.
- **siege.gg** (`siege.gg/matches/<id>`): both five-player rosters per match, map vetoes, scores. Robots allows everything but login pages; no terms page forbids caching. Per-player stats show "No player stats data available" on the pages checked: not a planned source.
- **Kalshi** public API.

## Windows

Fixed 2026-11-02; never moved.

- Seed: before 2023-01-01.
- Stage 1: [2023-01-01, 2026-01-01), outcomes only (three years; Kalshi had two series).
- Stage 2: [2026-01-01, 2026-07-01), six Kalshi months (~300 series with a quote).
- Holdout: 2026-07-01 on, opened once; ~355 series with a tradeable quote through Oct 2026, above the 300 minimum if most link.
