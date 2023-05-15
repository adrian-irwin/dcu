#!/usr/bin/env python3

class Point(object):

    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)

    def midpoint(self, point2):
        return Point(((self.x + point2.x) / 2), ((self.y + point2.y) / 2))

    def __str__(self):
        return f"({self.x}, {self.y})"

class Circle(object):

    def __init__(self, centre=Point(), radius=0.0):
        self.radius = radius
        self.centre = centre

    def __add__(self, other):
        return Circle(self.centre.midpoint(other.centre), self.radius + other.radius)

    def __str__(self):
        return f"Centre: {self.centre}\n" + f"Radius: {self.radius}"
