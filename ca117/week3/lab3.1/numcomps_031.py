#!/usr/bin/env python3

import sys

def proccessNumber(number):
    numbers = []
    for i in range(number):
        numbers.append(i + 1)

    multipleof3 = [n for n in numbers if not n % 3]
    print(f"Multiples of 3: {multipleof3}")

    multipleof3squared = [n ** 2 for n in multipleof3]
    print(f"Multiples of 3 squared: {multipleof3squared}")

    multipleof4doubled = [n * 2 for n in numbers if not n % 4]
    print(f"Multiples of 4 doubled: {multipleof4doubled}")

    multipleof3or4 = [n for n in numbers if not n % 3 or not n % 4]
    print(f"Multiples of 3 or 4: {multipleof3or4}")

    multipleof3and4 = [n for n in numbers if not n % 3 and not n % 4]
    print(f"Multiples of 3 and 4: {multipleof3and4}")

for line in sys.stdin:
    line = int(line.strip())
    proccessNumber(line)
