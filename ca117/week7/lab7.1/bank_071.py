#!/usr/bin/env python3

class BankAccount(object):

    def __init__(self, balance=0.00):
        self.balance = float(balance)

    def deposit(self, amount):
        self.balance += float(amount)

    def withdraw(self, amount):
        if float(amount) <= self.balance:
            self.balance -= float(amount)
        else:
            print("Insufficient funds available")

    def print_details(self):
        print(f"Your current balance is: {self.balance:.2f} euro")
