#!/usr/bin/env python3

import sys
s = sys.argv[1:]

space = " "
i = 0
while i < int(s[0]):
    print((space * i) + ".")
    i += 1
