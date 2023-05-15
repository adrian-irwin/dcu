#!/usr/bin/env python3

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip())

numbers = []
for c in lines[0].split():
    numbers.append(int(c))
order = lines[1]
numbers.sort()
output = []
for c in order:
    if c == "A":
        output.append(numbers[0])
    elif c == "B":
        output.append(numbers[1])
    elif c == "C":
        output.append(numbers[2])

print(f"{output[0]} {output[1]} {output[2]}")
