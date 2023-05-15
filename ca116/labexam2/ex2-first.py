#!/usr/bin/env python3

a = input()

i = 0
while i < len(a) and (a[i] < "0" or a[i] > "9"):
    i += 1

if i < len(a):
    print(a[i])
