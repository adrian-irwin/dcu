#!/usr/bin/env python3

n = int(input())

m = 5
i = 0
while i < m:
    o = int(input())
    if o < n:
        print("lower")
    elif o > n:
        print("higher")
    else:
        print("equal")
    n = o
    i += 1
