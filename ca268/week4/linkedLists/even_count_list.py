# Write a count_even function which takes a linked list of integers as an argument and counts the number of even elements in the list

def even_count(lst):
    total = 0
    i = lst.head
    while i != None:
        if i.item % 2 == 0:
            total += 1
        i = i.next
    return total
