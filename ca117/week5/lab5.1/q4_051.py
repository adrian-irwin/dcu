#!/usr/bin/env python3

import sys

numbers = sorted([int(line.strip()) for line in sys.stdin])

mean = sum(numbers) / len(numbers)

if len(numbers) % 2 == 1:
    median = numbers[len(numbers) // 2]
else:
    median = (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2

print(f"Mean: {mean:.1f}")
print(f"Median: {median:.1f}")
