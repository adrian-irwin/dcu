#!/usr/bin/env python3

import sys
n = sys.argv[1]

lines = sys.stdin.readlines()

i = 0
while i < len(lines):
    if int(n) < 10:
        h = int(lines[i]) % 10
    elif int(n) > 10:
        h = int(lines[i]) % 100
    if h != int(n):
        print(lines[i].rstrip())
    i += 1
