# Current state

## Status

Frozen monthly blend coefficients and private `cs2-series` execution candidates are implemented; the feed job uploads inputs for Prometheus’s execution Lambda.

Hourly root `.github/workflows/cs2-refresh-db.yml` and 10-minute root `.github/workflows/cs2-feed.yml` are implemented for S3 snapshot/publication and optional Prometheus dispatch when feed content excluding `generated` changes (cron-job.org; hourly GitHub backups). Offline snapshot equality is tested; GitHub runs/timings remain unverified and raw S3 caches need initial seeding.

`promcs export` writes the site feed with frozen calls, replayed results and Kalshi prices; `--no-fetch` runs offline. Ratings require a fresh crawl + setup_db; only DB tournaments are scanned; TBD sides are omitted.

2026-10-29: Kalshi collector, Liquipedia crawler, offline SQLite build, Kalshi ↔ Liquipedia linking, ratings and the two-stage benchmark are implemented and tested. Real cache: 4,713 pages; DB: 58,034 matches and 119,185 maps, zero parse errors. Kalshi: 41,545 markets (backfill complete); series linked 5,389/7,907, maps 9,568/12,865; result agreements 29,740/29,774. Stage 1 (73,819 maps): player_round_glicko map/series log loss 0.639856/0.618358; team_elo 0.660656/0.645151 (after the 2026-10-29 alias/lineup data fix). Kalshi validation (full backfill): player_round_glicko blended series −0.0115 vs Kalshi (significant; tiers 2–3), raw level; maps no edge; see the research ledger. Adopted 2026-10-29: rookie discount 200/400 + tier-3 K × 0.75 (`player_round_glicko_rookie_weights`): stage-2 maps −0.0068 vs base, blended series −0.0145 vs Kalshi; pinned as `models.ADOPTED`, the default `--baseline`. Holdout (2026-11-01 on) has no matches yet.

## Known limits

- Settlement mismatches need source review; 2,210 markets lack a parseable scheduled time and use the open-time fallback.
- Kaggle stats: 9,884/12,322 maps linked (80.2%), mostly tiers 1–2; 93,933 player rows. Actual lineups replace 17,295 sides (788 changed: stand-ins); 3 new players remain (two absent from Liquipedia, one ambiguous); bare-key resolution moves 8,729 map/roster rows; 5 Kaggle IDs still split, only on sides that keep Liquipedia lineups. Upstream origin is undocumented; refresh-db fetches it daily (untested on GitHub's runners). Teammate-relative KDA/ADR bonuses were rejected (ledger).
- Liquipedia tournament rosters miss stand-ins; Kaggle-linked maps use actual five-player lineups when complete and conflict-free. No veto data.
- Time zones are converted from a fixed abbreviation table (0 unknown on 2026-10-29); unknown ones would be treated as UTC with time_known=0. International classification is approximate.
- Liquipedia terms do not address betting/trading use; ask in their #api-help Discord.
- The scheduled Kalshi collector fails until S3 holds `manifest.json` (seed with a local backfill and `scripts/kalshi_data.sh push`).

## Future work

1. Review the unlinked "no team match" events.
2. Then, one at a time through the model change rules: form layer (needs per-player stats: find a source), map strength, a veto-aware map model. Rookie + tier-3 K adopted (ledger, 2026-10-29); regional (retested over the adopted model), calibration, online K and tier moves rejected.
3. Collect legacy `KXCSGOGAME`/`KXCSGOMAP` if the backfill shows they hold priced 2025 matches.
4. Per-match lineups (Liquipedia LPDB by approval, or GRID Open Access) if stand-ins prove costly.
