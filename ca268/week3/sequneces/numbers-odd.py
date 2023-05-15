# Write a function called get_odd_list which returns a list of odd numbers.
# The function should read numbers from standard input until one of the numbers is -1.
# The function should only add odd numbers to the list.

import sys

def get_odd_list():
    odds = []
    n = int(sys.stdin.readline())
    while n != -1:
        if n % 2 == 1:
            odds.append(n)
        n = int(sys.stdin.readline())
    return odds
