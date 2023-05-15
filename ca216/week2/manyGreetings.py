from multiprocessing import *

def sayHi2(n):
    print("Hi", n, "from process", current_process().pid)

def manyGreetings():
    print("Hi from process", current_process().pid, "(main process)")
    
    name = input("Enter your name:")
    numOfProc = int(input("Enter the number of processes you wan to make:"))
    for i in range(numOfProc):
        otherProc = Process(target=sayHi2, args=(name,))
        otherProc.start()


manyGreetings()