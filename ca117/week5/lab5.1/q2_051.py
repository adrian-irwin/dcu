#!/usr/bin/env python3

import sys

words = [line.strip() for line in sys.stdin]
letters = ["e", "v", "i", "l"]
hasEVILonce = []

for word in words:
    letterCount = {"e": 0, "v": 0, "i": 0, "l": 0}
    for letter in word.lower():
        if letter == "e":
            letterCount["e"] += 1
        elif letter == "v":
            letterCount["v"] += 1
        elif letter == "i":
            letterCount["i"] += 1
        elif letter == "l":
            letterCount["l"] += 1
    if letterCount["e"] == 1 and letterCount["v"] == 1 and letterCount["i"] == 1 and letterCount["l"] == 1:
        hasEVILonce.append(word)

for word in hasEVILonce:
    position = {"e": 0, "v": 0, "i": 0, "l": 0}
    for letter in letters:
        position[letter] = word.lower().find(letter)
    if position["e"] < position["v"] and position["v"] < position["i"] and position["i"] < position["l"]:
        print(word)
