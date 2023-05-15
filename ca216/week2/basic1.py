from multiprocessing import *


def sayHi():
    print(f"Hi from process {current_process().pid}")


def procEx():
    print(f"Hi from process {current_process().pid} (parent process)")

    otherProc = Process(target=sayHi, args=())
    otherProc2 = Process(target=sayHi, args=())
    otherProc3 = Process(target=sayHi, args=())

    otherProc.start()
    otherProc2.start()
    otherProc3.start()


procEx()