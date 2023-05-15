#!/usr/bin/env python3

import sys

a = sys.stdin.readlines()

total = 0
i = 0
while i < len(a):
    b = int(a[i].strip())
    total = total + b
    i += 1

print(total)