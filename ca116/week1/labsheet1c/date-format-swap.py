#!/usr/bin/env python3

date = int(input())

a = (date // 1000 % 10) * 100000
b = (date // 100 % 10) * 10000
c = (date // 100000 % 10) * 1000
d = (date // 10000 % 10) * 100
e = (date // 10 % 10) * 10
f = date // 1 % 10


print(a + b + c + d + e + f)
