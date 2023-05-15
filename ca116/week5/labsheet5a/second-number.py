#!/usr/bin/env python3

s = input()

i = 0
while i < len(s) and (s[i] < "0" or s[i] > "9"):
    i += 1

j = i
while j < len(s) and (s[j] >= "0" and s[j] <= "9"):
    j += 1

k = j
while k < len(s) and (s[k] < "0" or s[k] > "9"):
    k += 1

l = k
while l < len(s) and (s[l] >= "0" and s[l] <= "9"):
    l += 1

if k < len(s):
    print(s[k:l], k)
