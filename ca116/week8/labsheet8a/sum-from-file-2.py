#!/usr/bin/env python3

import sys
args = sys.argv[1]

with open(args) as f:
    lines = f.readlines()

total = 0
i = 0
while i < len(lines):
    lines[i] = lines[i].rstrip()
    total = total + int(lines[i])
    i += 1

print(total)
