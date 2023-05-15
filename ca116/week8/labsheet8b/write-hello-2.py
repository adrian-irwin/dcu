#!/usr/bin/env python3

import sys
a = sys.argv[1]

with open(a, "w") as f:
    f.write("Hello world.\n")
