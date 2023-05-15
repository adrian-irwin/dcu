# Write a function called get_sliced_lists which will take a list parameter and return the following lists which should be created using slices:
# A list including all but the last element
# A list including all but the first and last elements
# A reversed list (created using slicing)

# Your function should put the three lists into their own list and return that.

def get_sliced_lists(baselist):
    last = baselist[:-1]
    firstlast = baselist[1:-1]
    reverse = baselist[::-1]
    return last, firstlast, reverse
