import sys
from insertionSortStats import insertion_sort

def main():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()

    orig = list(items)

    result = insertion_sort(items)
    if items != sorted(orig):
        print("The list is not sorted.")
    else:
        print(result)

if __name__ == "__main__":
    main()
