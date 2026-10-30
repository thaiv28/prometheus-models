# Tech

## Stack

Python ≥ 3.12 with uv; SQLite rebuilt from raw caches; raw SQL; Typer CLI (`promdota`); ruff; pytest (offline, fixtures in `tests/fixtures/`).

## Layout

| Path | Purpose |
|---|---|
| `promdota/main.py` | CLI groups: `kalshi`, `liquipedia`, `opendota` |
| `promdota/kalshi/{api,collect,cli}.py` | Public HTTP client, raw catalogs, trades, candles and books |
| `promdota/liquipedia/{http,cache,crawl,cli}.py` | Rate-limited query API, incremental raw cache and discovery |
| `promdota/liquipedia/parse.py` | Pure balanced-template Dota parser, version 2 |
| `promdota/liquipedia/regions.py` | Tournament host country → macro region |
| `promdota/opendota/{http,cache,fetch,cli}.py` | Explorer months, projected single games, pacing and retry cache |
| `scripts/001_create_tables.sql` | SQLite schema and indexes |
| `scripts/002_load_liquipedia.py` | Offline tournament, Match-page, roster and game loader |
| `scripts/003_load_opendota.py` | Offline winners, Steam players, stats and team mappings |
| `scripts/004_load_kalshi.py` | Offline Kalshi catalogs |
| `scripts/005_link_kalshi.py`, `promdota/link.py` | Series/game linking, aliases and settlement checks |
| `scripts/setup_db.sh` | Rebuild `db/dota2.db` from cached inputs only |
| `tests/test_liquipedia_*.py`, `tests/test_opendota.py`, `tests/test_link.py`, `tests/test_kalshi_collect.py` | Offline fixture and temporary-cache checks |
| `tests/fixtures/` | Saved API projections and raw Liquipedia records |
| `promdota/ratings/`, `evaluation.py`, `backtest.py`, `blend.py` | Binary game ratings, evaluation, returns and causal blends |
| `scripts/evaluate_elo.py`, `series_independence.py` | Existing two-stage benchmark and diagnostics |
| `.githooks/pre-commit`, `scripts/work_log.py`, `tests/test_steering.py` | Work-log rotation and document guards |

## Kalshi collector

`promdota kalshi collect [--no-books] [--limit N]` refreshes `KXDOTA2GAME` (series) and `KXDOTA2MAP` (individual games), saves final-market histories and snapshots active books. `--limit` caps new trade/candle fetches combined. `promdota kalshi books --every 60 --minutes 60` refreshes active tickers each pass. Data root is `PROMDOTA_DATA` (default `data/`); files live under `kalshi/`. See Deployment for scheduling.

## Liquipedia crawler

`promdota liquipedia crawl [--limit N] [--full] [--no-matches]` uses only `action=query` at `https://liquipedia.net/dota2/api.php`, gzip, a request interval above two seconds and retry backoff. The User-Agent identifies dota2-model and carries the existing contact; `LIQUIPEDIA_CONTACT` overrides it. Category:Tournaments membership remains authoritative. Revision checks fetch only new or changed content unless `--full` is set. Subpages come from a full listing of non-redirect articles (`list=allpages`, namespace 0: every title under a tournament root, parented to the nearest root), since Dota stage tabs live in per-series templates; `linkN` tab links add more through three rounds. Links drop `#fragment`s and collapse spaces; the loader keeps one title per page ID (`duplicate_pages`). Dropped connections and HTTP exceptions are retried like timeouts.

A second pass lists namespace 130 with `generator=allpages`, `gapnamespace=130`, `gaplimit=500`, `prop=info`, following continuation. New or changed `lastrevid` values trigger content batches of 50. Match pages have source `match`, no parent. `--no-matches` skips this pass; `--limit` caps fetched titles across both passes, tournaments first. Summaries include `match_pages`.

Under `PROMDOTA_DATA`, `liquipedia/pages/<sha1-prefix>/<sha1>.json.gz` stores unparsed wikitext and metadata. `index.json` tracks revisions, sources and parents, atomically saved after batches; category snapshots record title lists. `promdota liquipedia status` reports cache counts and newest fetch time. Credit: Liquipedia contributors, CC BY-SA 3.0. No HTML scraping.

## OpenDota fetcher

