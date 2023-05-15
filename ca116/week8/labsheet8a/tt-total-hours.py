#!/usr/bin/env python3

timetable = []

s = input()
while s != "end":
    timetable.append(s)
    s = input()

total = 0

i = 0
while i < len(timetable):
    tokens = timetable[i].split()
    total = total + int(tokens[2])
    i += 1

print(total)
