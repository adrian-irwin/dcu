#!/usr/bin/env python3

s = input()

i = 0
while i < len(s):
    if s[i] >= "a" and s[i] <= "g":
        print(s[i])
        i = len(s)
    i += 1