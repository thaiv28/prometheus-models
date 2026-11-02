"""Fetch caller-supplied match IDs, retaining raw pages before parsing."""

from dataclasses import dataclass
from datetime import UTC, datetime
from http.client import HTTPException

from promr6.siegegg import cache, http
from promr6.siegegg.parse import parse_match


@dataclass
class Summary:
    requested: int = 0
    cached: int = 0
    fetched: int = 0
    not_found: int = 0
    errors: int = 0


def fetch_matches(ids, get=http.get, refresh=False, limit=None) -> Summary:
    """Limit newly attempted IDs; cached IDs consume no request allowance."""
    if limit is not None and limit < 0:
        raise ValueError("limit must be nonnegative")
    index = cache.read_index()
    summary = Summary()
    attempted = 0
    seen = set()
    for match_id in ids:
        match_id = int(match_id)
        if match_id <= 0:
            raise ValueError("match IDs must be positive")
        key = str(match_id)
        if key in seen:
            continue
        seen.add(key)
        old = index.get(key)
        if old and (old["finished"] or not refresh):
            summary.requested += 1
            summary.cached += 1
            continue
        if limit is not None and attempted >= limit:
            break
        summary.requested += 1
        attempted += 1
        try:
            status, final_url, body = get(f"{http.BASE}/matches/{match_id}")
            if status not in (200, 404):
                raise RuntimeError(f"siege.gg HTTP {status}")
            cache.save_match(match_id, body)
            # Metadata survives even when parsing fails; raw data remains reusable.
            index[key] = {
                "status": status,
                "url": final_url,
                "fetched_at": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
                "finished": False,
            }
            cache.save_index(index)
            if status == 404:
                summary.not_found += 1
            else:
                match = parse_match(body)
                if match is None:
                    raise ValueError("response has no match overview")
                index[key]["finished"] = match.finished
                cache.save_index(index)
                summary.fetched += 1
        except (OSError, HTTPException, RuntimeError, ValueError):
            summary.errors += 1
    return summary
