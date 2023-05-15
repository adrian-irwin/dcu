#!/usr/bin/env python3

# if word ends in ch,sh,x,s,z add es to end
# if word ends in o add es
# if word ends in consonant + y, remove y and add ies
# if word ends in f or fe, remove f or fe and add ves
# else add s

import sys

for noun in sys.stdin:
    noun = noun.strip()
    if noun.endswith(("ch", "sh", "x", "s", "z", "o")):
        print(noun + "es")
    elif noun.endswith("y") and (noun[-2] != "a" and noun[-2] != "e" and noun[-2] != "i" and noun[-2] != "o" and noun[-2] != "u"):
        print(noun[:-1] + "ies")
    elif noun.endswith("f"):
        print(noun[:-1] + "ves")
    elif noun.endswith("fe"):
        print(noun[:-2] + "ves")
    else:
        print(noun + "s")
