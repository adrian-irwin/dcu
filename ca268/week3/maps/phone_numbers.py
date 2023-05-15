# Write a program to manage phone numbers. A user enters commands a line at a time. There are three commands:

# 1. !! (two exclamation marks) exits the program
# 2. name number associates a number to a name. Note that the name cannot have spaces and if a second number is added to a name, it overwrites the first.
# 3. name ? gives the number for that name


print("Enter a name and number, or a name and ? to query (!! to exit)")

unlucky = {}
a = input().split()
while a[0] != "!!":
    if a[1] != "?":
        unlucky[a[0]] = a[1]
    else:
        try:
            print(f"{a[0]} has number {unlucky[a[0]]}")
        except:
            print(f"Sorry, there is no {a[0]}")
    a = input().split()

print("Bye")