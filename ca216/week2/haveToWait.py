from multiprocessing import *
import time


def slowpoke(lock):
    time.sleep(10)
    lock.acquire()
    print(f"Slowpoke: Ok, I',m coming")
    lock.release()


def haveToWait():
    lock = Lock()
    p1 = Process(target=slowpoke, args=(lock,))
    p1.start()
    print(f"Waiter: Any day now...")

    p1.join()
    print(f"Waiter: Finally! Geez.")


haveToWait()