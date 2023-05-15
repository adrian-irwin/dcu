import sys
from quickSortRecursiveDepth import qsort

def main():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()

    orig = list(items)

    recursive_depth = qsort(items)
    if items != sorted(orig):
        print("The list is not sorted.")
    else:
        print(recursive_depth)

if __name__ == "__main__":
    main()
