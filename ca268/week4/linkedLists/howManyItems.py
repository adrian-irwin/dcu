# Add a count method to the LinkedList class which returns the number of elements in the list. It should leave the list unchanged.


#  Just a class to store the item and the next pointer

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

    def count(self):
        total = 0
        i = self.head
        while i != None:
            total += 1
            i = i.next
        return total
