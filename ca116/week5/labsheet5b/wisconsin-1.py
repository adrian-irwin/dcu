#!/usr/bin/env python3

s = input()

s = input()


while s != "end":
    i = 0
    while i < len(s) and s[i] != ",":
        i += 1

    if i < len(s):
        t = s[i + 1:i + 3]

        if t == "WI":
            print(s[:i])

    s = input()
