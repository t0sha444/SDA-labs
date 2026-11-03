def binary_search(values, target):
    """Return target's index in a sorted list, or -1 when it is absent.

    Uses a half-open search interval [lo, hi) and constant extra space.
    """
    lo = 0
    hi = len(values)

    while lo < hi:
        mid = lo + (hi - lo) // 2

        if values[mid] == target:
            return mid
        if values[mid] < target:
            lo = mid + 1
        else:
            hi = mid

    return -1


def search_insert_position(values, target):
    """Return the first index whose value is >= target, or len(values)."""
    lo = 0
    hi = len(values)

    while lo < hi:
        mid = lo + (hi - lo) // 2

        if values[mid] < target:
            lo = mid + 1
        else:
            hi = mid

    return lo
