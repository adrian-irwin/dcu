#!/usr/bin/env python3

s = input()

sum = 0
i = 0
n = len(s)
while i < n:
    sum = sum + int(s[i])
    i += 1

print(sum)
