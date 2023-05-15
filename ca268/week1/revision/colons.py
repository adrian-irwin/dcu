# Write a python program which reads all the command line arguments and prints them out separated by colons.

import sys

a = sys.argv[1:]

print(f":{':'.join(a)}:")