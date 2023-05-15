#!/usr/bin/env python3

class MP3Track(object):

    def __init__(self, title, duration, artists=None):
        if artists is None:
            artists = []
        self.title = title
        self.duration = duration
        self.artists = artists

    def __str__(self):
        return f"Title: {self.title}\nBy: {', '.join(self.artists)}\nDuration: {self.duration}"

class MP3Collection(object):

    def __init__(self, collection=None):
        if collection is None:
            collection = {}
        self.collection = collection

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

    def get_mp3s_by_artist(self, artist):
        songList = []
        for item in self.collection.values():
            if artist in item.artists:
                songList.append(item)
        return songList

    def __add__(self, other):
        finalDict = {}
        for i in self.collection:
            finalDict[i.title] = i
        for j in other.collection:
            finalDict[j.title] = j
        return MP3Collection(finalDict)
