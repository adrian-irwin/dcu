# Write a recursive method which counts the number of even elements in a list. It should leave the list unchanged. Your method should be called count_even and should be added to the end of the LinkedList class.


#  Just a class to store the item and the next pointer
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


#   LinkedList class
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

    def count_even(self):
        return self.recursive_count(self.head)

    def recursive_count(self, ptr):
        if ptr==None:
            return 0
        if ptr.item % 2 == 0:
            x = self.recursive_count(ptr.next)
            return 1 + x
        else:
            return self.recursive_count(ptr.next)
