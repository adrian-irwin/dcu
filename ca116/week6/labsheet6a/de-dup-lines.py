#!/usr/bin/env python3

#not finished, idk man im bad at this.

s = input()
a = []
a.append(s)
print(len(a))

while s != "end":
    i = 0
    while i < len(a):
        #if s is not the same as a[i] add it to a. WRONG
        if s != a[i]:
            a.append(s)
        print(len(a))
        print(a)
        i += 1
    s = input()

print(a)