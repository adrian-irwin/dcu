#!/usr/bin/env python3

import sys


def quadrant(line):
    coords = line.split()
    x, y = int(coords[0]), int(coords[1])
    if x > 0 and y > 0:
        return 1
    elif x > 0 and y < 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x < 0 and y > 0:
        return 4


def main():
    for line in sys.stdin:
        print(quadrant(line))


if __name__ == '__main__':
    main()
