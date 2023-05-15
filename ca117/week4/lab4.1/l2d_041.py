#!/usr/bin/env python3

def l2d(lines):
    d = {}
    allLines = [line.strip().split() for line in lines]
    keys, values = allLines[0], allLines[1]
    i = 0
    while i < len(keys):
        d[keys[i]] = values[i]
        i += 1
    return d
