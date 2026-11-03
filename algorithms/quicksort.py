def partition(values, lo, hi):
    """Partition values[lo:hi] using the first value as the pivot.

    Values before the returned pivot index are strictly smaller than the
    pivot; values after it are greater than or equal to the pivot.
    The interval is half-open: lo is included and hi is excluded.
    """
    pivot = values[lo]
    boundary = lo

    for scan in range(lo + 1, hi):
        if values[scan] < pivot:
            boundary += 1
            values[boundary], values[scan] = values[scan], values[boundary]

    values[lo], values[boundary] = values[boundary], values[lo]
    return boundary


def quicksort(values, lo=0, hi=None):
    """Sort values in place with recursive quicksort; return the same list."""
    if hi is None:
        hi = len(values)

    if hi - lo <= 1:
        return values

    pivot_index = partition(values, lo, hi)
    quicksort(values, lo, pivot_index)
    quicksort(values, pivot_index + 1, hi)
    return values
