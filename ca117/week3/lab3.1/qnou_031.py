#!/usr/bin/env python3

import sys

words = [word.strip() for word in sys.stdin]

def qWithoutU(s):
    s = s.replace("qu", "__")
    return "q" in s

wordsWithoutQU = [word for word in words if qWithoutU(word.lower())]

print(f"Words with q but no u: {wordsWithoutQU}")
