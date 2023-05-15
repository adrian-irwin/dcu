#!/usr/bin/env python3

decimal = input()

binary = 0

i = 0
while i < len(decimal):
    if decimal[len(decimal) - 1 - i] == "1":
        binary = binary + (2 ** i)
    else:
        binary = binary + 0
    i += 1

print(binary)
