#!/usr/bin/env python3

def power(m, n):
    if m == 0 or n == 0:
        return 1
    return m * power(m, n - 1)
