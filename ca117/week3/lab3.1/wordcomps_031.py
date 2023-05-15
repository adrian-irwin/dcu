#!/usr/bin/env python3

import sys

words = [word.strip() for word in sys.stdin]

seventeen = [n for n in words if len(n) == 17]
eighteen = [n for n in words if len(n) >= 18]
fourAs = [n for n in words if n.lower().count("a") == 4]
twoOrMoreQs = [n for n in words if n.lower().count("q") >= 2]
containsCie = [n for n in words if "cie" in n.lower()]
anagramOfAngle = [n for n in words if sorted(n.lower()) == sorted("angle") if n != "angle"]

print(f"Words containing 17 letters: {seventeen}")
print(f"Words containing 18+ letters: {eighteen}")
print(f"Words with 4 a's: {fourAs}")
print(f"Words with 2+ q's: {twoOrMoreQs}")
print(f"Words containing cie: {containsCie}")
print(f"Anagrams of angle: {anagramOfAngle}")
