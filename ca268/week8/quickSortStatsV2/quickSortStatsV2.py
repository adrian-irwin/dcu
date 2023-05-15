#
#   qsort code and a partition function.
#
#   Modify the partition function so that it uses the middle element.
#
def partition(lst, lo, hi):
    global comparisons, moves

    midIndex = (lo + hi) // 2
    lst[midIndex], lst[lo] = lst[lo], lst[midIndex]
    moves += 3

    part = lo
    while lo < hi:
        comparisons += 2
        while lst[lo] <= lst[part] and lo < hi:
            comparisons += 1
            lo += 1
        while lst[hi] > lst[part]: # Don't have to check for hi >= 0 cos part is there as a sentinel.
            comparisons += 1
            hi -= 1

        if lo < hi:
            # Swap the two entries
            lst[hi], lst[lo] = lst[lo], lst[hi]
            moves += 3

    # Swap part into position
    comparisons += 1
    if lst[part] > lst[hi]: # (this may happen of the array is small (size 2))
        lst[part], lst[hi] = lst[hi], lst[part]
        moves += 3

    return hi

def rec_qsort(lst, lo, hi):
    global comparisons, moves
    if lo < hi:
        pivot = partition(lst, lo, hi)
        rec_qsort(lst, lo, pivot - 1)
        rec_qsort(lst, pivot + 1, hi)

def qsort(lst):
    global comparisons, moves
    comparisons = 0
    moves = 0
    rec_qsort(lst, 0, len(lst) - 1)
    return (comparisons, moves)