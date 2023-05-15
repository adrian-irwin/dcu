#!/usr/bin/env python3

import sys

def tagger(item):
    return item[1]

filename = sys.argv[1]

with open(filename, "r") as f:
    calories = {}
    for line in f:
        splitLine = line.strip().split()
        calories[" ".join(splitLine[:-1])] = splitLine[-1]

nameAndCalories = {}

for line in sys.stdin:
    tokens = line.strip().split(",")
    name = tokens[0]
    items = tokens[1:]
    calorieCount = 0
    for item in items:
        if item in calories:
            calorieCount += int(calories[item])
        else:
            calorieCount += 100
    nameAndCalories[name] = calorieCount

longestKey = len((max(nameAndCalories.keys(), key=len)))
longestValue = len(str(max(nameAndCalories.values())))

for k, v in sorted(nameAndCalories.items(), key=tagger):
    print(f"{k:>{longestKey}} : {v:>{longestValue}}")
