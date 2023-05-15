from Stack import Stack
import sys

def reverse_input(stack):
    n = sys.stdin.readlines()
    for line in n:
        line = line.strip()
        stack.push(line)
    while not stack.is_empty():
        print(stack.pop())