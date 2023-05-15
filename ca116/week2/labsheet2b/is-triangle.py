#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())

if a + b > c and b + c > a and c + a > b:
    print("yes")
else:
    print("no")
