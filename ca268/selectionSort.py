list = [34, 56, 12, 98, 1, 74, 7, 23, 3, 9]

for i in range(len(list)):
    smallest = i
    for j in range(i + 1, len(list)):
        if list[j] < list[smallest]:
            smallest = j

    tmp = list[smallest]
    list[smallest] = list[i]
    list[i] = tmp
    # list[i], list[smallest] = list[smallest], list[i]

print(list)

"""
everything before | is sorted
start with      = [34, 56, 12, 98, 1, 74, 7, 23, 3, 9]
first pass      = [1,| 56, 12, 98, 34, 74, 7, 23, 3, 9] start at 34, swap 34 and 1
second pass     = [1, 3,| 12, 98, 34, 74, 7, 23, 56, 9] start at 56, swap 56 and 3
third pass      = [1, 3, 7,| 98, 34, 74, 12, 23, 56, 9] start at 12, swap 12 and 7
fourth pass     = [1, 3, 7, 9,| 34, 74, 12, 23, 56, 98] start at 98, swap 98 and 9
fifth pass      = [1, 3, 7, 9, 12,| 74, 34, 23, 56, 98] start at 34, swap 34 and 12
sixth pass      = [1, 3, 7, 9, 12, 23,| 34, 74, 56, 98] start at 74, swap 74 and 23
seventh pass    = [1, 3, 7, 9, 12, 23, 34,| 74, 56, 98] start at 34, swap 34 and 34
eight pass      = [1, 3, 7, 9, 12, 23, 34, 56,| 74, 98] start at 74, swap 74 and 56
ninth pass      = [1, 3, 7, 9, 12, 23, 34, 56, 74,| 98] start at 74, swap 74 and 74
tenth pass      = [1, 3, 7, 9, 12, 23, 34, 56, 74, 98| ] start at 98, swap 98 and 98
"""