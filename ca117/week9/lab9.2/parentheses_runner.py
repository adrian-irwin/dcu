#!/usr/bin/env python3

from parentheses_092 import matcher
import sys


def main():
    for line in sys.stdin:
        print(matcher(line.strip()))


if __name__ == '__main__':
    main()
