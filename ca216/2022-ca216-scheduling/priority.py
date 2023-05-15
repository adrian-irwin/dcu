# Name: Adrian Irwin
# Student Number: 20415624
# I acknowledge that the work submitted in this assignment is my own work and does not breach the DCU Academic Integrity Policy.

from list import handle_tasks, sort_tasks
from scheduler import scheduler


def pri(task):
    return task['pri']


def priority():
    tasks = handle_tasks()
    tasks = sort_tasks(tasks, pri, True)
    print(f"\nPriority Scheduler:\n")
    scheduler("priority", tasks)


if __name__ == "__main__":
    priority()
