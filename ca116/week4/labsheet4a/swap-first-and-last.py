#!/usr/bin/env python3

s = input()

#hello
#5 - 1

print(s[len(s) - 1] + s[1:4] + s[0])
#   in len(s) -1= last thing
# s[1:len(s) - 1] from the 2nd letter to just before last letter (last letter - 1)
# first letter