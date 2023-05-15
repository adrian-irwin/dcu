# Write a python program which determines if a string has an even or odd number of characters.
# Should the string have an even number of characters, it prints the second half of the string.
# Otherwise it prints only the first and last letters of the string.
# The string will be passed to your program on the command line.

import sys

a = sys.argv[1]

if len(a) % 2:
    print(f"{a[0]}{a[-1]}")
else:
    print(a[(len(a) // 2):])