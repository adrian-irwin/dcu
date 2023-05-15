#!/usr/bin/env python3

s = input()


i = 0
n = len(s)
t = ""
while i < n:
    if s[i] != " ":
        t = t + s[i]
    i += 1

print(t)
