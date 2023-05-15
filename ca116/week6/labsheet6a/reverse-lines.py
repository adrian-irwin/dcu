#!/usr/bin/env python3

s = input()
a = []

while s != "end":
    a.append(s)
    s = input()

i = 0
while i < len(a) / 2:
    b = a[i]
    a[i] = a[len(a) - i - 1]
    a[len(a) - i - 1] = b
    i += 1

j = 0
while j < len(a):
    print(a[j])
    j += 1
