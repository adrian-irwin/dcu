#!/usr/bin/env python3

j = int(input())
positivetotal = 0
negativetotal = 0

while j != 0:
    if j > 0:
        positivetotal = positivetotal + j
    else:
        negativetotal = negativetotal + j
    j = int(input())

print(negativetotal, positivetotal)
