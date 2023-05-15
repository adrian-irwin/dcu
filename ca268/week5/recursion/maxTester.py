import sys
from recursiveMax import LinkedList

def main():
    # Create a list for the tests
    tests = []

    # Read each set
    line = sys.stdin.readline()
    items = line.strip().split()
    nums = [int(item) for item in items] # Create an array of nums from the strings

    ll = LinkedList()

    # Add each number to the list
    for num in nums:
        ll.add(num)

    # call the students function
    tests.append(ll.largest() == max(nums)) # First test ... compare students function to max

    # Keep reducing the list, comparing the largest of the reduced list to the remiaining numbers.
    count = 1
    while count == len(nums):
        ll.remove() # Remove one element from the list
        # Compare the largest of this list with the remaining numbers
        tests.append(ll.largest() == max(nums[count:]))
        count += 1

    if all(tests):
        print("All tests passed!")
    else:
        for i in range(len(tests)):
            if not tests[i]:
                print("test " + str(i) + " failed.")

if __name__ == "__main__":
    main()