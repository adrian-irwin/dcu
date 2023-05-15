#!/usr/bin/env python3

import sys

for word in sys.stdin:
    word = word.strip()
    choppedWord = word[1:-1]
    if len(choppedWord) > 0:
        print(choppedWord)
