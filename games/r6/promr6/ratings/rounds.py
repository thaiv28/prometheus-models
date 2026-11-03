"""Independent-round first-to-target probability with R6 overtime.

At (target−1, target−1) overtime is first to target+1: the best two of three
rounds (8–6 or 8–7 in the 2023–2026 data; 9–7 appears in 22 of 66k maps).
"""

from functools import lru_cache


def map_win(e, target=7):
    """Map win probability; quantize round share to bound the DP cache."""
    if not 0 <= e <= 1:
        raise ValueError("round probability must be between 0 and 1")
    if isinstance(target, bool) or not isinstance(target, int) or target < 1:
        raise ValueError("target must be a positive integer")
    return _map_win(round(e, 4), target)


@lru_cache(maxsize=10001)
def _map_win(e, target):
    # Work backwards from the tied overtime state.
    p = [[0.0] * (target + 1) for _ in range(target + 1)]
    for b in range(target):
        p[target][b] = 1.0
    p[target - 1][target - 1] = e * e * (3 - 2 * e)
    for a in range(target - 1, -1, -1):
        for b in range(target - 1, -1, -1):
            if a != target - 1 or b != target - 1:
                p[a][b] = e * p[a + 1][b] + (1 - e) * p[a][b + 1]
    return p[0][0]
