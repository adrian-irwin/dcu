# Write a function called get_counts which will take as a parameter a list of words and return a list of integers which will be a count of the lengths of those words. No word will have more than 9 letters.
# The counts list will be [0, 0, 0, 5, 0, 0, 0, 2, 0, 0].

def get_counts(words):
    count = [0,0,0,0,0,0,0,0,0,0]
    for i in words:
        if len(i) == 0:
            count[0] += 1
        elif len(i) == 1:
            count[1] += 1
        elif len(i) == 2:
            count[2] += 1
        elif len(i) == 3:
            count[3] += 1
        elif len(i) == 4:
            count[4] += 1
        elif len(i) == 5:
            count[5] += 1
        elif len(i) == 6:
            count[6] += 1
        elif len(i) == 7:
            count[7] += 1
        elif len(i) == 8:
            count[8] += 1
        elif len(i) == 9:
            count[9] += 1
    return count
