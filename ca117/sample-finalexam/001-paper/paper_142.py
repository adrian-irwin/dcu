#!/usr/bin/env python3

# rock paper scissors

# paper beats rock
# rock beats scissors
# scissors beats paper

import sys

lines = [line.strip() for line in sys.stdin]

for item in lines:
    tokens = item.split()
    p1 = tokens[0]
    p2 = tokens[1]
    if p1 == "paper" and p2 == "rock":
        print("Player 1 wins")
    elif p1 == "rock" and p2 == "scissors":
        print("Player 1 wins")
    elif p1 == "scissors" and p2 == "paper":
        print("Player 1 wins")
    elif p1 == "rock" and p2 == "paper":
        print("Player 2 wins")
    elif p1 == "paper" and p2 == "scissors":
        print("Player 2 wins")
    elif p1 == "scissors" and p2 == "rock":
        print("Player 2 wins")
    elif p1 == "scissors" and p2 == "scissors":
        print("Draw")
    elif p1 == "rock" and p2 == "rock":
        print("Draw")
    elif p1 == "paper" and p2 == "paper":
        print("Draw")
