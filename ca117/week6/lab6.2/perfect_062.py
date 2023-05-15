#!/usr/bin/env python3

import sys
from math import sqrt

numbers = [line for line in sys.stdin]

def sumFac(n):
    factorsOfNumber = []

    if n > 100:
        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                factorsOfNumber.append(i)
                factorsOfNumber.append(n // i)
        sumOfFactors = 0
        for i in factorsOfNumber:
            sumOfFactors += int(i)
        sumOfFactors = sumOfFactors - n
        return sumOfFactors

    else:
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                factorsOfNumber.append(i)
        sumOfFactors = 0
        for i in factorsOfNumber:
            sumOfFactors += int(i)
        return sumOfFactors


def isPerfect(n):
    if n == sumFac(n):
        return True
    else:
        return False

def main():
   for number in numbers:
        print(isPerfect(int(number)))

if __name__ == '__main__':
   main()
