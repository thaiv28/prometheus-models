"""Offline checks for the scheduled collector's storage safeguards."""

import json
import shutil
import subprocess
from pathlib import Path

WORKFLOW = Path(__file__).resolve().parents[3] / ".github/workflows/kalshi-collect.yml"


def test_kalshi_schedule_and_permissions():
    text = WORKFLOW.read_text()
    assert 'cron: "23 */6 * * *"' in text
    assert "workflow_dispatch:" in text
    assert "id-token: write" in text
    assert "if: github.ref == 'refs/heads/main'" in text


def test_kalshi_manifest_guard_and_upload():
    text = WORKFLOW.read_text()
    assert (
        'if [ ! -f data/kalshi/manifest.json ] && [ "$ALLOW_FULL" != "true" ]; then'
        in text
    )
    assert "github.event_name == 'workflow_dispatch' && inputs.allow_full" in text
    assert "Missing manifest.json: seed S3 first" in text
    assert "exit 1" in text
    assert "if: always() && steps.collect.outcome != 'skipped'" in text
    assert "aws s3 cp" in text
    assert "aws s3 sync data/kalshi" in text
    assert "aws s3 sync s3://" not in text
    assert "--delete" not in text


def test_site_workflow_guards():
    for name, cron, timeout in (
        ("refresh-db", "41 * * * *", 45),
        ("feed", "7 * * * *", 15),
    ):
        text = (WORKFLOW.parent / f"cs2-{name}.yml").read_text()
        assert f'cron: "{cron}"' in text
        assert "workflow_dispatch:" in text
        assert "if: github.ref == 'refs/heads/main'" in text
        assert "contents: read" in text
        assert "id-token: write" in text
        assert f"group: cs2-{name}" in text
        assert "cancel-in-progress: false" in text
        assert f"timeout-minutes: {timeout}" in text
        assert "role: ${{ secrets.AWS_ROLE_ARN }}" in text
        assert "uses: ./.github/actions/setup-game" in text
        assert "game: cs2" in text
        assert "aws-region: us-west-2" in setup_action()
        assert "uv sync --frozen --no-dev" in setup_action()
        assert "--delete" not in text


def test_refresh_storage_and_incremental_crawl():
    text = (WORKFLOW.parent / "cs2-refresh-db.yml").read_text()
    assert "actions/cache/restore@v4" in text
    assert "actions/cache/save@v4" in text
    assert "key: cs2-raw-${{ github.run_id }}" in text
    assert "restore-keys: cs2-raw-" in text
    assert "steps.crawl.outputs.changed == 'true'" in text
    assert "steps.raw.outputs.cache-matched-key" in text
    assert "find data/liquipedia data/kalshi -newer /tmp/raw-marker" in text
    assert "uv run promcs liquipedia crawl" in text
    assert "--full" not in text
    assert "s3://$BUCKET/cs2-model/liquipedia" in text
    assert "s3://$BUCKET/cs2-model/kalshi" in text
    assert '--exclude "books/*"' in text
    assert "--size-only" in text
    assert "bash scripts/setup_db.sh" in text
    assert "uv run promcs feed-state" in text
    assert "s3://$BUCKET/cs2-model/feed/state.pkl.gz" in text


def test_feed_storage_and_dispatch():
    text = (WORKFLOW.parent / "cs2-feed.yml").read_text()
    assert "s3://$BUCKET/cs2-model/feed/state.pkl.gz" in text
    assert "run refresh-db first" in text
    assert "bash scripts/feed_data.sh restore" in text
    assert "bash scripts/feed_data.sh save" in text
    assert "cs2-model/feed/upcoming/latest.json.gz" in text
    assert (
        "uv run promcs export --state data/feed/state.pkl.gz --out data/feed/cs2.json"
        in text
    )
    assert (
        "upload data/feed/candidates.json cs2-model/feed/candidates.json application/json"
        in text
    )
    assert "gzip -n -9 -c" in text
    assert "cs2-model/feed/cs2.json.gz" in text
    assert "--content-type application/json" in text
    assert "gh workflow run games.yml -R thaiv28/Prometheus --ref main" in text
    assert "if: env.HAS_DISPATCH == 'true'" in text
    assert "HAS_DISPATCH: ${{ secrets.PROMETHEUS_DISPATCH_TOKEN != '' }}" in text
    assert "GH_TOKEN: ${{ secrets.PROMETHEUS_DISPATCH_TOKEN }}" in text
    assert "continue-on-error: true" in text
    assert "setup_db.sh" not in text
    assert "PROMCS_DATA" not in text


def test_feed_data_bash_syntax():
    import subprocess

    subprocess.run(
        ["bash", "-n", str(WORKFLOW.parents[2] / "games/cs2/scripts/feed_data.sh")],
        check=True,
    )


def refresh_steps():
    text = (WORKFLOW.parent / "cs2-refresh-db.yml").read_text()
    return text.split("      - ")[1:]


