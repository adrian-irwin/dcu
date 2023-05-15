#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())

is_even = (((c + 1) % 2) * a) + ((c % 2) * b)


print(is_even)
