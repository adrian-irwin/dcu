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

def sort_on_id(s):
    return s.sid

def sort_on_value(s):
    return s[1]

class Classlist(object):

    def __init__(self):
        self.students = {}

    def add(self, student):
        self.students[student.sid] = student

    def remove(self, sid):
        del (self.students[sid])

    def lookup(self, sid):
        if sid in self.students:
            return self.students[sid]
        else:
            return None

    def least_popular_module(self):
        modules = {}
        for student in self.students.values():
            for module in student.marks:
                if module not in modules.keys():
                    modules[module] = 1
                else:
                    modules[module] += 1

        return sorted(modules.items(), key=sort_on_value)[0][0]

    def __str__(self):
        return "\n".join([f"{s}" for s in sorted(self.students.values(), key=sort_on_id)])
