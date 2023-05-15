
def insertion_sort(lst):
    comparisons = 0
    moves = 0
    for todo in range(1, len(lst)):
        tobeinserted = lst[todo]
        i = todo
        while i > 0 and tobeinserted < lst[i-1]:
            comparisons += 1
            moves += 1
            lst[i] = lst[i-1] # Make space for the item
            i -= 1
        lst[i] = tobeinserted  # Found the place for this item, plonk it in
        comparisons += int(i > 0)
        moves += 2

    return (comparisons, moves)

# def insertion_sort(lst):
#     comparisons = 0
#     moves = 0
#     # At each pass ensure that that section is sorted.
#     for todo in range(1, len(lst)):
#         # Find correct position for lst[todo].
#         i = todo
#         while i > 0 and lst[i] < lst[i-1]:
#             lst[i], lst[i-1] = lst[i-1], lst[i] # Swap it down towards the correct position
#             moves += 1
#             comparisons += 1
#             i -= 1
#         comparisons += int(i > 0)

#     return (comparisons, moves)

