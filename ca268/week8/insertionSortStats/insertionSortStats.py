def insertion_sort(lst):
    comparisons = 0
    swaps = 0
    # At each pass ensure that that section is sorted.
    for todo in range(1, len(lst)):
        # Find correct position for lst[todo].
        i = todo
        while i > 0 and lst[i] < lst[i-1]:
            lst[i], lst[i-1] = lst[i-1], lst[i] # Swap it down towards the correct position
            swaps += 1
            comparisons += 1
            i -= 1
        comparisons += int(i > 0)

    return (comparisons, swaps)


# folabi's attempt
# def insertion_sort(lst):
#     # At each pass ensure that that section is sorted.
#     a = 0
#     b = 0
#     for todo in range(1, len(lst)):
#         # Find correct position for lst[todo].
#         i = todo
#         while i > 0 and lst[i] < lst[i-1]:
#             a += 1
#             lst[i], lst[i-1] = lst[i-1], lst[i] # Swap it down towards the correct position
#             b += 1
#             i -= 1
#         a -= int(i > 0)
#     return(a, b)