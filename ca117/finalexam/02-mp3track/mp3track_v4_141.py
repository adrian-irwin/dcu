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
        time = divmod(self.duration, 60)
        return f"Title: {self.title}\nBy: {', '.join(self.artists)}\nDuration: {time[0]}:{time[1]:02d}"
