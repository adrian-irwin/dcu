#!/usr/bin/env python3

import sys
args = sys.argv[1]

with open(args) as f:
    lines = (f.readlines())

i = 0
while i < len(lines):
    lines[i] = lines[i].strip()
    i += 1

total = 0
k = 0
while k < len(lines):
    numbers = lines[k].split()
    j = 0
    while j < len(numbers):
        total = total + int(numbers[j])
        j += 1
    k += 1

print(total)
