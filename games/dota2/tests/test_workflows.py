"""Offline storage, schedule and command guards for production workflows."""

import json
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github/workflows"


def test_yaml_and_shell_parse():
    if not shutil.which("ruby"):
        pytest.skip("Ruby's standard-library YAML parser is unavailable")
    parsed = subprocess.run(
        [
            "ruby",
            "-rpsych",
            "-rjson",
            "-e",
            "puts JSON.generate(ARGV.map { |p| Psych.load_file(p) })",
            *map(str, WORKFLOWS.glob("*.yml")),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    for workflow in json.loads(parsed.stdout):
        for job in workflow["jobs"].values():
            for step in job["steps"]:
                if "run" in step:
                    subprocess.run(
                        ["bash", "-n"], input=step["run"], text=True, check=True
                    )
    subprocess.run(["bash", "-n", str(ROOT / "scripts/feed_data.sh")], check=True)


def test_site_workflow_guards():
    for name, cron in (("refresh-db", "41 */6 * * *"), ("feed", "37 * * * *")):
        text = (WORKFLOWS / f"{name}.yml").read_text()
        for required in (
            f'cron: "{cron}"',
            "workflow_dispatch:",
            "id-token: write",
            "if: github.ref == 'refs/heads/main'",
            f"group: {name}",
            "cancel-in-progress: false",
            "secrets.AWS_ROLE_ARN",
            "vars.DATA_BACKUP_BUCKET",
            "aws-region: us-west-2",
        ):
            assert required in text
        assert "--delete" not in text


def test_refresh_inputs_and_optional_opendota():
    text = (WORKFLOWS / "refresh-db.yml").read_text()
    for required in (
        "promdota liquipedia crawl --listing none",
        "promdota liquipedia crawl --listing full",
        'date -u +%H)" =~ ^0[345]$',
        'promdota opendota bulk --from "$month"',
        "promdota opendota games --limit 1800",
        "secrets.OPENDOTA_API_KEY",
        'if [ "$HAS_OPENDOTA" = true ]',
        "-2 months",
        "scripts/setup_db.sh",
        "hashFiles('scripts/**', 'promdota/**', 'uv.lock')",
        "sha256sum",
        "key: db-${{ steps.inputs.outputs.hash }}",
        "key: db-${{ steps.final-inputs.outputs.hash }}",
        "Metadata.inputs",
        'if [ "$DB_HIT" = true ] && [ "$published" = "$INPUTS" ]',
        "promdota feed-state",
        "promdota blend-artifact",
        "--metadata inputs=",
        "dota2-model/feed/state.pkl.gz",
        "dota2-model/feed/blend_artifact.json",
        "dota2-model/seed/raw.tar.zst",
        "dota2-model/liquipedia",
        "dota2-model/opendota",
        "dota2-model/kalshi",
        '--exclude "books/*"',
        "actions/cache/restore@v4",
        "actions/cache/save@v4",
    ):
        assert required in text
    assert text.index("Hash final database inputs") > text.index(
        "promdota opendota games"
    )


def test_feed_is_database_free_and_persists_private_candidates():
    text = (WORKFLOWS / "feed.yml").read_text()
    for required in (
        "dota2-model/feed/state.pkl.gz",
        "dota2-model/feed/dota2.json.gz",
        "dota2-model/feed/candidates.json",
        "dota2-model/feed/upcoming",
        "bash scripts/feed_data.sh restore",
        "bash scripts/feed_data.sh save",
        "promdota export --state data/feed/state.pkl.gz",
        "gzip -n -9 -c",
        "secrets.PROMETHEUS_DISPATCH_TOKEN",
        "if: env.HAS_DISPATCH == 'true'",
        "gh workflow run games.yml -R thaiv28/Prometheus --ref main",
    ):
        assert required in text
    assert "setup_db.sh" not in text
    script = (ROOT / "scripts/feed_data.sh").read_text()
    for required in (
        "PROMDOTA_DATA",
        "dota2-model/feed/predictions.json",
        "--if-match",
        "--if-none-match",
        "Metadata.sha256",
        '--metadata sha256="$hash"',
        'if [ "$hash" = "$previous" ]',
    ):
        assert required in script


def test_feed_gate_precedes_dependencies_and_full_checkout():
    text = (WORKFLOWS / "feed.yml").read_text()
    for required in (
        "timeout-minutes: 10",
        "sparse-checkout: scripts/feed_gate.py",
        "sparse-checkout-cone-mode: false",
        "fetch-depth: 1",
        "clean: false",
        "python3 scripts/feed_gate.py --gate data/feed/gate.json --snapshot data/feed/upcoming/latest.json.gz",
        "dota2-model/feed/gate.json",
        "dota2-model/feed/upcoming/latest.json.gz",
        "--mark-export",
        "Metadata.sha256",
        '--metadata sha256="$hash"',
        'if [ "$hash" != "$previous" ]',
        "steps.upload.outputs.feed_changed == 'true'",
    ):
        assert required in text
    assert text.index("Restore gate inputs") < text.index("id: gate")
    assert text.index("id: gate") < text.index("Full checkout")
    assert text.index("Full checkout") < text.index("setup-uv")
    assert text.index("id: gate") < text.index("uv sync")
    assert text.index("upload data/feed/candidates.json") < text.index("--mark-export")
    assert text.index("upload data/feed/upcoming/latest.json.gz") < text.index(
        "--mark-export"
    )
    # Every step after the gate either saves its skipped state or needs a full run.
    if shutil.which("ruby"):
        parsed = subprocess.run(
            [
                "ruby",
                "-rpsych",
                "-rjson",
                "-e",
                "puts JSON.generate(Psych.load_file(ARGV[0]))",
                str(WORKFLOWS / "feed.yml"),
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        steps = json.loads(parsed.stdout)["jobs"]["feed"]["steps"]
        gate_index = next(i for i, step in enumerate(steps) if step.get("id") == "gate")
        for step in steps[gate_index + 1 :]:
            assert "if" in step
            if step.get("name") != "Dispatch Prometheus":
                assert "steps.gate.outputs.run" in step["if"]


def test_runtime_dependencies_and_cache():
    for name in ("feed", "refresh-db", "ci"):
        text = (WORKFLOWS / f"{name}.yml").read_text()
        assert "enable-cache: true" in text
        assert "cache-dependency-glob: uv.lock" in text
        if name != "ci":
            assert "uv sync --frozen --no-dev" in text
    assert "timeout-minutes: 45" in (WORKFLOWS / "refresh-db.yml").read_text()


def test_docs_only_ci_keeps_steering_check():
    text = (WORKFLOWS / "ci.yml").read_text()
    for required in (
        "changes:",
        "needs: changes",
        "github.event.pull_request.base.sha || github.event.before",
        "git diff --name-only -z",
        "git merge-base",
        'p.startswith(b"docs/")',
        'p.endswith(b".md")',
        "uv run ruff format --check && uv run ruff check",
        "if: needs.changes.outputs.docs_only == 'true'",
        "uv run pytest -q tests/test_steering.py",
        "if: needs.changes.outputs.docs_only != 'true'",
        "run: uv run pytest -q",
    ):
        assert required in text
    assert "paths-ignore" not in text
    assert "dorny/paths-filter" not in text


def test_refresh_rebuilds_after_top_up_only_when_games_were_saved():
    text = (ROOT / ".github/workflows/refresh-db.yml").read_text()
    top_up = text.index("promdota opendota games --limit 1800")
    assert "grep -qE 'saved=[1-9]' /tmp/games-summary" in text[top_up:]
    assert text[top_up:].index("saved=[1-9]") < text[top_up:].index("setup_db.sh")
