#!/usr/bin/env python3

def build_dictionary(stream):
    dictionary = {}
    for line in stream:
        animal, number = line.strip().split()
        dictionary[animal] = number
    return dictionary

def extract_range(d, low, high):
    itemsWithinRange = {}
    for item in d.items():
        if int(item[-1]) <= high and int(item[-1]) >= low:
            itemsWithinRange[item[0]] = item[-1]
    return itemsWithinRange
