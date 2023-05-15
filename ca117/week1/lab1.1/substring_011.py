#!/usr/bin/env python3

import sys

for word in sys.stdin:
    
    word = word.split()
    first = word[0].lower()
    second = word[1].lower()
    start = second.find(first)

    if second[start:start + len(first)] == first:
        print("True")
    else:
        print("False")
