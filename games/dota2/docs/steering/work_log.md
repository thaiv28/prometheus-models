## 2026-10-29 — Dota 2 data layer

Converted Liquipedia crawling/parsing to Dota tournaments and Match pages; added projected OpenDota bulk/single caches and offline winner/player enrichment. Replaced maps with games, ported Kalshi Dota loading/linking, and updated steering docs. Checks: `UV_NO_SYNC=1 uv run pytest -q` (127 passed, 117 requested Phase 3 skips), Ruff format/check, diff whitespace and CLI help passed. The full temporary-cache setup_db test verifies reversed Vici winner, ten players and four Kalshi markets. Baseline archive: 263 passed, 3 skipped in 12.40s; current suite 1.14s, with Phase 3 coverage deferred. Plain uv sync panics in this sandbox; the already-synced environment works with UV_NO_SYNC. Unresolved series now stay with a NULL winner, so `opendota games` finds their match IDs after a rebuild. Real crawl pending.

## 2026-10-29 — Scaffold from cs2-model

Copied cs2-model `origin/main` (75bab17) per Prometheus `docs/playbooks/new_game.md`; package `promdota`, CLI `promdota`, DB `db/dota2.db`. Removed feed, trading, blend artifact, stored weights and their workflows/tests until the holdout gate passes. Product and Current state rewritten with the Phase 0 findings (Kalshi volumes, Liquipedia and OpenDota coverage, windows). Data and benchmark code are still CS2's. Checks: pytest (263 passed, 3 skipped), ruff.
