#!/usr/bin/env python3

import sys

lines = [line.strip() for line in sys.stdin]

for line in lines:
    groupsOfTwo = [line[i:i + 2] for i in range(0, len(line), 2)]
    wordToPrint = []
    for group in groupsOfTwo:
        wordToPrint.append(group[::-1])
    print("".join(wordToPrint))
