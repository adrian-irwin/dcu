#!/usr/bin/env python3

import sys
import string

lines = [line.strip() for line in sys.stdin if len(line) <= 100 if len(line) >= 1]

for line in lines:
    number = 0
    missingLetters = []
    for c in string.ascii_lowercase:
        if c in line.lower():
            number += 1
        else:
            missingLetters.append(c)
    if number >= 26:
        print("pangram")
    else:
        print(f"missing {''.join(missingLetters)}")
