# The list implementation of the queue normally uses a head and a tail to point to the beginning and end of the list. It is possible, at the cost of a little more work, to dispense with the tail variable.

# Write a function which will take the head of the list implementation of a queue and will add an item to the end of the list.

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

def add_to_queue(head, item):
    while head != None:
        if head.next == None:
            head.next = Node(item, None)
            break
        head = head.next
    if head == None:
        head = Node(item, head)