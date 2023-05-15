#!/usr/bin/env python3

class Patient(object):

    def __init__(self, name, age, doctor, medications=None):
        if medications is None:
            self.medications = []
        self.name = name
        self.age = age
        self.doctor = doctor
        self.medications = medications

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nMedications: {', '.join(self.medications)}\nDoctor: {self.doctor}"
