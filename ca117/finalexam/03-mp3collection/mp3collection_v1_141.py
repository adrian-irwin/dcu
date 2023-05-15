#!/usr/bin/env python3

class MP3Track(object):

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def __str__(self):
        return f"Title: {self.title}\nDuration: {self.duration}"

class MP3Collection(object):

    def __init__(self):
        self.collection = {}

    def add(self, track):
        self.collection[track.title] = track

    def remove(self, title):
        if title in self.collection.keys():
            del(self.collection[title])

    def lookup(self, title):
        if title in self.collection:
            return self.collection[title]
        else:
            return None
