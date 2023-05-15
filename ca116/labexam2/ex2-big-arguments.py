#!/usr/bin/env python3

import sys
inputs = sys.argv[1:]

i = 0
while i < len(inputs):
    if int(inputs[i]) > 50:
        print(inputs[i])
    i += 1
