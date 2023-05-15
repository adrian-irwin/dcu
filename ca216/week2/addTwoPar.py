from multiprocessing import *
import time


def addTwoNumbers(a, b ,q):
    time.sleep(1)
    q.put(a+b)


def addTwoPar():
    x = int(input(f"Enter first number: "))
    y = int(input(f"Enter second number: "))

    q = Queue()
    p1 = Process(target=addTwoNumbers, args=(x, y, q))
    p1.start()

    print(q.get())


addTwoPar()
