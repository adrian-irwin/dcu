#!/usr/bin/env python3

n = int(input())
p = int(input())

pick = (n // (10 ** p)) % 10
print(pick)
