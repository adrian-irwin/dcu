
# # array = [7,3,12,8,43,81,9,46]
# array = [4,3,2,10,12,1,5,6]

# for i in range(1,len(array)):
#     yo = array[i]
#     j = i - 1
#     while j >= 0 and yo < array[j]:
#         array[j+1] = array[j]
#         j -= 1
#     array[j+1] = yo

# print(f"sorted array = {array}")


"""
everything before | is sorted
start with =    [34, 56, 12, 98, 1, 74, 7, 23, 3, 9]
first pass =    [34, 56,| 12, 98, 1, 74, 7, 23, 3, 9] 56 is greater than 34 so it stays the same
second pass =   [12, 34, 56,| 98, 1, 74, 7, 23, 3, 9] 12 is less than both 34 and 56
third pass =    [12, 34, 56, 98,| 1, 74, 7, 23, 3, 9] 98 is greater than 56 so it stays the same
fourth pass =   [1, 12, 34, 56, 98,| 74, 7, 23 ,3, 9] 1 is less than all the sorted
fifth pass =    [1, 12, 34, 56, 74, 98,| 7, 23 ,3, 9] 74 is less than 98 and greater than the rest so it goes before 98
sixth pass =    [1, 7, 12, 34, 56, 74, 98,| 23 ,3, 9] 7 is less than everything but 1
seventh pass =  [1, 7, 12, 23, 34, 56, 74, 98,| 3, 9] 23 less than 34 greater than 12
eighth pass =   [1, 3, 7, 12, 23, 34, 56, 74, 98,| 9] 2 less than 7 greater than 1
final pass =    [1, 3, 7, 9, 12, 23, 34, 56, 74, 98| ] 9 less than 12 greater than 7
"""

list = [34, 56, 12, 98, 1, 74, 7, 23, 3, 9]
for i in range(1, len(list)):
    j = i - 1
    tmp = list[i]
    while j >= 0 and list[j] > tmp:
        list[j+1] = list[j]
        j = j - 1
    list[j+1] = tmp
