# Write a function which will read the input until terminated by -1 and create two lists, one to hold the odd numbers and one to hold the even numbers.
# The function should return both these lists as a tuple, the odd list followed by the even list.

import sys

def get_evenodd_list():
    odds = []
    evens = []
    n = int(sys.stdin.readline())
    while n != -1:
        if n % 2 == 1:
            odds.append(n)
        else:
            evens.append(n)
        n = int(sys.stdin.readline())
    return odds, evens
