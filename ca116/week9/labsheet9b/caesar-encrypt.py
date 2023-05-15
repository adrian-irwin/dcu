#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

caeser = {}

n = 13
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

src = lower + upper
dst = lower[n:] + lower[:n] + upper[n:] + upper[:n]

i = 0
while i < len(src):
    caeser[src[i]] = dst[i]
    i += 1

j = 0
while j < len(lines):
    s = lines[j].rstrip()
    o = ""
    i = 0
    while i < len(s):
        if ("a" <= s[i] and s[i] <= "z") or ("A" <= s[i] and s[i] <= "Z"):
            o = o + caeser[s[i]]
        else:
            o = o + s[i]
        i += 1
    print(o)
    j += 1
