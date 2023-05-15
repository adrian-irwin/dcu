#!/usr/bin/env python3

import sys

def binarySearch(query, sorted_list):
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] < query:
            low = mid + 1
        elif sorted_list[mid] > query:
            high = mid - 1
        else:
            return True
    return False

lines = [word.strip() for word in sys.stdin]
words = sorted([word.lower() for word in lines if len(word) >= 5])
reversableWords = [word for word in lines if binarySearch(word[::-1].lower(), words)]

print(reversableWords)
