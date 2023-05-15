#!/usr/bin/env python3

import sys

lines = [line.strip() for line in sys.stdin]

def seconds(time):
    mins, secs = time.split(":")
    totalSeconds = int(mins) * 60 + int(secs)
    return totalSeconds

def sort(t):
    return seconds(t[-1])

bestTimes = {}

for line in lines:
    try:
        name, times = line.split()[0], line.split()[1:]
        bestTimes[name] = min(times, key=seconds)
    except ValueError:
        pass

bestName, bestTime = min(bestTimes.items(), key=sort)

print(f"{bestName} : {bestTime}")
