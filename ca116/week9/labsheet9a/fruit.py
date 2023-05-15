#!/usr/bin/env python3

import sys

s = sys.stdin.readlines()

fruit = {
    "apple": True,
    "pear": True,
    "orange": True,
    "banana": True,
    "cherry": True,
}

i = 0
while i < len(s):
    if s[i].strip() in fruit:
        print(s[i].strip())
    i += 1
