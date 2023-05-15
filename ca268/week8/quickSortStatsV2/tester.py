import sys
from quickSortStatsV2 import qsort

def main():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()

    orig = list(items)

    result = qsort(items)
    if items != sorted(orig):
        print("The list is not sorted.")
        print(f"The list looks like this: {items}")
    else:
        print(result)

if __name__ == "__main__":
    main()
