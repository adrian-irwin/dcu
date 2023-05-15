import sys
from AVLTree import AVLTree
from upThePath import add

def main():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()
    nums = [int(item) for item in items]

    tree = AVLTree()
    for num in nums[:-1]:
        tree.add(num)

    # Call the students function to determine which element would be modified
    item = add(tree, nums[-1])
    print(item)

if __name__ == "__main__":
    main()