#!/usr/bin/env python3

n = int(input())
if n != 0:
    o = int(input())

    while o != 0:
        if o < n:
            print("lower")
        elif o > n:
            print("higher")
        else:
            print("equal")
        n = o
        o = int(input())
