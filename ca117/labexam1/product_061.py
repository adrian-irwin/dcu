#!/usr/bin/env python3

import sys
import math

number = [line.strip() for line in sys.stdin][0]

if int(number) <= 10000 and int(number) >= 1:
    tokens = [int(c) for c in number if c != "0"]
    product = math.prod(tokens)

    while len(str(product)) != 1:
        if product > 9 or product < 1:
            product = str(product)
            tokens = [int(c) for c in product if c != "0"]
            product = math.prod(tokens)

    print(product)
