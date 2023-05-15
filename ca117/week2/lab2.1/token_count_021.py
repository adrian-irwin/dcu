#!/usr/bin/env python3

import sys

count = 0
for line in sys.stdin.readlines():
    tokens = line.split()
    for i in tokens:
        count += 1

print(count)
