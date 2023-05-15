# Name: Adrian Irwin
# Student Number: 20415624
# I acknowledge that the work submitted in this assignment is my own work and does not breach the DCU Academic Integrity Policy.

from error_handler import *


def file_handler(sys_argv):
    """Opens a file and returns the content as a list."""
    filename = ""
    if argv_check(sys_argv):
        filename = sys_argv[1]

    tasks = []

    if check_file_exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                if len(line.strip()) > 0:       # ignore empty lines
                    tasks.append(line.strip())
        return tasks
