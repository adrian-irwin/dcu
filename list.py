# Name: Adrian Irwin
# Student Number: 20415624
# I acknowledge that the work submitted in this assignment is my own work and does not breach the DCU Academic Integrity Policy.

from sys import argv
from queue import Queue
import file_handler as fh
import error_handler as eh

# task name, priority, CPU burst


def handle_tasks():
    """Takes tasks from a given file and adds them to a queue. Returns the queue of tasks."""
    tasks = Queue()
    lines = fh.file_handler(argv)
    for i, line in enumerate(lines):
        line = line.split(",")
        eh.task_check(line, i)
        eh.priority_check(line[1], i)
        eh.burst_check(line[2], i)
        task = {
            "name": line[0],
            "pri": int(line[1]),
            "burst": int(line[2]),
        }
        tasks.put(task)
    return tasks


def sort_tasks(unsorted, sortOn, rev=False):
    """Sorts a queue of tasks based on a given sortOn function. Returns the sorted queue."""
    sortedTasks = Queue()

    # add tasks into a temp array before sorting
    temp = []
    for i in range(unsorted.qsize()):
        temp.append(unsorted.get())

    # sort the temp array
    temp.sort(key=sortOn, reverse=rev)

    # put tasks back into queue after being sorted
    for i in range(len(temp)):
        sortedTasks.put(temp[i])

    return sortedTasks
