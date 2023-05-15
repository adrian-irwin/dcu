#
#  Create a queue relying on a Stack. Actually Two Stacks.
#
#  The Stack ADT has three methods:
#     isempty(), push() and pop()
#
from Stack import Stack

class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def isempty(self):
        return self.stack1.isempty() and self.stack2.isempty()

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        if self.stack1.isempty() == False and self.stack2.isempty() == True:
            while self.stack1.isempty() == False:
                self.stack2.push(self.stack1.pop())
            return self.stack2.pop()
        else:
            return self.stack2.pop()