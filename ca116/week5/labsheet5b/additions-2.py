#!/usr/bin/env python3

i = 0
s = "271+9730+30+813+5"
total = 0

k = 0
j = 0

while i < 5 :

    if j < len(s):
        while s[j] != "+" and j < len(s):
            j += 1

        print(s[k:j])
        total = total + int(s[k:j])
        print(total)

        k = j + 1
        j += 1
    else:
        print(s[len(s)-2:])
        total = total + int(s[len(s)-2:])
        print(total)

    i += 1

print(total)