#!/usr/bin/env python3

import sys
inputTextFile = sys.argv[1]

lines = [line.strip() for line in sys.stdin]

with open(inputTextFile) as f:
    words = f.readlines()
censorWords = [line.strip() for line in words]

i = 0
while i < len(lines):
    for word in censorWords:
        if word in lines[i].lower():
            lines[i] = lines[i].replace(word, "@" * len(word))
    i += 1

print("\n".join(lines))
