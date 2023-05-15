# Define a function called calc_average() in a python program.
# The function should have one parameter which is a list of integers and should return a single value which is the average of the integers in the list.


def calc_average(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum // len(numbers)
