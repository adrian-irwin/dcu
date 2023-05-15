#!/usr/bin/env python3

s = input()
a = []

while s != "end":
    a.append(s)
    s = input()

b = 0
i = 0
while i < len(a):
    if int(a[i]) < int(a[b]):
        b = i
    i += 1

print(b)
