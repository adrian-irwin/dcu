#!/usr/bin/env python3

import sys
files = sys.argv[1:]

total = 0
i = 0
while i < len(files):
    with open(files[i]) as f:
        lines = f.readlines()
        j = 0
        while j < len(lines):
            a = int(lines[j].strip())
            total = total + a
            j += 1
    i += 1

print(total)
