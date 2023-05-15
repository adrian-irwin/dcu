# You might have noticed that the LinkedList behaves in a similar way to a Stack. Create a Stack class using a LinkedList.
# You need to fill out the three methods, push(), pop() and is_empty()

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

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

class LinkedStack:
    def __init__(self):
        self.ll = LinkedList()

    def push(self, item):
        self.ll.add(item)
    def pop(self):
        return self.ll.remove()
    def is_empty(self):
        return self.ll.is_empty()
