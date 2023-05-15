# Add a rotate() method to the LinkedList class which rotates the list so that the first element of the list becomes the last and all the other elements move one place up.

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

    def __str__(self):
        tmp_str = ""
        ptr = self.head
        while ptr != None:
            tmp_str += " " + ptr.item
            ptr = ptr.next

        return tmp_str

    def rotate(self):
        first2last = self.remove()
        i = self.head
        while i != None:
            if i.next == None:
                i.next = Node(first2last, None)
                break
            i = i.next
        if i == None:
            self.head = Node(first2last, self.head)