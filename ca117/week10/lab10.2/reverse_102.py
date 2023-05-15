#!/usr/bin/env python3

def reverse_list(numbers):
    if len(numbers) == 0:
        return []
    return numbers[-1:] + reverse_list(numbers[:-1])
