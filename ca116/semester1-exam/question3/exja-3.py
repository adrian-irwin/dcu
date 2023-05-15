#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

words = []
i = 0
while i < len(lines):
    words.append(lines[i].split())
    i += 1

i = 0
while i < len(words):
    p = i
    j = i + 1
    while j < len(words):
        if words[j][1] < words[p][1]:
            p = j
        j += 1

    tmp = words[p]
    words[p] = words[i]
    words[i] = tmp

    i += 1

i = 0
while i < len(words):
    p = i
    j = i + 1
    while j < len(words):
        if words[j][0] < words[p][0] and words[j][1] == words[p][1]:
            p = j
        j += 1

    tmp = words[p]
    words[p] = words[i]
    words[i] = tmp

    i += 1

i = 0
while i < len(words):
    print(" ".join(words[i]))
    i += 1
