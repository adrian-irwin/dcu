# Write a function called set_intersection which takes two sets as parameters and returns the intersection of the two sets.

def set_intersection(set1, set2):
    intersection = []
    for i in set1:
        if i in set2:
            intersection.append(i)
    return intersection
