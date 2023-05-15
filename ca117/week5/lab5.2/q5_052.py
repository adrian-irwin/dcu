#!/usr/bin/env python3

import sys

def tagger(item):
    return item[1]

lines = [line.strip() for line in sys.stdin]

skipped = []
finalMark = {}
for line in lines:
    total = 0
    name, marks = line.split(":")
    marks = marks.split(",")
    try:
        for i in range(0, len(marks)):
            total += int(marks[i])
        finalMark[name] = total
    except ValueError:
        skipped.append(name)

for k, v in sorted(finalMark.items(), key=tagger, reverse=True):
    print(f"{k} : {v}")

print("Skipped:")
for s in skipped:
    print(s)
