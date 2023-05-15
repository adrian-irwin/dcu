#!/usr/bin/env python3

n = 10
smallest_positive = int(input())

i = 0
while i < n - 1:
    v = int(input())
    if v >= 1:
        if smallest_positive > v:
            smallest_positive = v
    i = i + 1

print(smallest_positive)