`promdota opendota bulk [--from 2019-01] [--to YYYY-MM]` requests two `/explorer?sql=` queries per UTC month: match metadata and joined player stats, ordered by game and player slot. Rows are saved unchanged with `fetched_at` under `opendota/explorer/{matches,players}/YYYY-MM.json.gz`. An `err` response is counted and never cached. A month fetched more than 45 days after its end is final; recent months refresh.

`promdota opendota games [--limit N] [--db db/dota2.db]` fills missing referenced games newest first through `/matches/{id}`. It skips games already available from explorer or single caches. Single records under `opendota/matches/<last-three-digits>/<id>.json.gz` carry `FETCH_VERSION=1` and only match ID, time, duration, outcome, league/series/team IDs plus each player's account ID, slot, hero, KDA, GPM and XPM. Full responses are about 250 KB each (roughly 5 GB for history); this projection avoids retaining unused telemetry. Only finished games with ten players are cached. Missing/incomplete responses enter `missing.json` and retry after seven days. Index and missing files are written atomically after batches of 50. `status` counts cached months, singles and missing IDs.

For initial single-game top-ups, build the Liquipedia-only database with `uv run python scripts/002_load_liquipedia.py` before enrichment: the final rebuild removes series without any resolved winner.

The HTTP client identifies dota2-model, accepts gzip, spaces requests by at least 1.1 seconds and retries 429/5xx with backoff, at most four attempts. The default run budget is 1,800 requests. Injected HTTP functions keep tests offline; the build never fetches. `PROMDOTA_DATA` controls the root.


With `OPENDOTA_API_KEY` set (gitignored `.env`; load it with `set -a; . ./.env; set +a`), requests carry `api_key`, are spaced 0.1 s and a run may make 100,000 calls (pay per call, $0.01 per 100). Without it: 1.1 s and 1,800 a run (free tier, 2,000/day). The CLI hides traceback locals so the key never reaches a log.
## Database

`uv run bash scripts/setup_db.sh` rebuilds `db/dota2.db` offline. Tables: `events`, `teams`, `players`, `matches`, `games`, `rosters`, `player_games`, `opendota_teams`, `kalshi_markets`, `team_aliases`, `kalshi_links`. Foreign keys are enabled. Loaders print aggregate summaries; parse failures go beside the DB in `parse_errors.txt`.

Event IDs are page IDs; missing infobox fields inherit independently from cached ancestors. Numeric tiers 1/2/3–4 become tier1/tier2/tier3; others are unknown. `tier_type` retains qualifiers/showmatches/monthlies; `leagueid` is optional. Online/international/mode exclusions remain. Team/player IDs use deterministic hashes of their keys; Steam players have `steam:<account_id>` keys. Rosters retain Liquipedia player keys and display names.

Inline Match templates and MatchPage templates produce series with at least one game. Empty slots are skipped. A Match page belongs to the tournament/subpage whose Bracket or Matchlist contains its ten-character bracket ID; unowned pages are counted and skipped. Match-page ordinals are bracket position × 1,000 plus the sorted page-key rank. Match IDs retain deterministic page/team/time/ordinal hashing and duplicate rules; game IDs are match ID × 10 + order (1–9).

Inline `Map` winners supply `winner_source=liquipedia`, optional Radiant/Dire side, duration and match ID. Skipped/unfinished maps without playable content are omitted. `ApiMap` sets team1 to Dire when `reversed=true`, otherwise Radiant. OpenDota fills unresolved winners by side; disagreements retain Liquipedia's winner and increment conflicts. Thus a reversed game with `radiant_win=true` belongs to opponent2. Series scores and winners are recomputed from games; series without any resolved game stay with a NULL winner (`opendota games` reads their match IDs; ratings skip them) and are counted as `unresolved_matches`.

Known sides build counted `(od_team_id, team_id)` mappings in `opendota_teams`; these can resolve games with missing side information. Unknown sides cannot assign players. Slots below 128 are Radiant; other slots are Dire. `player_games` stores hero, kills/deaths/assists, GPM/XPM. Games without OpenDota data have no player stats. Dates convert listed zones to UTC; absent times use noon UTC and unknown zones are counted with `time_known=0`.

## Kalshi ↔ Liquipedia links

