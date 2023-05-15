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

    def __str__(self):
        return f"Name: {self.name}\nAddress: {self.address}\nID: {self.sid}"
