# Name: Adrian Irwin
# Student Number: 20415624
# I acknowledge that the work submitted in this assignment is my own work and does not breach the DCU Academic Integrity Policy.

from list import handle_tasks
from scheduler import scheduler


def fcfs():
    tasks = handle_tasks()
    print(f"\nFirst-come, first-served (FCFS) Scheduler:\n")
    scheduler("fcfs", tasks)


if __name__ == "__main__":
    fcfs()
