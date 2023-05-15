#!/usr/bin/env python3

import sys
files = sys.argv[1:]

total = 0
i = 0
while i < len(files):
    with open(files[i]) as f:
        lines = f.readlines()

    j = 0
    while j < len(lines):
        lines[j] = lines[j].strip()
        j += 1

    k = 0
    while k < len(lines):
        numbers = lines[k].split()
        h = 0
        while h < len(numbers):
            total = total + int(numbers[h])
            h += 1
        k += 1
    i += 1

print(total)
