# Work log

## 2026-10-29 — Scaffold from cs2-model

Copied cs2-model `origin/main` (75bab17) per Prometheus `docs/playbooks/new_game.md`; package `promdota`, CLI `promdota`, DB `db/dota2.db`. Removed feed, trading, blend artifact, stored weights and their workflows/tests until the holdout gate passes. Product and Current state rewritten with the Phase 0 findings (Kalshi volumes, Liquipedia and OpenDota coverage, windows). Data and benchmark code are still CS2's. Checks: pytest (263 passed, 3 skipped), ruff.
