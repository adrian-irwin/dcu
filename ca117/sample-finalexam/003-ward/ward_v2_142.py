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

class Ward(object):

    def __init__(self):
        self.patients = {}

    def add(self, patient):
        self.patients[patient.name] = patient

    def remove(self, name):
        del(self.patients[name])

    def lookup(self, name):
        if name in self.patients:
            return self.patients[name]
        else:
            return None

    def get_patients_by_medication(self, medication):
        patientList = []
        for item in self.patients.values():
            if medication in item.medications:
                patientList.append(item)
        return patientList
