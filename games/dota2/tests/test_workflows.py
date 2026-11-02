"""Offline storage, schedule and command guards for production workflows."""

import json
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = Path(__file__).resolve().parents[3] / ".github/workflows"


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
            *map(
                str,
                [
                    *WORKFLOWS.glob("dota2-*.yml"),
                    WORKFLOWS / "ci.yml",
                    WORKFLOWS / "kalshi-collect.yml",
                ],
            ),
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
        text = (WORKFLOWS / f"dota2-{name}.yml").read_text()
        for required in (
            f'cron: "{cron}"',
            "workflow_dispatch:",
            "id-token: write",
            "if: github.ref == 'refs/heads/main'",
            f"group: dota2-{name}",
            "cancel-in-progress: false",
            "secrets.AWS_ROLE_ARN",
            "vars.DATA_BACKUP_BUCKET",
            "uses: ./.github/actions/setup-game",
            "game: dota2",
        ):
            assert required in text
        assert "--delete" not in text


def test_refresh_inputs_and_optional_opendota():
    text = (WORKFLOWS / "dota2-refresh-db.yml").read_text()
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
        "hashFiles('games/dota2/scripts/**', 'games/dota2/promdota/**', 'games/dota2/uv.lock')",
        "sha256sum",
        "key: dota2-db-${{ steps.inputs.outputs.hash }}",
        "key: dota2-db-${{ steps.final-inputs.outputs.hash }}",
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
    text = (WORKFLOWS / "dota2-feed.yml").read_text()
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
    text = (WORKFLOWS / "dota2-feed.yml").read_text()
    for required in (
        "timeout-minutes: 10",
        "sparse-checkout: |",
        "/games/dota2/scripts/feed_gate.py",
        "/.github/actions/*",
        "sparse-checkout-cone-mode: false",
        "fetch-depth: 1",
        "clean: false",
        "python3 scripts/feed_gate.py --gate data/feed/gate.json --snapshot data/feed/upcoming/latest.json.gz",
        "dota2-model/feed/gate.json",
        "dota2-model/feed/upcoming/latest.json.gz",
        "--mark-export",
        "Metadata.sha256",
        'metadata="sha256=$hash"',
        'if [ "$hash" != "$previous" ]',
        "steps.upload.outputs.feed_changed == 'true'",
    ):
        assert required in text
    initial_setup = text.split("uses: ./.github/actions/setup-game", 1)[1].split(
        "      - ", 1
    )[0]
    assert "install: 'false'" in initial_setup
    assert "role: ${{ secrets.AWS_ROLE_ARN }}" in initial_setup
    full_setup = text.rsplit("uses: ./.github/actions/setup-game", 1)[1].split(
        "      - ", 1
    )[0]
    assert "if: steps.gate.outputs.run == 'true'" in full_setup
    assert "role:" not in full_setup
    assert text.count("/.github/actions/*") == 2
    assert text.index("Restore gate inputs") < text.index("id: gate")
    assert text.index("id: gate") < text.index("Full checkout")
    assert text.index("Full checkout") < text.rindex(
        "uses: ./.github/actions/setup-game"
    )
    assert text.index("id: gate") < text.rindex("uses: ./.github/actions/setup-game")
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
                str(WORKFLOWS / "dota2-feed.yml"),
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
        text = (
            WORKFLOWS / ("ci.yml" if name == "ci" else f"dota2-{name}.yml")
        ).read_text()
        runtime = text if name == "ci" else setup_action()
        assert "enable-cache: true" in runtime
        dependency = (
            "games/${{ matrix.game }}/uv.lock"
            if name == "ci"
            else "games/${{ inputs.game }}/uv.lock"
        )
        assert f"cache-dependency-glob: {dependency}" in runtime
        if name != "ci":
            assert "uv sync --frozen --no-dev" in runtime
            assert "uses: ./.github/actions/setup-game" in text
            assert "game: dota2" in text
    assert "timeout-minutes: 45" in (WORKFLOWS / "dota2-refresh-db.yml").read_text()


def test_docs_only_ci_keeps_steering_check():
    text = (WORKFLOWS / "ci.yml").read_text()
    for required in (
        'out.append({"game": g, "docs_only": docs_only})',
        "changes:",
        "needs: changes",
        "github.event.pull_request.base.sha || github.event.before",
        "git diff --name-only",
        "git merge-base",
        'p.startswith("docs/")',
        'p.endswith(".md")',
        "uv run ruff format --check && uv run ruff check",
        "if: matrix.docs_only",
        "uv run pytest -q tests/test_steering.py",
        "if: ${{ !matrix.docs_only }}",
        "run: uv run pytest -q",
    ):
        assert required in text
    assert "paths-ignore" not in text
    assert "dorny/paths-filter" not in text


