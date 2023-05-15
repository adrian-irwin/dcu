#!/usr/bin/env python3

n = 5
j = 0
positivetotal = 0
negativetotal = 0

i = 0
while i < n:
    j = int(input())
    if j > 0:
        positivetotal = positivetotal + j
    else:
        negativetotal = negativetotal + j
    i += 1

print(negativetotal, positivetotal)
