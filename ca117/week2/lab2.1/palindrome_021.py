#!/usr/bin/env python3

import sys

for line in sys.stdin.readlines():
    line = line.strip().lower()
    chars = []
    for c in line:
        if c.isalnum():
            chars.append(c)
    print(chars == chars[::-1])
