#!/usr/bin/env python3

import sys

def tagger(item):
   return item[1]

lines = [line.strip() for line in sys.stdin]

playerAndShots = {}
disqualified = []
for line in lines:
    try:
        line = line.split()
        playerName = " ".join(line[:-3])
        shotsTaken = line[-3:]
        totalShotsTaken = 0

        if len(shotsTaken) <= 3 and int(shotsTaken[0]) > 0 and int(shotsTaken[1]) > 0 and int(shotsTaken[2]) > 0:
            for n in shotsTaken:
                totalShotsTaken += int(n)
            playerAndShots[playerName] = totalShotsTaken
        else:
            disqualified.append(playerName)
    except ValueError:
        disqualified.append(playerName)

for k, v in sorted(playerAndShots.items(), key=tagger):
    print(f"{k}: {v}")

if len(disqualified) > 0:
    print(f"Disqualified: {', '.join(disqualified)}")
