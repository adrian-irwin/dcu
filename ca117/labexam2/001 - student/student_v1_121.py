#!/usr/bin/env python3

class Student(object):

    def __init__(self, name, address, sid):
        self.name = name
        self.address = address
        self.sid = sid

    def __str__(self):
        return f"Name: {self.name}\nAddress: {self.address}\nID: {self.sid}"
