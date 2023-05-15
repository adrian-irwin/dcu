#!/usr/bin/env python3

import sys

lines = [line.strip() for line in sys.stdin]

numberWords = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

bigNumberWords = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}

for line in lines:
    lineToPrint = []
    numbers = line.split()
    for number in numbers:
        if int(number) < 20:
            lineToPrint.append(numberWords[int(number)])
        elif int(number) == 100:
            lineToPrint.append("one hundred")
        else:
            ten, remainder = divmod(int(number), 10)
            if remainder == 0:
                lineToPrint.append(bigNumberWords[ten])
            else:
                lineToPrint.append(f"{bigNumberWords[ten]}-{numberWords[remainder]}")
    print(" ".join(lineToPrint))
