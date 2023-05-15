#!/usr/bin/env python3

i = 0
c = 0

while c != 1000:
    s = input()
    j = 0
    while s[j] != "+":
        j += 1

    a = int(s[0:j])
    b = int(s[j + 1:])
    c = a + b
    print(a + b)
    i += 1
