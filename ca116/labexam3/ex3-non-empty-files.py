#!/usr/bin/env python3

import sys
files = sys.argv[1:]

i = 0
while i < len(files):
    with open(files[i]) as f:
        lines = f.readlines()
    if lines != []:
        print(files[i])
    i += 1
