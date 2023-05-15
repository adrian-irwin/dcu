#!/usr/bin/env python3

import sys
args = sys.argv[1:]

i = 0
n = 0
while i < len(args):
    n = n + int(args[i])
    i += 1

print(n)
