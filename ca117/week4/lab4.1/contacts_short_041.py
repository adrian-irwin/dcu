#!/usr/bin/env python3

import sys

def load_contacts(filename):
    d = {}
    with open(filename, "r") as fin:
        for line in fin:
            name, number = line.strip().split()
            d[name] = number
    return d

d = load_contacts(sys.argv[1])

for line in sys.stdin:
    name = line.strip()
    print(f"Name: {name}")
    if name in d:
        print(f"Phone: {d[name]}")
    else:
        print("No such contact")
