# Write a function called make_map() which reads data from the input and creates and returns a map.
# The program should read student details from standard input, one line per student.
# Each line contains a student name followed by a mark.

import sys

def make_map():
    # inp = sys.stdin.readlines()
    inp = ["James 90","John 80", "Bobby 40", ""]
    d = {}
    for i in inp:
        if i != "":
            a = i.split()
            # print(a)
            d[a[0]] = a[1]
    return d


student = make_map() # Call the student function
print(type(student)) # check the type ... should be a map (or in python, dict)
names = student.keys()   # get all names
for name in sorted(names): # sort the names
    print(name + " has mark " + student[name]) # print the names and marks
