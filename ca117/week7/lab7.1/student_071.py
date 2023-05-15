#!/usr/bin/env python3

class Student(object):

    def __init__(self, surname, forename, sid, modlist=None):
        if modlist is None:
            modlist = []
        self.sid = sid
        self.surname = surname
        self.forename = forename
        self.modlist = modlist

    def add_module(self, module):
        if module not in self.modlist:
            self.modlist.append(module)

    def del_module(self, module):
        if module in self.modlist:
            self.modlist.remove(module)

    def print_details(self):
        print(f"ID: {self.sid}")
        print(f"Surname: {self.surname}")
        print(f"Forename: {self.forename}")
        print(f"Modules: {' '.join(self.modlist)}")
