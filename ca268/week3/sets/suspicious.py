# A headmaster of a school is contacted by the police and provided with a file of names of juvenile delinquents.
# He has another file containing the name of his students and wants a program to check if any of the names are the same.
# Each line of each file contains one name only.
# Write a program to detect if any name appears on both files.
import sys

args = sys.argv[1:]

with open(args[0]) as file1:
    file1Lines = [s.strip() for s in file1.readlines()]
with open(args[1]) as file2:
    file2Lines = [s.strip() for s in file2.readlines()]

same = []
for s in file1Lines:
    for t in file2Lines:
        if s == t and t not in same:
            same.append(t)

same = sorted(same)
for i in range(len(same)):
    print(f"{i + 1}. {same[i]}")