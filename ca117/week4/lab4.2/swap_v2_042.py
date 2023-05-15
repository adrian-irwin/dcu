#!/usr/bin/env python3

def swap_unique_keys_values(d):
    new_dictionary = {}

    times = {}
    for value in d.values():
        if value not in times:
            times[value] = 1
        elif value in times:
            times[value] += 1

    for k, v in d.items():
        if times[v] == 1:
            new_dictionary[v] = k
    return new_dictionary
