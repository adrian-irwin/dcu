#!/usr/bin/env python3

s = input()
a = []

while s != "end":
    a.append(s)
    s = input()

#   convert list to integers to make things easier
z = 0
while z < len(a):
    a[z] = int(a[z])
    z += 1

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

print(a[(len(a) // 2)])
