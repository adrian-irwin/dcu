#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

count = 0
i = 0
while i < len(lines):
    a = lines[i]
    j = 0
    while j < len(a):
        if "A" <= a[j] and a[j] <= "Z":
            count += 1
        j += 1
    i += 1

print(count)
