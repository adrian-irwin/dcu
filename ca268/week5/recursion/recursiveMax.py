# Write a recursive method which finds the largest integer in a list. The method should be called largest().

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

    def largest(self):
        return self.recursive_largest(self.head, self.head.item)

    def recursive_largest(self, ptr, max):
        if not ptr:
            return max
        elif ptr.item > max:
            max = ptr.item
            return self.recursive_largest(ptr.next, max)
        else:
            return self.recursive_largest(ptr.next, max)