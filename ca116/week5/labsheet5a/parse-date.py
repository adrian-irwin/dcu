#!/usr/bin/env python3

s = input()

i = 0
while i < len(s) and s[i] != " ":
    i += 1

day = s[0:i]  # day

j = i + 1
while j < len(s) and s[j] != " ":
    j += 1

date = s[i + 1:j]  # day number

k = j + 1
while k < len(s) and s[k] != " ":
    k += 1

month = s[j + 1:k - 1]  # month

l = k + 1
while l < len(s) and s[l] != " ":
    l += 1

year = s[k + 1:l]  # year

print(month + " " + date + ", " + year + " (" + day + ")")
