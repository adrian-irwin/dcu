# Write a recursive method called duplicates() which returns true if two consecutive elements of the linked list are equal. Add the method to the LinkedList class from recursiveMax.py

#
#  Just a class to store the item and the next pointer
#
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

# Note, these are methods "A method is a function that is stored as a class attribute"
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        self.head = Node(item, self.head)

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next    # remove the item by moving the head pointer
            return item

    def is_empty(self):
        return self.head == None

    def duplicates(self):
        return self.recursive_duplicates(self.head, self.head.item)

    def recursive_duplicates(self, ptr, dupe):
        if ptr != ptr.next:
            return dupe
        elif ptr.item == dupe:
            dupe = ptr.item
            return self.recursive_duplicates(ptr.next, dupe)
        else:
            return self.recursive_duplicates(ptr.next, dupe)


