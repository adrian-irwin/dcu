#!/usr/bin/env python3

a = []

b = input()
while b != "end":
    a.append(b)
    b = input()

i = 0
while i < len(a):
    print(i, len(a), a[i])
    i += 1
