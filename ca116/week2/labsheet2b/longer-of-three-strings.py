#!/usr/bin/env python3

line1 = input()
line2 = input()
line3 = input()

len1 = len(line1)
len2 = len(line2)
len3 = len(line3)

if len1 > len2 and len1 > len3:
    print(line1)
elif len2 > len1 and len2 > len3:
    print(line2)
else:
    print(line3)
