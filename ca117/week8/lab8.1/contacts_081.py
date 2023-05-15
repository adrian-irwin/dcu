#!/usr/bin/env python3

class Contact(object):

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return self.name, self.phone, self.email

class ContactList(object):

    def __init__(self, d=None):
        if d is None:
            d = {}
        self.d = d

    def add_contact(self, contact):
        self.d[contact.name] = (contact.phone, contact.email)

    def del_contact(self, contact):
        if contact in self.d:
            del(self.d[contact])

    def get_contact(self, contact):
        if contact in self.d:
            return contact + " " + " ".join(self.d[contact])

    def __str__(self):
        contacts = []
        for item in self.d:
            contacts.append(item + " " + " ".join(self.d[item]))
        return "Contact list\n" + "-" * 12 + "\n" + "\n".join(sorted(contacts))
