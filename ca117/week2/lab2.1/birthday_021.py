#!/usr/bin/env python3

import sys
import calendar

poem = ["Monday's child is fair of face", "Tuesday's child is full of grace", "Wednesday's child is full of woe", "Thursday's child has far to go", "Friday's child is loving and giving", "Saturday's child works hard for a living", "Sunday's child is fair and wise and good in every way"]

for line in sys.stdin.readlines():
    date = line.strip().split()
    day = int(date[0])
    month = int(date[1])
    year = int(date[2])
    weekday = calendar.weekday(year, month, day)
    print(f"You were born on a {calendar.day_name[weekday]} and {poem[weekday]}.")
