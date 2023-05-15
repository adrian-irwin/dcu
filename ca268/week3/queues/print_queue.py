# Write a function which will take some queue parameters and return a list of the elements of the queue.
# Your function will be called print_queue and will be in a file called print_queue.py.
# It will take three parameters, a list representing the circular buffer and two integers, representing the front and back of the queue.


from Queue import Queue

def print_queue(data, front, back):
    i = front
    while i != back:
        print(data[i])
        i = (i + 1) % len(data)