#!/usr/bin/env python3

class Score(object):

    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points
        self.full_score = (goals * 3) + points

    def __eq__(self, other):
        return self.full_score == other.full_score

    def __ne__(self, other):
        return self.full_score != other.full_score

    def __gt__(self, other):
        return self.full_score > other.full_score

    def __ge__(self, other):
        return self.full_score >= other.full_score

    def __lt__(self, other):
        return self.full_score < other.full_score

    def __le__(self, other):
        return self.full_score <= other.full_score

    def __add__(self, other):
        return Score(self.goals + other.goals, self.points + other.points)

    def __sub__(self, other):
        return Score(self.goals - other.goals, self.points - other.points)

    def __iadd__(self, other):
        z = self + other
        self.goals, self.points = z.goals, z.points
        return self

    def __isub__(self, other):
        z = self - other
        self.goals, self.points = z.goals, z.points
        return self

    def __str__(self):
        return f"{self.goals} goal(s) and {self.points} point(s)"
