#!/usr/bin/env python3

timetable = []

s = input()
while s != "end":
    timetable.append(s)
    s = input()

i = 0
while i < len(timetable):
    tokens = timetable[i].split()
    c = int(tokens[1]) + (int(tokens[2]) - 1)
    d = str(c)
    tokens[2] = d + ":50"
    e = int(tokens[1])
    f = str(e)
    tokens[1] = f + ":00"
    print(" ".join(tokens))
    i += 1
