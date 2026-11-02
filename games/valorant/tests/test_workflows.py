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


def test_site_workflow_safeguards():
    for name, cron, timeout in (
        ("refresh-db", "41 * * * *", 90),
        ("feed", "7 * * * *", 15),
    ):
        text = (WORKFLOW.parent / f"valorant-{name}.yml").read_text()
        assert f'cron: "{cron}"' in text
        assert "workflow_dispatch:" in text
        assert "contents: read" in text and "id-token: write" in text
        assert "if: github.ref == 'refs/heads/main'" in text
        assert f"group: valorant-{name}" in text
        assert "cancel-in-progress: false" in text
        assert f"timeout-minutes: {timeout}" in text
        assert "${{ vars.DATA_BACKUP_BUCKET }}" in text
        assert "${{ secrets.AWS_ROLE_ARN }}" in text
        assert "uses: ./.github/actions/setup-game" in text
        assert "game: valorant" in text
        assert "aws-region: us-west-2" in setup_action()
        assert "--delete" not in text
        assert "shell: bash" in text


def test_refresh_db_storage_and_incremental_crawl():
    text = (WORKFLOW.parent / "valorant-refresh-db.yml").read_text()
    assert "uv run promval vlr crawl --since 2021-01-01" in text
    assert "--full" not in text
    assert "bash scripts/setup_db.sh" in text
    assert "uv run promval feed-state" in text
    assert "s3://$BUCKET/valorant-model/vlr" in text
    assert "s3://$BUCKET/valorant-model/kalshi" in text
    assert "s3://$BUCKET/valorant-model/feed/state.pkl.gz" in text
    assert '--exclude "books/*"' in text
    assert "--size-only" in text
    assert "actions/cache/restore@v4" in text and "actions/cache/save@v4" in text
    # Save the raw cache before the DB build, so a slow build can't lose a seed.
    assert text.index("actions/cache/save@v4") < text.index("name: Build DB")
    assert text.count("key: valorant-raw-${{ github.run_id }}") == 2
    assert "restore-keys: valorant-raw-" in text
    assert "-newer" in text and "cache-matched-key" in text
    assert "if: steps.changed.outputs.save == 'true'" in text


def test_feed_storage_and_guarded_dispatch():
    text = (WORKFLOW.parent / "valorant-feed.yml").read_text()
    assert "PROMVAL_DATA" not in text
    assert "setup_db.sh" not in text
    assert "run refresh-db first" in text
    assert (
        "uv run promval export --state data/feed/state.pkl.gz --out data/feed/valorant.json"
        in text
    )
    for key in ("state.pkl.gz", "upcoming", "valorant.json.gz"):
        assert f"s3://$BUCKET/valorant-model/feed/{key}" in text
    assert "bash scripts/feed_data.sh restore" in text
    assert "bash scripts/feed_data.sh save" in text
    assert "--content-type application/json" in text
    assert (
        "upload data/feed/candidates.json valorant-model/feed/candidates.json application/json"
        in text
    )
    assert "--acl" not in text
    assert "gzip -n -9 -c" in text
    assert "HAS_DISPATCH: ${{ secrets.PROMETHEUS_DISPATCH_TOKEN != '' }}" in text
    assert "if: env.HAS_DISPATCH == 'true'" in text
    assert "GH_TOKEN: ${{ secrets.PROMETHEUS_DISPATCH_TOKEN }}" in text
    assert "continue-on-error: true" in text
    assert "gh workflow run games.yml -R thaiv28/Prometheus --ref main" in text


def test_feed_data_shell_syntax():
    import subprocess

    script = WORKFLOW.parents[2] / "games/valorant/scripts/feed_data.sh"
    subprocess.run(["bash", "-n", str(script)], check=True)
    text = script.read_text()
    assert "valorant-model/feed/predictions.json" in text
    assert "--if-match" in text and "--if-none-match" in text


def test_refresh_db_input_hash_and_exact_cache():
    text = (WORKFLOW.parent / "valorant-refresh-db.yml").read_text()
    assert (
        "hashFiles('games/valorant/scripts/**', 'games/valorant/promval/**', 'games/valorant/uv.lock')"
        in text
    )
    assert (
        "find data/vlr data/kalshi -type f -not -path '*/books/*' "
        "-not -path 'data/vlr/parsed/*' -print0 | LC_ALL=C sort -z | xargs -0 sha256sum"
        in text
    )
    assert "xargs -0 sha256sum; printf" in text
    assert "sha256sum" in text
    assert text.count("key: valorant-db-${{ steps.inputs.outputs.hash }}") == 2
    restore = text.split("id: db\n", 1)[1].split("      - name:", 1)[0]
    assert "path: games/valorant/db" in restore
    assert "restore-keys:" not in restore
    assert text.index("name: Crawl") < text.index("name: Hash DB inputs")


