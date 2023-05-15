#!/usr/bin/env python3

# for every line in input, split both words into list
# seperate the two words into their own variables
# first = letter
# second = word
# searching for letters in first that are also in second.
# if all letters from first are in second then print true, else false.

# for every letter in first search for it in second, if found remove it from second

import sys

def contains(letters, word):
    for c in letters:
        # print("looking for =", c)
        if c in word:
            # print("searching =", s)
            word = word.replace(c, "", 1)
        else:
            return False
    return True

for line in sys.stdin:
    words = line.strip().split()
    letters = words[0].lower()
    word = words[1].lower()

    print(contains(letters, word))
