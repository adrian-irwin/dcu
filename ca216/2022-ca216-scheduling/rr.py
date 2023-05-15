# Name: Adrian Irwin
# Student Number: 20415624
# I acknowledge that the work submitted in this assignment is my own work and does not breach the DCU Academic Integrity Policy.

from list import handle_tasks
from scheduler import scheduler

# each task will only run for a max of the time quantum then go to the next task.
timeQuantum = 10


def roundRobin():
    tasks = handle_tasks()
    print(f"\nRound-robin (RR) Scheduler with time quantum of {timeQuantum}:\n")
    scheduler("rr", tasks, timeQuantum)


if __name__ == "__main__":
    roundRobin()
