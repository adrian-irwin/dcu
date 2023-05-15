#!/usr/bin/env python3

import sys

for word in sys.stdin:
    word = word.strip()
    if len(word) > 1:
        print(word[:1].capitalize() + word[1:-1] + word[-1:].capitalize())
