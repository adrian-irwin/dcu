#!/usr/bin/env python3

w = input()
s = ""
i = 0
j = 0
while i < len(w) // 2:
    if w[i] == w[len(w) - 1 - i]:
        j += 1
    i += 1

if j == len(w) // 2:
    print("palindrome")
