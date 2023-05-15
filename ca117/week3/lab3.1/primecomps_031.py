#!/usr/bin/env python3

import sys

def prime(n):
    if n <= 1:
        return False
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True

def primeNumbers(i):
    numbers = []
    for j in range(i):
        numbers.append(j + 1)
    primes = [n for n in numbers if prime(n) and n != 4]

    return primes

for line in sys.stdin:
    i = int(line.strip())
    print(f"Primes: {primeNumbers(i)}")
