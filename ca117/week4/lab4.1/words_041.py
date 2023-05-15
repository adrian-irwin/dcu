#!/usr/bin/env python3

import sys
import string

lines = [line.strip() for line in sys.stdin]
joined = " ".join(lines)
words = joined.lower().split()
words = [word.strip(string.punctuation) for word in words]

d = {}
for word in words:
    if word not in d:
        d[word] = 1
    elif word in d:
        d[word] += 1

for key in sorted(d):
    print(f"{key} : {d[key]}")
