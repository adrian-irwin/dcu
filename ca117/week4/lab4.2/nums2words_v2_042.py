#!/usr/bin/env python3

import sys

lines = [line.strip() for line in sys.stdin]

numberWords = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten"
}

for line in lines:
    lineToPrint = []
    numbers = line.split()
    for number in numbers:
        if number in numberWords:
            lineToPrint.append(numberWords[number])
        else:
            lineToPrint.append("unknown")
    print(" ".join(lineToPrint))
