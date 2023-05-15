#!/usr/bin/env python3

import sys

line = sys.stdin.readline()

# word A = horizontal
wordA = line.split()[0]
# word B = vertical
wordB = line.split()[1]

# both words cross at one shared letter (must be first letter in both A and B)
for c in range(len(wordA)):
    if wordA[c] in wordB:
        wordAindex = c
        wordBindex = wordB.find(wordA[c])
        break

# make a grid of full stops and word A is horizontal and word B is vertical and they cross at the first letter they have in common
# all letters of word B will be in the same index
# all together len(lineB) lines with a length of len(wordA)

linesToPrint = []
for i in range(len(wordB)):
    line = []

    if i == wordBindex:
        line = wordA.split()
    else:
        for j in range(len(wordA)):
            if j != wordAindex:
                line.append(".")
            else:
                line.append(wordB[i])

    linesToPrint.append("".join(line))
    print(linesToPrint)

print("\n".join(linesToPrint))
