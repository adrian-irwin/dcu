#!/usr/bin/env python3

import sys

for word in sys.stdin:
    word = word.strip()
    if len(word) % 2 == 1:
        middle = len(word) // 2
        print(word[middle])
    else:
        print("No middle character!")
