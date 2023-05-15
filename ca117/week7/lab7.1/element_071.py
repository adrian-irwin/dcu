#!/usr/bin/env python3

class Element(object):

    def __init__(self, number, name, symbol, boiling):
        self.number = number
        self.name = name
        self.symbol = symbol
        self.boiling = boiling

    def print_details(self):
        print(f"Number: {self.number}")
        print(f"Name: {self.name}")
        print(f"Symbol: {self.symbol}")
        print(f'Boiling point: {self.boiling} K')
