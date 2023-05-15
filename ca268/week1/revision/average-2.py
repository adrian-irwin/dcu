# Define a function called above_average().
# The function should have one parameter which is a list of integers and should return a new list which is all the elements of the original list which are larger than the average.


def above_average(numbers):
    sum = 0
    for i in numbers:
        sum += i

    avg = sum // len(numbers)

    newlist = [n for n in numbers if n > avg]
    return newlist