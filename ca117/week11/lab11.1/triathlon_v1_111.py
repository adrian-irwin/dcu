#!/usr/bin/env python3

class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def __str__(self):
        return f"Name: {self.name}\nID: {self.tid}"


class Triathlon(object):

    def __init__(self):
        self.triathletes = {}

    def add(self, triathlete):
        self.triathletes[triathlete.tid] = triathlete

    def remove(self, tid):
        del(self.triathletes[tid])

    def lookup(self, tid):
        if tid in self.triathletes:
            return self.triathletes[tid]
        else:
            return None
