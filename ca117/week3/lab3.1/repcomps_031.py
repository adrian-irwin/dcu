#!/usr/bin/env python3

import sys

def replaceNumber(i):
    numbers = []
    for j in range(i):
        numbers.append(j + 1)
    multipleof3 = ["X" if not n % 3 else n for n in numbers]
    print(f"Multiples of 3 replaced: {multipleof3}")

for line in sys.stdin:
    i = int(line.strip())
    replaceNumber(i)
