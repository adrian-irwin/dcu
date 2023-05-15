#!/usr/bin/env python3

class MP3Track(object):

    def __init__(self, title, duration, artists=None):
        if artists is None:
            artists = []
        self.title = title
        self.duration = duration
        self.artists = artists

    def add_artist(self, artist):
        self.artists.append(artist)

    def __str__(self):
        return f"Title: {self.title}\nBy: {', '.join(self.artists)}\nDuration: {self.duration}"
