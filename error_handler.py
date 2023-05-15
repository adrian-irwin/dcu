# Name: Adrian Irwin
# Student Number: 20415624
# I acknowledge that the work submitted in this assignment is my own work and does not breach the DCU Academic Integrity Policy.

import os


def argv_check(sys_argv):
    """Checks if the given system arguments are valid.
    To be valid, the program only accepts 2 arguments: the program name and the input file name."""
    if len(sys_argv) != 2:
        print(f"Error: Invalid number of arguments({len(sys_argv)}).")
        exit(1)
    else:
        return True


def check_file_exists(filename):
    """Checks if the given file exists."""
    if not os.path.isfile(filename):
        print(f"Error: File does not exist.")
        exit(1)
    else:
        return True


def task_check(tasks, line_number):
    """Checks if the given scheduler task has a valid number of tasks (3)."""
    if len(tasks) != 3:
        print(f"Error: Invalid number of items({len(tasks)}) in schedule task on line {line_number + 1}.")
        exit(1)
    else:
        return True


def priority_check(priority, line_number):
    """Checks if the scheduler task has a valid priority (1-10)."""
    try:
        priority = int(priority.strip())
    except ValueError:
        print(f"Error: Invalid priority level({priority}) on line {line_number + 1}.")
        exit(1)

    if priority not in range(1, 11):
        print(f"Error: Invalid priority level({priority}) on line {line_number + 1}.")
        exit(1)
    else:
        return True


def burst_check(burst, line_number):
    """Checks if the scheduler task has a valid burst time (an integer that is greater than 0)."""
    try:
        burst = int(burst.strip())
    except ValueError:
        print(f"Error: Invalid burst time({burst}) on line {line_number + 1}.")
        exit(1)

    if burst < 0 and burst is not type(int):
        print(f"Error: Invalid burst time({burst}) on line {line_number + 1}.")
        exit(1)
    else:
        return True
