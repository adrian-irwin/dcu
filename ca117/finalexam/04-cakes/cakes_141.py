#!/usr/bin/env python3

import sys


def cakes(line):
    prices = sorted([int(i) for i in line.split()])
    finalPrice = 0
    while len(prices) > 0:
        if len(prices) < 3:
            finalPrice += sum(prices)
            prices = []
        elif len(prices) == 3:
            finalPrice += sum(prices) - min(prices)
            prices = []
        else:
            finalPrice += sum(prices[-3:]) - min(prices[-3:])
            prices = prices[:-3]

    return finalPrice


def main():
    for line in sys.stdin:
        print(cakes(line))


if __name__ == '__main__':
    main()
