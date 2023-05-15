#!/usr/bin/env python3

import sys

s = sys.stdin.readlines()

numbers = {
    "one": "eins",
    "two": "zwei",
    "three": "drei",
    "four": "vier",
    "five": "funf",
    "six": "sechs",
    "seven": "sieben",
    "eight": "acht",
    "nine": "neun",
    "ten": "zehn"
}

i = 0
while i < len(s):
    a = s[i].strip()
    if a in numbers:
        print(numbers[a])
    i += 1