def test_refresh_rebuilds_after_top_up_only_when_games_were_saved():
    text = (WORKFLOWS / "dota2-refresh-db.yml").read_text()
    top_up = text.index("promdota opendota games --limit 1800")
    assert "grep -qE 'saved=[1-9]' /tmp/games-summary" in text[top_up:]
    assert text[top_up:].index("saved=[1-9]") < text[top_up:].index("setup_db.sh")


def setup_action():
    return (
        Path(__file__).resolve().parents[3] / ".github/actions/setup-game/action.yml"
    ).read_text()


def test_shared_setup_preserves_runtime_cache_and_aws():
    text = setup_action()
    for required in (
        "name: Set up a game",
        "required: true",
        "default: ''",
        "default: 'true'",
        "using: composite",
        "astral-sh/setup-uv@v10.2.0",
        "enable-cache: true",
        "cache-dependency-glob: games/${{ inputs.game }}/uv.lock",
        "if: inputs.install == 'true'",
        "working-directory: games/${{ inputs.game }}",
        "shell: bash",
        "uv sync --frozen --no-dev",
        "if: inputs.role != ''",
        "aws-actions/configure-aws-credentials@v6",
        "role-to-assume: ${{ inputs.role }}",
        "aws-region: us-west-2",
    ):
        assert required in text
    assert text.index("uv sync") < text.index("configure-aws-credentials")


def test_shared_kalshi_matrix():
    text = (
        Path(__file__).resolve().parents[3] / ".github/workflows/kalshi-collect.yml"
    ).read_text()
    for required in (
        "name: Kalshi collect",
        "fail-fast: false",
        "group: kalshi-collect-${{ matrix.game }}",
        "cancel-in-progress: false",
        "working-directory: games/${{ matrix.game }}",
        "timeout-minutes: 30",
        "game: ${{ matrix.game }}",
        "role: ${{ secrets.AWS_ROLE_ARN }}",
        "uv run ${{ matrix.cli }} kalshi collect",
        "s3://$BUCKET/${{ matrix.game }}-model/kalshi",
        "if: always() && steps.collect.outcome != 'skipped' && steps.collect.outcome != ''",
    ):
        assert required in text
    for game, cli in (
        ("cs2", "promcs"),
        ("dota2", "promdota"),
        ("valorant", "promval"),
    ):
        assert f"- game: {game}\n            cli: {cli}" in text


def test_feed_dispatch_requires_content_change():
    text = (
        Path(__file__).resolve().parents[3] / ".github/workflows/dota2-feed.yml"
    ).read_text()
    assert "id: upload" in text
    assert "steps.upload.outputs.feed_changed == 'true'" in text
    assert "env.HAS_DISPATCH == 'true' &&" in text
    assert 'd.pop("generated",None)' in text
    assert "json.dumps(d,sort_keys=True)" in text
    assert """--query 'Metadata."content-sha256"'""" in text
    assert "content-sha256=" in text
    assert 'if [ "$content_hash" != "$previous_content" ]; then' in text
    assert 'echo "feed_changed=true" >> "$GITHUB_OUTPUT"' in text


def test_gate_tracks_ratings_etag_and_guards_all_full_run_steps():
    text = (
        Path(__file__).resolve().parents[3] / ".github/workflows/dota2-feed.yml"
    ).read_text()
    check = text.split("id: gate\n", 1)[1].split("      - name:", 1)[0]
    assert (
        "--key dota2-model/feed/state.pkl.gz --query ETag --output text 2>/dev/null || true"
        in check
    )
    assert '--state-etag "$state_etag"' in check
    assert 'echo "state_etag=$state_etag" >> "$GITHUB_OUTPUT"' in check
    assert "STATE_ETAG: ${{ steps.gate.outputs.state_etag }}" in text
    assert '--state-etag "$STATE_ETAG" --mark-export' in text
    assert "install: 'false'" in text
    assert "/.github/actions/*" in text
    after_gate = text.split("      - name: Save unchanged gate", 1)[1]
    steps = after_gate.split("      - ")
    assert "if: steps.gate.outputs.run == 'false'" in steps[0]
    assert 'if [ "$hash" != "$previous" ]' in steps[0]
    for step in steps[1:]:
        assert "steps.gate.outputs.run == 'true'" in step
