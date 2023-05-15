#!/usr/bin/env python3

import sys

def readNum(file):
    try:
        for line in file:
            try:
                number = line.strip()
                number = int(number)
                print(f"Thank you for {number}")
                break

            except ValueError:
                print(f"{number} is not a number")

    except FileNotFoundError:
        print(f"The file {filename} cannot be opened.")

readNum(sys.stdin.readlines())
