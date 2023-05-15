# Write a python program which reads a string on the command line and prints all consecutive pairs of characters of the string.

import sys

arg = sys.argv[1]

for i in range(len(arg) - 1):
    print(arg[i] + arg[i+1])