def test_refresh_db_skip_requires_cache_and_matching_state():
    text = (WORKFLOW.parent / "valorant-refresh-db.yml").read_text()
    assert "DB_CACHE_HIT: ${{ steps.db.outputs.cache-hit }}" in text
    guard = text.split("name: Check rebuild", 1)[1].split("name: Build DB", 1)[0]
    assert 'if [ "$DB_CACHE_HIT" = "true" ]; then' in guard
    assert "--key valorant-model/feed/state.pkl.gz --query Metadata.inputs" in guard
    assert 'if [ "$state_inputs" = "$INPUTS" ]; then' in guard
    assert 'echo "skip=true" >> "$GITHUB_OUTPUT"' in guard
    assert "Unchanged inputs; skipped rebuild" in guard
    for step in ("Build DB", "Save ratings snapshot", "Publish blend artifact"):
        block = text.split(f"name: {step}\n", 1)[1].split("      - ", 1)[0]
        assert "if: steps.rebuild.outputs.skip != 'true'" in block
    save = text.rsplit("uses: actions/cache/save@v4", 1)[1]
    assert "if: steps.rebuild.outputs.skip != 'true'" in save
    assert '--metadata inputs="$INPUTS"' in text
    assert "uv run promval blend-artifact --out data/feed/blend_artifact.json" in text
    assert (
        'aws s3 cp data/feed/blend_artifact.json "s3://$BUCKET/valorant-model/feed/blend_artifact.json" --content-type application/json --only-show-errors'
        in text
    )
    assert "promval/blend_artifact.json" not in text


def test_refresh_db_cold_and_weekly_seeds():
    text = (WORKFLOW.parent / "valorant-refresh-db.yml").read_text()
    seed = text.split("name: Seed cold raw cache\n", 1)[1].split("      - name:", 1)[0]
    assert "if: steps.raw.outputs.cache-matched-key == ''" in seed
    assert "continue-on-error: true" in seed
    assert (
        'aws s3 cp "s3://$BUCKET/valorant-model/seed/raw.tar.zst" - | tar -I zstd -xf -'
        in seed
    )
    assert text.index("name: Seed cold raw cache") < text.index(
        "name: Top up raw cache"
    )
    assert text.index("name: Top up raw cache") < text.index("find data/vlr/parsed")
    weekly = text.split("name: Refresh weekly raw seed\n", 1)[1].split(
        "      - name:", 1
    )[0]
    assert "if: steps.raw_save.outcome == 'success'" in weekly
    assert "id: raw_save" in text
    assert "continue-on-error: true" in weekly
    assert "--query LastModified" in weekly
    assert '[ -z "$modified" ]' in weekly
    assert "-gt 604800" in weekly
    assert (
        "tar -I 'zstd -T0 -3' -cf - --exclude='*/books/*' data/vlr data/kalshi"
        in weekly
    )
    assert "--expected-size 3000000000" in weekly
    assert text.index("id: raw_save") < text.index("name: Build DB")


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
        Path(__file__).resolve().parents[3] / ".github/workflows/valorant-feed.yml"
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
    text = (WORKFLOW.parent / "valorant-feed.yml").read_text()
    for required in (
        "timeout-minutes: 15",
        "sparse-checkout: |",
        "/games/valorant/scripts/feed_gate.py",
        "/.github/actions/*",
        "sparse-checkout-cone-mode: false",
        "fetch-depth: 1",
        "clean: false",
        "python3 scripts/feed_gate.py --gate data/feed/gate.json --snapshot data/feed/valorant.json.gz",
        "valorant-model/feed/gate.json",
        "valorant-model/feed/valorant.json.gz",
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
    assert text.index("upload data/feed/valorant.json.gz") < text.index("--mark-export")
    # Every step after the gate either saves its skipped state or needs a full run.
    if shutil.which("ruby"):
        parsed = subprocess.run(
            [
                "ruby",
                "-rpsych",
                "-rjson",
                "-e",
                "puts JSON.generate(Psych.load_file(ARGV[0]))",
                str(WORKFLOW.parent / "valorant-feed.yml"),
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
        Path(__file__).resolve().parents[3] / ".github/workflows/valorant-feed.yml"
    ).read_text()
    check = text.split("id: gate\n", 1)[1].split("      - name:", 1)[0]
    assert (
        "--key valorant-model/feed/state.pkl.gz --query ETag --output text 2>/dev/null || true"
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
