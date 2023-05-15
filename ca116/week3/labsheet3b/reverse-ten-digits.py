#!/usr/bin/env python3

n = 10
number = 0

i = 0
while i < n:
    a = int(input())
    number = number + (a * (10 ** i))
    i += 1

output = 0
i = 10
n = 0

while i > n:
    output = (number // (10 ** (i - 1))) % 10
    print(output)
    i -= 1
