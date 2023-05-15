# given stack class

class Node:
    def __init__(self):
        self.item = None
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top == None

    def push(self, item):
        oldtop = self.top
        self.top = Node()
        self.top.item = item
        self.top.next = oldtop

    def pop(self):
        item = self.top.item
        self.top = self.top.next
        return item
