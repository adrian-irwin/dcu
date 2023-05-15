#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

n = 20

plot = []

i = 0
while i < n:
    plot.append([" "] * n)
    i += 1

i = 0
while i < len(lines):
    tokens = lines[i].split()
    x = int(tokens[0])
    y = int(tokens[1])
    plot[y][x] = "*"
    i += 1

print(" " + "-" * n)
i = 0
while i < n:
    print("|" + "".join(plot[n - i - 1]) + "|")
    i += 1

print(" " + "-" * n)
