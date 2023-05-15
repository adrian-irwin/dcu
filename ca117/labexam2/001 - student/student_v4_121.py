#!/usr/bin/env python3

class Student(object):

    def __init__(self, name, address, sid):
        self.name = name
        self.address = address
        self.sid = sid
        self.marks = {}

    def add_mark(self, module, mark):
        self.marks[module] = mark

    def get_mark(self, module):
        if module in self.marks:
            return self.marks[module]
        else:
            return "Not registered for module"

    def avg_mark(self):
        if len(self.marks) > 0:
            avg = [n for n in self.marks.values()]
            return sum(avg) / len(self.marks.values())
        else:
            return 0

    def __eq__(self, other):
        return self.avg_mark() == other.avg_mark()

    def __gt__(self, other):
        return self.avg_mark() > other.avg_mark()

    def __lt__(self, other):
        return self.avg_mark() < other.avg_mark()

    def __str__(self):
        return f"Name: {self.name}\nAddress: {self.address}\nID: {self.sid}\nAverage mark: {self.avg_mark():.2f}"