The rebuild loads catalogs from `kalshi/markets/{KXDOTA2GAME,KXDOTA2MAP}.json`; absent inputs load zero rows. Dota 2 rules supply tournament names and EDT/EST schedules, converted to UTC. Tickers supply team codes and game numbers. Kalshi “map N” targets game N; map-event series lookup replaces `KXDOTA2MAP-` with `KXDOTA2GAME-`.

`team_aliases` maps consistent competitor IDs using confident evidence; conflicts drop aliases. `kalshi_links` stores match/game identity, method and failure reason. Only nonexcluded events supply candidates. Candidates lie within ±30 hours of schedule, falling back to open time +24 hours. Exact, alias and anchor passes repeat; fuzzy matching requires both similarities ≥0.8. Anchors require one confirmed team unique in the window and a plausible opponent. Exact opponents take precedence; ambiguity stays unresolved. Generic normalization and thresholds remain. The tested academy-only overlap safeguard prevents unrelated academy teams from anchoring; there is no special 1WIN rule. Game links inherit series identity; absent games are unplayed. Binary settlements are checked against winners; `db/link_report.txt` records failures and mismatches.

## Model change rules

Do not tune or select on holdout. Stage 1 tunes on outcomes only, [2023-01-01,2025-11-01). Stage 2 freezes parameters and validates outcomes and Kalshi's tradeable quote, [2025-11-01,2026-07-01). Holdout is 2026-07-01 on, opened once. Tradeable quote: first hourly bid/ask at least 30 minutes after listing and at least 2 hours before start, spread ≤0.06. Use paired match-clustered intervals; require significant stage-1 gain and no stage-2 regression, including guarded sections: all, tier1, tier2, tier3, international. Benchmark (also the defaults): `uv run python scripts/evaluate_elo.py --models team_elo,player_glicko --report-models team_elo,player_glicko --layers none --tune-from 2023-01-01 --tune-to 2025-11-01 --validate-from 2025-11-01`.

- An added parameter, feature or layer also needs a stage-1 gain of at least 0.0005 log loss.
- A stage-2 gain is reported but never rescues a change that failed stage 1; don't tune on stage 2 to pass it.
- Removals ship when every guarded section's interval stays below +0.0005 on both stages (non-inferior).
- Every tested model idea goes in the [research ledger](../research/README.md), adopted or not, with its numbers; count the tests run against stage 2.
- Trading results are reported, not gates. Data fixes ship when correct and the benchmark doesn't get significantly worse.

## Ratings and benchmark

`uv run python scripts/evaluate_elo.py` reads `db/dota2.db` and writes `docs/elo_backtest.md`. The games-schema port is tested on synthetic databases. `--models` and `--report-models` default to team_elo,player_glicko; team_elo and `--baseline` (default player_glicko) are always tuned comparators. `--layers none` is identity. `--jobs` defaults to min(cpu,8); `--k-grid` overrides ordinary model K grids. `PINNED` fixes player_glicko at k=24, rd_new=280, rd_info=0.0625, fixed initialization, and player_glicko_rookie_weights at CANDIDATE below. `ADOPTED="player_glicko"` names the provisional baseline, not an empirical adoption claim. Pinned models score their fixed parameters unless `--full-grid` re-searches. `--write-weights` writes parameters, series temperatures and fit date to `promdota/ratings/elo_weights.json`. No network or new dependencies are needed.

`load_maps` retains its interface but joins games/matches/events, filters resolved game winners and excluded=0, and emits binary score1/score2/won, NULL map name and nullable series_won. Replay predicts before updating, ordered by UTC start, match_id and game order. `load_lineups` reads player_games and accepts only games with exactly five players on each side. Otherwise neither side has a current lineup. Player strength is mean starter rating; missing starters use the team's latest earlier lineup, then one namespaced pseudo-player keyed by team ID. New players initialize at 1500 or known teammates' mean.

Initial rating is 1500, scale 400; expectation is 1/(1+10^(−Δ/400)). Binary credit is game win/loss, updates ±K·(credit−expectation). EloModel retains optional margin credit (0.5±0.5·tanh(abs(score difference)/c)), but no registered model uses it. Round credit and its probability module are removed: Dota has no rounds.

Registry and grids:

