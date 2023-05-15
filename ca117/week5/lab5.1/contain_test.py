#!/usr/bin/env python3

import sys

# def contains(letters, word):
#     return 1 in [c in word for c in letters]

def contains(letters, word):
    for c in letters:
        if c in word:
            word = word.replace(c, "", 1)
        else:
            return False
    return True

words = [line.strip() for line in sys.stdin]
letters = ["e", "v", "i", "l"]

for word in words:
    if contains(letters, word.lower()):
        print(word)