#!/usr/bin/env python3

s = input()
a = []

while s != "end":
    a.append(s)
    s = input()

i = 0
while i < len(a):
    c = i
    j = i + 1
    while j < len(a):
        if a[j] < a[c]:
            c = j
        j = j + 1

    tmp = a[c]
    a[c] = a[i]
    a[i] = tmp

    i += 1

k = 0
while k < len(a):
    print(a[k])
    k += 1