- coin: constant 0.5; team_elo: binary team rating, K={16,24,32,48,64,96}.
- player_binary: same K grid, initialization fixed/teammates; player_binary_region adds region_k={2,4,8,16}.
- player_glicko: binary player rating with RD; K={16,24,32,48,64}, rd_new={160,200,240,280,350,450}, rd_info={0.03125,0.0625,0.125,0.25,0.5}, initialization fixed/teammates (300 candidates). player_region_glicko adds region_k={2,4}.
- Registered ladder variants (not adopted) player_glicko_rookie, player_glicko_weights, player_glicko_rookie_weights cross rookie_penalty={300,400,600,800,1200}, rookie_maps={200,400,800,1600}, and/or online_k/tier3_k={0.5,0.75,1}. Base parameters always come from PINNED["player_glicko"] when present. Without that pin, ordinary runs error with instructions to pin the base; only --full-grid crosses the full base grid with the adjustment grid. K overrides do not change a ladder's fixed base. No tau grid remains.
- New experimental variants fix every CANDIDATE value: k=24, new_player=fixed, rd_info=0.0625, rd_new=280, rookie_penalty=600, rookie_maps=800, online_k=tier3_k=0.75. player_glicko_rw_revert grids season_revert={0,0.1,0.2,0.35,0.5}, season_month={1,10}, inactive_half_life={0,180,365,730} (40 candidates). player_glicko_rw_tier_revert fixes revert_target=tier, grids season_revert={0.1,0.2,0.35,0.5}, season_month={1,10}, inactive_half_life={0} (8). player_glicko_rw_perf grids perf_k={1,2,3,5,7,10,15,20} (8). They search without --full-grid; player_glicko remains adopted.

RD starts at rd_new², grows rd_growth² per idle day capped at rd_new², scales updates by variance/rd_floor², and shrinks by inverse-variance information after updates. Defaults: new=280, floor=140, growth=10, info=0.125. Rookie discounts decay logarithmically with earlier games and affect effective strength, never directly subtract stored rating. Optional tier move adjustments remain available in EloModel but have no registered candidates. Online/tier3 K multipliers default to 1 and compound; missing online is treated as online.

Player reversion defaults off: season_revert=0 (range [0,1]), season_month=1 (integer 1–12), inactive_half_life=0 days (nonnegative), revert_target=init. At date d, r′=target+(r−target)·(1−season_revert)^s·0.5^(gap_days/inactive_half_life); omit the inactivity factor when disabled. s counts UTC first-of-season_month boundaries since the last update. Predictions do not store reversion; updates commit all reverted ratings simultaneously before computing expectations. Tier targets use the mean stored rating of players whose latest ranked section was the same tier1/tier2/tier3; unknown sections retain the previous tier. Players without update history are unaffected.

Performance bonuses default off (perf_k=0, nonnegative; perf_stat accepts only kda). KDA per minute is (kills+0.5·assists−deaths)/(duration_s/60). Expectation uses the hero EMA after ≥20 sightings, otherwise the global EMA, otherwise zero; α=0.01. Residuals are centred within each side, adding perf_k·residual before RD weighting, so bonuses sum to zero within a side before weighting. Missing stats or nonpositive/missing duration give no bonus; sides with fewer than two observations get no bonus. EMAs update only after all player updates. load_performance reads hero/stats once and shares them with worker initialization and final replays.

Region identity codes are EU, CIS, NA, SA, AS, OCE, AF; missing/other codes are unknown. Homes use earlier known non-international event-host game counts; ties retain the previous home. Regional Elo adds home offsets; only different known homes update offsets, preserving zero sum. Current hosts are recorded after updates.

Stage 1 tunes game log loss; earlier games seed history unless --seed-from limits it. Require seed-from ≤ tune-from < tune-to ≤ validate-from ≤ holdout. Only --holdout opens July 2026 onward. Series use the first game's chance and independent games in Bo1/Bo3/Bo5; Bo2, unknown/unsupported lengths and unresolved series are skipped. Kalshi's Bo2 market is three-way. Stage-1 Bo3/Bo5 temperatures use ≥30 series and a 0.40–1.50 grid; Bo1 stays 1; --no-series-temperature disables fitting. Reports show section metrics, coin and paired comparisons with 2,000 match-clustered bootstrap resamples, seed 0. `scripts/series_independence.py` uses the same game loader for calibration, second-game dependence and Bo3 decider diagnostics.