def test_refresh_database_input_cache():
    steps = refresh_steps()
    inputs = next(step for step in steps if "id: inputs\n" in step)
    assert (
        "hashFiles('games/cs2/scripts/**', 'games/cs2/promcs/**', 'games/cs2/uv.lock')"
        in inputs
    )
    assert (
        "{ find data/liquipedia data/kalshi -type f -not -path '*/books/*' "
        "-print0; find data/kaggle -name '*.zip' -print0; } "
        "| LC_ALL=C sort -z | xargs -0 sha256sum" in inputs
    )
    # The daily last_checked marker must not force a rebuild; the fetch runs first.
    kaggle = next(step for step in steps if "promcs kaggle fetch" in step)
    assert steps.index(kaggle) < steps.index(inputs)
    assert "printf '%s\\n' \"$CODE_HASH\"" in inputs
    assert "sha256sum" in inputs
    caches = [step for step in steps if "key: cs2-db-" in step]
    assert len(caches) == 2
    for step in caches:
        assert "path: games/cs2/db\n" in step
        assert "key: cs2-db-${{ steps.inputs.outputs.hash }}" in step
        assert "restore-keys:" not in step
    assert "actions/cache/restore@v4" in caches[0]
    assert "actions/cache/save@v4" in caches[1]


def test_refresh_rebuild_requires_cache_and_published_state():
    steps = refresh_steps()
    skip = next(step for step in steps if "id: skip\n" in step)
    assert "steps.database.outputs.cache-hit" in skip
    assert "--key cs2-model/feed/state.pkl.gz --query Metadata.inputs" in skip
    assert 'if [ "$DB_HIT" = true ] && [ "$published" = "$INPUTS" ]; then' in skip
    assert "Unchanged inputs; skipped rebuild" in skip
    for command in (
        "bash scripts/setup_db.sh",
        "uv run promcs feed-state",
        "actions/cache/save@v4\n",
        "uv run promcs blend-artifact",
    ):
        matching = [
            step for step in steps if command in step and "key: cs2-raw-" not in step
        ]
        assert len(matching) == 1
        assert "if: steps.skip.outputs.unchanged != 'true'" in matching[0]
    state = next(step for step in steps if "uv run promcs feed-state" in step)
    assert '--metadata inputs="$INPUTS"' in state
    artifact = next(step for step in steps if "uv run promcs blend-artifact" in step)
    assert "--out data/feed/blend_artifact.json" in artifact
    assert (
        'aws s3 cp data/feed/blend_artifact.json "s3://$BUCKET/cs2-model/feed/blend_artifact.json" --content-type application/json --only-show-errors'
        in artifact
    )
    assert "Artifact snapshots:" in artifact
    assert "DB build:" in skip
    assert "Raw cache:" in skip
    assert "DB cache:" in skip


def test_refresh_seed_guards_and_raw_save_order():
    steps = refresh_steps()
    download = next(step for step in steps if "name: Seed cold raw cache" in step)
    assert "if: steps.raw.outputs.cache-matched-key == ''" in download
    assert "continue-on-error: true" in download
    assert (
        'aws s3 cp "s3://$BUCKET/cs2-model/seed/raw.tar.zst" - | tar -I zstd -xf -'
        in download
    )
    crawl = next(step for step in steps if "id: crawl\n" in step)
    raw_save = next(step for step in steps if "id: raw-save\n" in step)
    weekly = next(step for step in steps if "name: Refresh weekly seed" in step)
    build = next(step for step in steps if "bash scripts/setup_db.sh" in step)
    assert steps.index(download) < steps.index(crawl) < steps.index(raw_save)
    assert steps.index(raw_save) < steps.index(build)
    assert "if: steps.crawl.outputs.changed == 'true'" in raw_save
    assert "if: steps.raw-save.outcome == 'success'" in weekly
    assert "continue-on-error: true" in weekly
    assert "--key cs2-model/seed/raw.tar.zst --query LastModified" in weekly
    assert '[ -z "$modified" ]' in weekly
    assert "-gt 604800" in weekly
    assert "tar -I 'zstd -T0 -3' -cf - --exclude='*/books/*'" in weekly
    assert "--expected-size 3000000000 --only-show-errors" in weekly


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
        Path(__file__).resolve().parents[3] / ".github/workflows/cs2-feed.yml"
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


def test_feed_gate_precedes_dependencies_and_full_checkout():
    text = (WORKFLOW.parent / "cs2-feed.yml").read_text()
    for required in (
        "timeout-minutes: 15",
        "sparse-checkout: |",
        "/games/cs2/scripts/feed_gate.py",
        "/.github/actions/*",
        "sparse-checkout-cone-mode: false",
        "fetch-depth: 1",
        "clean: false",
        "python3 scripts/feed_gate.py --gate data/feed/gate.json --snapshot data/feed/upcoming/latest.json.gz",
        "cs2-model/feed/gate.json",
        "cs2-model/feed/upcoming/latest.json.gz",
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
                str(WORKFLOW.parent / "cs2-feed.yml"),
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


def test_gate_tracks_ratings_etag_and_guards_all_full_run_steps():
    text = (
        Path(__file__).resolve().parents[3] / ".github/workflows/cs2-feed.yml"
    ).read_text()
    check = text.split("id: gate\n", 1)[1].split("      - name:", 1)[0]
    assert (
        "--key cs2-model/feed/state.pkl.gz --query ETag --output text 2>/dev/null || true"
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
