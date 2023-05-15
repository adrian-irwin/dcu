#!/usr/bin/env python3

class Student(object):

    def __init__(self, name, address, sid):
        self.name = name
        self.address = address
        self.sid = sid

    def __str__(self):
        return f"Name: {self.name}\nAddress: {self.address}\nID: {self.sid}"

def sort_on_id(s):
    return s.sid

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

    def __str__(self):
        return "\n".join([f"{s}" for s in sorted(self.students.values(), key=sort_on_id)])