Kalshi kinds remain series (KXDOTA2GAME) and map (KXDOTA2MAP); report headings call map markets games. Absent Kalshi tables explicitly skip those sections while outcome stages run. Linked rows prefer team1 contracts and invert team2 quotes. Tradeable quote rules are above; hours24/hours6 use the last tight quote by those cutoffs, prestart the last valid quote by start. Missing links/aliases/candles skip rows. Game markets use the first game's pre-match chance. --robustness compares quote rules without retuning; --series-check adds diagnostics.

Returns buy the greater positive after-fee edge. Fees round up to cents per order. Flat stake is $1 plus fees; ROI divides profit by outlay. Kelly starts at $50 with Prometheus caps: 10% capital/$250 per fixture, $250/order, $1k exposure, $2k/day; same-day bets size on opening capital and settle together. Depth caps use half acceptable-price tape volume over six hours after quote; missing tape means no fills. Reports pair unlimited/depth-capped returns. Monthly logistic blends fit separate market/model coefficients by kind using earlier months from 2025-11-01, excluding holdout and later months; fewer than 100 training rows retain market unchanged and are excluded from blended metrics.

Layers fit exclusively on stage 1. regional fits logit(p′)=s·logit(p)+e[home1]−e[home2], seven zero-sum effects with ridge 4; fewer than 50 eligible cross-region rows is identity. Homes are causal and use the same resolved/nonexcluded game filter as replay. Calibration fits tier×online logit temperatures with ridge 4 toward T=1; groups below 300 rows stay identity. Form adds w·(form1−form2) to the base logit. Starter form is the mean of players’ normalized decayed KDA-per-minute sums/weights from earlier games; half-life H={3,5,8,12,20,40,80} counts player appearances, including null-stat appearances which decay weights without adding observations. History includes unscored games; incomplete 5v5 lineups receive no adjustment. Stage 1 alone selects H and fits w by logistic loss; later outcomes never fit the layer. Outputs clip to [1e-6,1−1e-6].

## Site feed

`promdota blend-artifact` writes `promdota/blend_artifact.json`: adopted-model benchmark series odds with stored stage-1 temperatures and tradeable quotes, oriented to team1. Monthly no-intercept fits from 2026-01-01 require 300 earlier series; no holdout exclusion. Prometheus packages a copy of this frozen artifact.

`export --candidates PATH` also atomically writes private `data/feed/candidates.json`, raw six-decimal series chances keyed by validated Kalshi rules names, with provenance. Only future upcoming known-best-of matches linked to both open contracts qualify; rules starts must agree within 18 hours of our start. All groups are `cs2-series`; Prometheus handles blending, edge, sizing and orders. `--no-fetch` emits no candidates.

`promdota feed-state` builds `feed/state.pkl.gz`: atomic gzip-6 pickle, version 1, replayed model/rated teams, temperatures, reconstructed finals/closes, match joins, lookups/aliases and data-through. Load only trusted internal snapshots; incompatible versions fail. `promdota export --state PATH` bypasses SQLite and candles; the DB wrapper remains available.

`promdota export [--out PATH] [--no-fetch]` atomically writes `PROMDOTA_DATA/feed/cs2.json` (default root `data/`) for Prometheus. Replays the adopted player_round_glicko_rookie_weights with its stored stage-1 weights; no refit. Upcoming named teams use latest rated lineups; unknown/even lengths emit null and use untempered Bo3 odds. Active DB events within the UTC date window supply revision-content queries in batches of 50. Raw snapshots go to `upcoming/latest.json.gz`; `--no-fetch` uses that snapshot and omits current prices. Raw Liquipedia/Kalshi caches stay read-only.

`predictions.json` saves upcoming calls by page/team IDs/ordinal, refreshes future calls and prunes disappeared future entries. Calls freeze once their saved start passes. Results join the closest unordered team pair within 36 hours once, flipping reversed probabilities; otherwise replay reconstructs them. Page results require a saved call. Missing started calls show live for six hours, then pending finals for seven days. Current Kalshi series prices use the offline linker's passes/window plus DB aliases, spread ≤0.10; finals use cached prestart candle mids. Only present sections are emitted. Ratings depend on crawl + setup_db freshness; tournaments absent from the DB are not scanned; TBD sides are omitted.
