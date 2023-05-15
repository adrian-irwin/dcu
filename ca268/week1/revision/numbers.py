# Write a python function which takes two parameters, a list of integers and a number, k, and which prints every pair of numbers in the list which add up to k.

def sum_to_k(numbers, outcome):
    for i in numbers:
        for j in numbers:
            if j <=outcome // 2:
                l = i + j
                if l == outcome:
                    print(f"{i} {j}")