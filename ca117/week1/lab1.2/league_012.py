#!/usr/bin/env python3

import sys

position = []
club = []
played = []
wins = []
draws = []
losses = []
gf = []
ga = []
gd = []
points = []

for line in sys.stdin:

    line = line.split()

    position.append(line[0])
    club.append(" ".join(line[1:-8]))
    played.append(line[-8])
    wins.append(line[-7])
    draws.append(line[-6])
    losses.append(line[-5])
    gf.append(line[-4])
    ga.append(line[-3])
    gd.append(line[-2])
    points.append(line[-1])

longest = club[0]
i = 0
while i < len(club):
    if len(club[i]) > len(longest):
        longest = club[i]
    i += 1

n = len(longest)
h1 = "POS"
h2 = "CLUB"
h3 = "P"
h4 = "W"
h5 = "D"
h6 = "L"
h7 = "GF"
h8 = "GA"
h9 = "GD"
h10 = "PTS"
print(f"{h1:>3} {h2:<{n}} {h3:>2} {h4:>3} {h5:>3} {h6:>3} {h7:>3} {h8:>3} {h9:>3} {h10:>3}")

i = 0
while i < len(position):
    print(f"{position[i]:>3} {club[i]:<{n}} {played[i]:>2} {wins[i]:>3} {draws[i]:>3} {losses[i]:>3} {gf[i]:>3} {ga[i]:>3} {gd[i]:>3} {points[i]:>3}")
    i += 1
