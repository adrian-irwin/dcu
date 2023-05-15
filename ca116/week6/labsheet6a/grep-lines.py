#!/usr/bin/env python3

#input the word searching for
import sys
args = sys.argv[1:]

#turns the search word into string format
search = args[0]

#length of the search word for indexing
k = len(search)

#input the lines to search through
s = input()
a = []
while s != "end":
    a.append(s)
    s = input()

#counter for lines
i = 0
#counter for letters in lines
j = 0

#search for word in lines
while i < len(a):
    #line to search through
    c = a[i]

    #when j is less than the length of the line and when we haven't found the word we add 1 to j
    while j < len(a[i]) and c[j:j + k] != search:
        # print("length of line:", len(a[i]) , ", j :", j, c[j:j + k])
        j += 1

    #if we find the word and j is less than the length of the line we print the line
    if j < len(a[i]):
        # print(c[j:j + k])
        print(a[i])


    #reset j for the next line
    j = 0

    i += 1
