#!/usr/bin/env python3

import sys
import math

def main():
    for line in sys.stdin:
        numbers = line.strip().split()
        start_r = float(numbers[0])
        inc_r = float(numbers[1])
        end_r = float(numbers[2])

        h1 = 'Radius (m)'
        h4 = '-' * len(h1)
        h2 = 'Area (m^2)'
        h5 = '-' * len(h2)
        h3 = 'Volume (m^3)'
        h6 = '-' * len(h3)

        print(f'{h1:>s} {h2:>15s} {h3:>15s}')
        print(f'{h4:>s} {h5:>15s} {h6:>15s}')

        iterations = (end_r - start_r) / inc_r

        i = 0
        while i < iterations:
            radius = (start_r + (inc_r * i))
            area = 4 * math.pi * (radius ** 2)
            volume = (4 / 3) * math.pi * (radius ** 3)
            print(f'{radius:>10.1f} {area:>15.2f} {volume:>15.2f}')
            i += 1

        area = 4 * math.pi * (end_r ** 2)
        volume = (4 / 3) * math.pi * (end_r ** 3)
        print(f'{end_r:>10.1f} {area:>15.2f} {volume:>15.2f}')


if __name__ == '__main__':
    main()
