#!/usr/bin/env python3

n = int(input())
m = 0

i = 0
while i < n:
    a = input()
    if a == "one":
        m = m + 1
    elif a == "two":
        m = m + 2
    elif a == "three":
        m = m + 3
    elif a == "four":
        m = m + 4
    elif a == "five":
        m = m + 5
    else:
        print("error")
    i += 1

print(m)
