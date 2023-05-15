#!/usr/bin/env python3

# fib series : xn+2 = xn+1 + xn
# or xn = xn-2 + xn-1

n = int(input())
first = 0
second = 1

fib = 0

i = 0
while first < n:
    fib = first + second
    print(first)
    first = second
    second = fib
    i = i + 1
