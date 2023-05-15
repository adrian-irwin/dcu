# This problem is a non programming problem
#  Your list is: [18, 8, 15, 23, 12, 20]
#
# first pivot = 18, [8,15,12] 18 [23,20]
# second pivot = 8, [] 8 [15,12]
# third pivot = 15, [12] 15 []
# fourth pivot = 23, [20] 23 []
#
#
#
#
def solution():
    return [18, 12, 8, 23]


# partition code
def partition(lst, lo, hi):
    if len(lst) == 0: # if length of list = 0, dont sort
        return 0

    part = lo
    while lo < hi: # while lo is still less than hi loop
        while lst[lo] <= lst[part] and lo < hi: # if the element at index lo is less or equal to element at part add 1 to lo
            lo += 1
        while lst[hi] > lst[part]: # Don't have to check for hi >= 0 cos part is there as a sentinel.
            hi -= 1

        if lo < hi:
            # Swap the two entries
            lst[hi], lst[lo] = lst[lo], lst[hi]

    # Swap part into position
    if lst[part] > lst[hi]: # (this may happen of the array is small (size 2))
        lst[part], lst[hi] = lst[hi], lst[part]

    return hi

# quick sort code
def qsort(lst, lo, hi):
    if lo < hi:
        pivot = partition(lst, lo, hi)
        qsort(lst, lo, pivot - 1) # do the left
        qsort(lst, pivot + 1, hi) # do the right

# def rec_qsort(lst, lo, hi):
#     if lo < hi:
#         pivot = partition(lst, lo, hi)
#         rec_qsort(lst, lo, pivot - 1)
#         rec_qsort(lst, pivot + 1, hi)

# def qsort(lst):
#     rec_qsort(lst, 0, len(lst) - 1)

def main():
    line = [18, 8, 15, 23, 12, 20]
    items = line

    orig = list(items)

    result = qsort(items, 0, len(items) - 1)
    if items != sorted(orig):
        print("The list is not sorted.")
        print(f"The list looks like this: {items}")
    else:
        print(items)

if __name__ == "__main__":
    main()
