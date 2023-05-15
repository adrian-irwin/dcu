# Write a function called set_stuff which takes two sets, a and b as parameters and returns a tuple with the following elements:

# The union of the two sets a and b.
# A boolean value, True or False, depending on whether a is a subset of b.
# A boolean value, True or False, depending on whether a is a superset of b.

def set_stuff(a, b):
    union = a.union(b)
    subset = a.issubset(b)
    superset = a.issuperset(b)
    return union, subset, superset
