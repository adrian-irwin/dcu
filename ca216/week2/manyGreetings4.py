from multiprocessing import *


def sayHi3(personName):
    print(f"Hi {personName} from process {current_process().name} - pid {current_process().pid}")


def manyGreetings3():
    print(f"Hi from process {current_process().pid} (parent process)")

    personName = "Jimmy"
    for i in range(10):
        Process(target=sayHi3, args=(personName,), name=str(i)).start()


def sayHi4(lock, name):
    lock.acquire()
    print(f"Hi {name} from process {current_process().pid}")
    lock.release()


def manyGreetings4():
    lock1 = Lock()
    print(f"Hi from process {current_process().pid} (parent process)")
    for i in range(10):
        Process(target=sayHi4, args=(lock1, "p"+str(i))).start()

manyGreetings4()