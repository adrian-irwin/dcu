import sys
from quickSortStats import qsort

def main():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()

    orig = list(items)

    result = qsort(items)
    if items != sorted(orig):
        print("The list is not sorted.")
    else:
        print(result)

if __name__ == "__main__":
    main()
