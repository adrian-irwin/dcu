#!/usr/bin/env python3

s = input()
a = []

while s != "end":
    if (int(s) % 2) == 1:
        a.append(s)
    else:
        print(s)
    s = input()

i = 0
while i < len(a):
    print(a[i])
    i += 1
