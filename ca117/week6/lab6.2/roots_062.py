#!/usr/bin/env python3

import sys
import math

def realRoots(a, b, c):
    try:
        root1 = (-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
        root2 = (-b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
        return f"r1 = {root1}, r2 = {root2}"
    except ValueError:
        return None

def main():
    for line in sys.stdin:
        line = line.strip().split()
        a = int(line[0])
        b = int(line[1])
        c = int(line[2])
        print(realRoots(a, b, c))

if __name__ == '__main__':
   main()
