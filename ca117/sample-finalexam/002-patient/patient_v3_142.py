#!/usr/bin/env python3

class Patient(object):

    def __init__(self, name, age, doctor, medications=None):
        if medications is None:
            medications = []
        self.medications = medications
        self.name = name
        self.age = age
        self.doctor = doctor

    def add_medication(self, medication):
        self.medications.append(medication)

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nMedications: {', '.join(self.medications)}\nDoctor: {self.doctor}"
