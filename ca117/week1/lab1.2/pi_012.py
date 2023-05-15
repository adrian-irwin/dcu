#!/usr/bin/env python3

import sys
import math

pi = math.pi

for n in sys.stdin:
    n = int(n)
    print(f'{pi:.{n}f}')
