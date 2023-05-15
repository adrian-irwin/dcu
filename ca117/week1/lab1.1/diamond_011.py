#!/usr/bin/env python3

import sys

for number in sys.stdin:
    number = int(number)
    j = 1
    for i in range((number * 2) - 1):
        if i < (number - 1):
            beforeMiddle = (" " * (number - i - 1) + "* " * (i + 1)).rstrip()
            print(beforeMiddle)

        elif i == (number - 1):
            middle = ("* " * number).rstrip()
            print(middle)

        else:
            afterMiddle = (" " * (i - number + 1) + "* " * (i - j)).rstrip()
            print(afterMiddle)
            j += 2
