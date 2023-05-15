#!/usr/bin/env python3

s = input()
u = ""
i = 0
j = 0
while i < len(s):
    t = ""
    while s[j] != "," and j < len(s):
        t = t + s[j]
        j += 1
    print(t)
    j += 1
    i += 1















    # if j < len(s) :
    #     t = ""
    #     t = s[j]
    #     u = t + s[j]
    #     print(u)