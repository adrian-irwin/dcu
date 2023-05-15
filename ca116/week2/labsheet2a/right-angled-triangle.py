#!/usr/bin/env python3

long_side = int(input())
side1 = int(input())
side2 = int(input())

is_right_angle = (side1 ** 2 + side2 ** 2) == long_side ** 2

print(is_right_angle)
