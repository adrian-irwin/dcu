import sys
from selectionSortStats import selection_sort

def main():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()

    orig = list(items)

    result = selection_sort(items)
    if items != sorted(orig):
        print("The list is not sorted.")
    else:
        print(result)

if __name__ == "__main__":
    main()
