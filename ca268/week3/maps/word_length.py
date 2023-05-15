# Write a function called get_counts_dict() which will takes a list of words as a parameter and returns a map of a count of each word.

def get_counts_dict(lists):
    d = {}
    for word in lists:
        if len(word) not in d:
            d[len(word)] = 1
        else:
            d[len(word)] = int(d[len(word)]) + 1
    return d