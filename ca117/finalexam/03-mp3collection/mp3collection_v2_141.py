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

    def get_mp3s_by_artist(self, artist):
        songList = []
        for item in self.collection.values():
            if artist in item.artists:
                songList.append(item)
        return songList
