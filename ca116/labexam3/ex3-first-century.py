#!/usr/bin/env python3

import sys

numbers = sys.stdin.readlines()

i = 0
while i < len(numbers) and int(numbers[i]) < 100:
    i += 1

if i < len(numbers):
    print(numbers[i].strip())
else:
    print("none")
