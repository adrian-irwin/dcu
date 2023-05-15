#!/usr/bin/env python3

s = input()

s = input()

while s != "end":
    i = 0
    while i < len(s) and s[i] != ",":
        i += 1

    if i < len(s):
        t = s[i - 4:i]

        if t == "City":
            print(s[:i])

    s = input()
