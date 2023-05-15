#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip().split(".", 1)
    firstName = line[0].capitalize()
    s = line[1].split("@")
    lastName = s[0].rstrip("0123456789").capitalize()
    print(firstName, lastName)
