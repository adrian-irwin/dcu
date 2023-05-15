#!/usr/bin/env python3

def maximum(l):
    if len(l) == 1:
        return l[0]

    firstNumber = l[0]
    restOfList = maximum(l[1:])
    return firstNumber if firstNumber > restOfList else restOfList
