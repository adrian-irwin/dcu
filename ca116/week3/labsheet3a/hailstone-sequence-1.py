#!/usr/bin/env python3

#   hailstone ting says that
#
#   if m is even divide by 2
#
#   if odd multiply by 3 and add 1

n = int(input())
m = int(input())

print(m)
i = 0
while (i + 1) < n:
    if m % 2 == 0:
        m = m // 2
        print(m)
    else:
        m = (3 * m) + 1
        print(m)
    i = i + 1
