# If the end of the list pointed to the head of the list, then you would have a bit of a problem. Printing this list would take forever and wear out a poor computer.

# Write a function called detect_loop() which has a LinkedList parameter and which returns True or False depending on whether any of the next pointers point to the head. Your function should be placed in a file called evil_loop_lists.py.

def detect_loop(self):
    first = self.head
    keep = self.head
    while keep != None:
        if keep.next == first:
            return True
        keep = keep.next
    return False
