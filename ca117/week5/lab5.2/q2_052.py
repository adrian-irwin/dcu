#!/usr/bin/env python3

import sys

lines = [line.strip() for line in sys.stdin]

numbers = sorted(lines[0].split(), key=int, reverse=True)
order = lines[1]
finalOrder = []

for c in order:
    if c == "A":
        finalOrder.append(numbers[0])
    elif c == "B":
        finalOrder.append(numbers[1])
    elif c == "C":
        finalOrder.append(numbers[2])
    elif c == "D":
        finalOrder.append(numbers[3])

print(" ".join(finalOrder))
