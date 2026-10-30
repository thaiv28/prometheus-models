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
    for name, cron in (("refresh-db", "41 * * * *"), ("feed", "7 * * * *")):
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
        'date -u +%H)" = "03"',
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
        "gzip -9 -c",
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
    ):
        assert required in script
