#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
longest = lines[0]

i = 0
while i < len(lines):
    if len(lines[i]) > len(longest):
        longest = lines[i]
    i += 1

for line in lines:
    line = line.strip()
    print(f'{line:^{len(longest) - 1}}')
