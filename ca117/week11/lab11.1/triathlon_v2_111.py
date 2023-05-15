#!/usr/bin/env python3

class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def __str__(self):
        return f"Name: {self.name}\nID: {self.tid}"

def sort_on(t):
    return t.name

class Triathlon(object):

    def __init__(self):
        self.triathletes = {}

    def add(self, t):
        self.triathletes[t.tid] = t

    def remove(self, tid):
        del (self.triathletes[tid])

    def lookup(self, tid):
        if tid in self.triathletes:
            return self.triathletes[tid]
        else:
            return None

    def __str__(self):
        printList = [f"{s}" for s in sorted(self.triathletes.values(), key=sort_on)]
        return "\n".join(printList)
