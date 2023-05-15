#!/usr/bin/env python3

s = input()

i = 0
while i < len(s) and (s[i] < "A" or s[i] > "Z"):
    i += 1

if i < len(s):
    print(s[i], i)
