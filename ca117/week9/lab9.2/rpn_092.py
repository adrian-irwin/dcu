#!/usr/bin/env python3

import math


class Stack(object):

    def __init__(self):
        self.l = []

    def push(self, e):
        self.l.append(e)

    def pop(self):
        return self.l.pop()

    def top(self):
        return self.l[-1]

    def is_empty(self):
        return len(self.l) == 0

    def __len__(self):
        return len(self.l)


binops = {"+": float.__add__,
          "-": float.__sub__,
          "*": float.__mul__,
          "/": float.__truediv__
          }
uniops = {"n": float.__neg__,
          "r": math.sqrt}


def calculator(line):
    s = Stack()

    for c in line.split():

        if c not in binops and c not in uniops:  # put numbers into stack
            s.push(float(c))
        elif c in uniops:  # check if c is an operator which takes one number/argument, remove last number from stack then apply operator on number then put answer back in the stack
            arg = s.pop()
            s.push(uniops[c](arg))
        elif c in binops:  # check if c is an operator which takes two number/arguments, remove last two numbers from stack, make them variables, apply operator on numbers then put answer back in the stack
            rarg = s.pop()
            larg = s.pop()
            s.push(binops[c](larg, rarg))
        else:  # if c is not a number or operator, raise an index error, which means we dont have a valid rpn expression
            raise IndexError

    if len(s) != 1:  # if the len of s is more than one that means there was not enough numbers/operators to give a final answer meaning we dont have a valid rpn expression
        raise IndexError

    return s.pop()  # if there are no errors return the final answer
