#!/usr/bin/env python3

f = input()

i = 0
while i < len(f) and f[i] != ".":
    i += 1

j = i + 1
while j < len(f):
    j += 1

print(f[0:i])
print(f[i + 1:])
