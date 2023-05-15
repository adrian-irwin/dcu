#!/usr/bin/env python3

import sys

lines = [line.strip() for line in sys.stdin]

tokens = lines[0].split()
numberOfRooms = int(tokens[0])
occupiedRooms = [int(token) for token in tokens[1:]]
allRooms = [i + 1 for i in range(numberOfRooms)]

roomsOccupied = []
for n in allRooms:
    if n not in sorted(occupiedRooms):
        print(n)
        break
    else:
        roomsOccupied.append(n)

if len(roomsOccupied) == len(allRooms):
    print("no room")
