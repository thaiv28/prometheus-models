#!/usr/bin/env bash
# Restore/save the feed log, with atomic S3 concurrency checks.
set -euo pipefail

root="${PROMDOTA_DATA:-data}"
LOG="$root/feed/predictions.json"
STATE="$root/feed/.predictions-etag"
bucket="${DATA_BACKUP_BUCKET:-${BUCKET:?set DATA_BACKUP_BUCKET or BUCKET}}"
key=dota2-model/feed/predictions.json

etag() {
    local out
    if out=$(aws s3api head-object --bucket "$bucket" --key "$key" --query ETag --output text 2>&1); then
        echo "$out"
    elif grep -q "(404)" <<<"$out"; then
        echo ""
    else
        echo "::error::Can't read prediction log: $out" >&2
        return 1
    fi
}

case "${1:-}" in
restore)
    mkdir -p "$root/feed"
    tag=$(etag)
    if [ -z "$tag" ]; then
        rm -f "$LOG"
        : > "$STATE"
        echo "No saved prediction log yet."
        exit 0
    fi
    aws s3api get-object --bucket "$bucket" --key "$key" --if-match "$tag" "$LOG" >/dev/null
    echo "$tag" > "$STATE"
    echo "Restored prediction log."
    ;;
save)
    [ -f "$LOG" ] || { echo "No prediction log to save."; exit 0; }
    [ -f "$STATE" ] || { echo "::error::Restore prediction log before saving."; exit 1; }
    restored=$(cat "$STATE")
    current=$(etag)
    if [ "$current" != "$restored" ]; then
        echo "::warning::Prediction log changed since restore; skipping save."
        exit 0
    fi
    hash=$(sha256sum "$LOG" | cut -d ' ' -f 1)
    previous=$(aws s3api head-object --bucket "$bucket" --key "$key" --query Metadata.sha256 --output text 2>/dev/null || true)
    if [ "$hash" = "$previous" ]; then
        echo "Prediction log unchanged; skipping save."
        exit 0
    fi
    condition=(--if-none-match '*')
    [ -z "$current" ] || condition=(--if-match "$current")
    if out=$(aws s3api put-object --bucket "$bucket" --key "$key" --body "$LOG" \
        --content-type application/json --metadata sha256="$hash" "${condition[@]}" 2>&1); then
        echo "Saved prediction log."
    elif grep -Eq 'PreconditionFailed|ConditionalRequestConflict|\(412\)|\(409\)' <<<"$out"; then
        echo "::warning::Prediction log changed during save; skipping save."
    else
        echo "::error::Can't save prediction log: $out" >&2
        exit 1
    fi
    ;;
*)
    echo "usage: $0 restore|save" >&2
    exit 2
    ;;
esac
