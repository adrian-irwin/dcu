# Write a python program which reads all the command line arguments and prints them out.

import sys

a = sys.argv[1:]

for i in a:
    print(i)