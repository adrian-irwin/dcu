#!/usr/bin/env python3

import sys

lines = [line.strip() for line in sys.stdin]

def upper(letter):
    if letter.isupper():
        return letter
    return "-"

for line in lines:
    onlyUpperCase = "".join([upper(letter) for letter in line]).split("-")
    print(max(onlyUpperCase, key=len))
