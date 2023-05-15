#!/usr/bin/env python3

import string
import sys

lines = [line.strip() for line in sys.stdin]
words = " ".join(lines).lower().split()
words = " ".join([word.strip(string.punctuation) for word in words])
letters = [letter for letter in words]

vowels = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0,
}
for letter in letters:
    if letter == "a":
        vowels["a"] += 1
    elif letter == "e":
        vowels["e"] += 1
    elif letter == "i":
        vowels["i"] += 1
    elif letter == "o":
        vowels["o"] += 1
    elif letter == "u":
        vowels["u"] += 1

longestKey = len((max(vowels.keys(), key=len)))
longestValue = len(str(max(vowels.values())))

def tagger(item):
    return item[1]

for key, value in sorted(vowels.items(), key=tagger, reverse=True):
    print(f"{key:>{longestKey}} : {value:>{longestValue}}")
