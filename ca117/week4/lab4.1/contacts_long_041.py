#!/usr/bin/env python3

import sys

def load_contacts(filename):
    d = {}
    with open(filename, "r") as fin:
        for line in fin:
            name, number, email = line.strip().split()
            d[name] = (number, email)
    return d

d = load_contacts(sys.argv[1])

for line in sys.stdin:
    name = line.strip()
    print(f"Name: {name}")
    if name in d:
        number, email = d[name]
        print(f"Phone: {number}")
        print(f"Email: {email}")
    else:
        print("No such contact")
