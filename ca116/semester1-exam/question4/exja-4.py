#!/usr/bin/env python3

s = input()

i = 0
while i < len(s) and s[i] != '"':
    i += 1

j = i + 1
if i < len(s):
    while j < len(s) and s[j] != '"':
        j += 1

    if j < len(s):
        print(s[i + 1:j])
