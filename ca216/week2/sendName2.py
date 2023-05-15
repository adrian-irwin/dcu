from multiprocessing import *
import time


def greet2(q):
    for i in range(5):
        print(f"(child process) Waiting for name...")
        name = q.get()
        # time.sleep(1)
        print(f"(child process) Well, hi {name}")


def sendName2():
    q = Queue()

    p1 = Process(target=greet2, args=(q,))
    p1.start()

    for i in range(5):
        time.sleep(1)
        print(f"(parent process) Ok, I'll send the name")
        q.put(f"Jimmy {i}")


sendName2()