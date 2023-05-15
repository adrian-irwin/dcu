#!/usr/bin/env python3

s = input()
a = []

while s != "end":
    a.append(s)
    s = input()

i = int(input())
b = a[i:]

c = 0
j = 0
while j < len(b):
    if int(b[j]) < int(b[c]):
        c = j
    j += 1

print(c + i)
