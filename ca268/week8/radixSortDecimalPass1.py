#
#   Return an empty list to get your list of numbers.
#
#   Then return a list of 10 lists representing the buckets
#

# Your list is: [52, 88, 290, 33, 189, 98, 256, 223, 274, 257, 18]

def sol():
    return [[290], [], [52], [33, 223], [274], [], [256], [257], [88, 98, 18], [189]]


# [0] [1] [2] [3] [4] [5] [6] [7] [8] [9]
# [290] [] [52] [33, 223] [274] [] [256] [257] [88, 98, 18] [189]
# [] [] [] [] [] [] [] [] [] []
# [] [] [] [] [] [] [] [] [] []