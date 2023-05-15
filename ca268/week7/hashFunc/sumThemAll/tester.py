import sys
from HashSet import HashSet

def main():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()

    # First number is the capacity
    strset = HashSet(int(items[0]))

    for word in items[1:]:
        strset.add(word)

    # Print the hash table (the layout will vary with the hashing function)
    print(strset)

if __name__ == "__main__":
    main()
