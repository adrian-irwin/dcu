#!/usr/bin/env python3

import sys
import string

unique = []
for line in sys.stdin.readlines():
    line = line.strip().split()
    for word in line:
        word = word.strip(string.punctuation).lower()
        if word not in unique:
            unique.append(word)

count = 0
for i in unique:
    if i != "":
        count += 1

print(count)
