#!/usr/bin/env python3

if __name__ == "__main__":
    a = ["", "", "dog", "", "", "cat", "", "", "", "mouse"]

i = 0
j = 0
while i < len(a):
    if a[i] != "":
        j += 1
    i += 1
print(j)
