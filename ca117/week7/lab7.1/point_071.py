#!/usr/bin/env python3

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def reflect(self):
        self.x = self.x * -1
        self.y = self.y * -1

    def distance(self, point2):
        return (((point2.x - self.x) ** 2) + ((point2.y - self.y) ** 2)) ** 0.5
