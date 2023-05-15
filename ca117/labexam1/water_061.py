#!/usr/bin/env python3

import sys

lines = [line.strip() for line in sys.stdin]

if int(lines[0]) >= 0 and int(lines[0]) <= 1000:
    n = int(lines[0])

tokens = lines[1].split()

for i in range(len(tokens)):
    n -= int(tokens[i])
    if n < 0:
        print(i)
        break

if n >= 0:
    print(i + 1)
