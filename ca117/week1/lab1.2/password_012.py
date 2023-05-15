#!/usr/bin/env python3

import sys

for word in sys.stdin:
    word = word.strip()
    security = [0, 0, 0, 0]
    for c in word:
        if c.islower():
            security[0] = 1
        elif c.isupper():
            security[1] = 1
        elif c.isdigit():
            security[2] = 1
        else:
            security[3] = 1

    print(sum(security))
