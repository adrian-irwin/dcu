#!/usr/bin/env python3

import sys

lines = [l.strip() for l in sys.stdin if 100 > len(l) > 1]

for item in lines:
    letters = []
    for c in item:
        if c not in letters:
            letters.append(c)
    # print(letters)

    deletions = 0
    while len(letters) > 2:
        letters.pop()
        deletions += 1

    print(deletions)
