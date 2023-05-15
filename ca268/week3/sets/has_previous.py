# Write a program which reads numbers until a -1 is encountered and only print out numbers which have previously occurred in the input.

print("Enter numbers (-1 to end): ", end="")
numbers = []
numsToPrint = []
n = int(input())

while n != -1:
    if n not in numbers:
        numbers.append(n)
    else:
        numsToPrint.append(n)
    n = int(input())

for i in numsToPrint:
    print(str(i) + " ", end="")
print()