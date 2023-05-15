#!/usr/bin/env python3

import sys


for line in sys.stdin:
    sum = 0
    numbers = line.strip().split()
    numberToConvert = numbers[0]
    baseOfNumber = numbers[1]

    i = 0
    while i < len(numberToConvert):
        sum = sum + (int(numberToConvert[len(numberToConvert) - i - 1]) * (int(baseOfNumber) ** i))
        i += 1
    print(sum)
