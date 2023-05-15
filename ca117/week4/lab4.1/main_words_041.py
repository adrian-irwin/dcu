#!/usr/bin/env python3

import sys
import string

lines = [line.strip() for line in sys.stdin]
words = " ".join(lines).lower().split()
words = [word.strip(string.punctuation) for word in words if len(word) > 3]

d = {}
for word in words:
    if word not in d:
        d[word] = 1
    elif word in d:
        d[word] += 1

finalDict = {}
for key in sorted(d):
    if d[key] >= 3:
        finalDict[key] = d[key]

longestKey = len((max(finalDict.keys(), key=len)))
longestValue = len(str(max(finalDict.values())))

for key in sorted(finalDict):
    print(f"{key:>{longestKey}} : {d[key]:>{longestValue}}")
