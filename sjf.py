# Name: Adrian Irwin
# Student Number: 20415624
# I acknowledge that the work submitted in this assignment is my own work and does not breach the DCU Academic Integrity Policy.

from list import handle_tasks, sort_tasks
from scheduler import scheduler


def burst(task):
    return task['burst']


def sjf():
    tasks = handle_tasks()
    tasks = sort_tasks(tasks, burst)
    print(f"\nShortest-job-first (SJF) Scheduler:\n")
    scheduler("sjf", tasks)


if __name__ == "__main__":
    sjf()
