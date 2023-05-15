#!/usr/bin/env python3

class Triathlete(object):

    def __init__(self, name, tid, sports=None):
        if sports is None:
            sports = {}
        self.sports = sports
        self.name = name
        self.tid = tid
        self.raceTime = 0

    def add_time(self, sport, time):
        self.raceTime += int(time)
        self.sports[sport] = time

    def get_time(self, sport):
        if sport in self.sports:
            return self.sports[sport]

    def __str__(self):
        return f"Name: {self.name}\nID: {self.tid}\nRace time: {self.raceTime}"
