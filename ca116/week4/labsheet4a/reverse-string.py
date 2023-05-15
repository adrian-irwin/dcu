#!/usr/bin/env python3

s = input()

i = 0
n = len(s)
t = ""
while i < n:
    t = t + s[len(s) - i - 1]
    i += 1

print(t)
