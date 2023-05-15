#!/usr/bin/env python3

import sys

for line in sys.stdin:
    words = line.split()
    finishedLine = ""
    for word in words:
        finishedLine = finishedLine + word[:-1] + word[-1].capitalize() + " "
    print(finishedLine.rstrip())
