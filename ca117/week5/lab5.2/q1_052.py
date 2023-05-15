#!/usr/bin/env python3

import sys

lines = [line.strip() for line in sys.stdin]

for line in lines:
    s, n = line.split()
    n = int(n)
    for i in range(n):
        s = s[-1] + s[:-1]
    print(s)
