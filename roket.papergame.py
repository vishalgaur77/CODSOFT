# Task: CodSoft Internship
# Project: ROCK–PAPER–SCISSORS GAME/ etc
# rendom chose proper simple logic 
# Author: Vishal Gaur
# Description: Simple besic application using Python

import random   

print("=== Rock Paper Scissors Game ===")
choices = ["rock", "paper", "scissors"]

user_choice = input("Choose rock, paper, or scissors: ").lower()
computer_choice = random.choice(choices)

print("Computer chose:", computer_choice)

if user_choice == computer_choice:
    print("It's a Tie!")
elif (
    (user_choice == "rock" and computer_choice == "scissors") or
    (user_choice == "paper" and computer_choice == "rock") or
    (user_choice == "scissors" and computer_choice == "paper")
):
    print("You Win!")
else:
    print("Computer Wins!")




