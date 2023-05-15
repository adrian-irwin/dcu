#!/usr/bin/env python3

def swap_keys_values(d):
    new_dictionary = {}
    for k, v in d.items():
        new_dictionary[v] = k
    return new_dictionary
