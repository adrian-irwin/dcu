#!/usr/bin/env python3

import sys

#read input
input = sys.stdin.readlines()

#banned words taken from text file and put into 'banned' list
with open("banned.txt") as f:
    banned = f.readlines()

#remove new line characters from banned
j = 0
while j < len(banned):
    banned[j] = banned[j].strip()
    j += 1

#
i = 0
while i < len(input):
    tokens = input[i].split()
    k = 0
    while k < len(tokens):
        l = 0
        while l < len(banned):
            if tokens[k] == banned[l]:
                tokens[k] = "*" * len(banned[l])
            l += 1
        k += 1
    print(" ".join(tokens))
    i += 1
