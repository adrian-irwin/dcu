from multiprocessing import *
import time


def greet(q):
    print(f"(child process) Waiting for name...")
    name = q.get()
    time.sleep(1)
    print(f"(child process) Well, hi {name}")


def sendName():
    q = Queue()

    p1 = Process(target=greet, args=(q,))
    p1.start()

    time.sleep(2)
    print(f"(parent process) Ok, I'll send the name")
    q.put("Jimmy")


sendName()