# Write a recursive function called rprint to print a range of integers from a to b.

def rprint(a, b):
    if a < b:
        print(a)
        rprint(a + 1, b)