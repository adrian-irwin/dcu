from multiprocessing import *


def workerHello(lock, worker, holeNum):
    lock.acquire()
    print(f"Hiddy-ho!  I'm worker {worker} and today I have to dig hole {holeNum}")
    lock.release()


def assignDiggers():
    workers = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    lock1 = Lock()

    for i, worker in enumerate(workers):
        Process(target=workerHello, args=(lock1, worker, i)).start()


assignDiggers()