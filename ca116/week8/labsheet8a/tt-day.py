#!/usr/bin/env python3

timetable = []

s = input()
while s != "end":
    timetable.append(s)
    s = input()

day = int(input())

i = 0
while i < len(timetable):
    tokens = timetable[i].split()
    if int(tokens[0]) == day:
        print(timetable[i])
    i += 1
