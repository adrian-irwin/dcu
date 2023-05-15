import sys
from HashSet import HashSet

def main():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()
    nums = [int(item) for item in items]

    # First number is the capacity
    numset = HashSet(nums[0])

    for x in nums[1:]:
        print(str(numset.add(x)) + " ", end="")

    print()

if __name__ == "__main__":
    main()
