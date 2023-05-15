#
#   Return an empty list to get your list of numbers.
#
#   List of numbers:
#   [18, 12, 15, 23, 8, 20]
#
#   Then return a list of lists corresponding to the passes of an insertion sort on the numbers.
#

def solution():
    return [
        [12, 18],
        [12, 15, 18],
        [12, 15, 18, 23],
        [8, 12, 15, 18, 23],
        [8, 12, 15, 18, 20, 23]
    ]