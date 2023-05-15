#!/usr/bin/env python3

s = input()
star = "*"

n = len(s)
i = 0
while i < n:
    print(int(s[i]) * star)
    i += 1
