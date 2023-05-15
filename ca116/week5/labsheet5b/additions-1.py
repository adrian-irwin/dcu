#!/usr/bin/env python3

i = 0
while i < 10:
    s = input()
    j = 0
    while s[j] != "+":
        j += 1

    a = int(s[0:j])
    b = int(s[j + 1:])

    print(a + b)
    i += 1
