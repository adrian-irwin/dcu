#!/usr/bin/env python3

import sys

words = [word.strip() for word in sys.stdin]
vowels = "aeiou"

def containsVowels(word):
    for c in vowels:
        if c in word:
            word = word.replace(c, "", 1)
        else:
            return False
    return True
shortestWordWithVowels = sorted([word for word in words if containsVowels(word)], key=len)[0]

iaryEnding = len([word for word in words if word.lower().endswith("iary")])

countOfEs = []
for word in words:
    if word.lower().find("e") >= 0:
        countOfEs.append(word.lower().count("e"))
countOfEs = sorted(countOfEs, reverse=True)
wordsWithMostEs = [word for word in words if word.lower().count("e") == countOfEs[0]]

print(f"Shortest word containing all vowels: {shortestWordWithVowels}")
print(f"Words ending in iary: {iaryEnding}")
print(f"Words with most e's: {wordsWithMostEs}")
