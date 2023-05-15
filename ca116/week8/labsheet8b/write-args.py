#!/usr/bin/env python3

import sys
file = sys.argv[1]
words = sys.argv[2:]

with open(file, "w") as f:
    i = 0
    while i < len(words):
        f.write(words[i] + "\n")
        i += 1
