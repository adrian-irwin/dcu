#!/usr/bin/env python3

a = []

b = input()
while b != "end":
    a.append(int(b))
    b = input()

n = int(input())

i = 0
while i < len(a):
    a[i] = a[i] + n
    print(a[i])
    i += 1
