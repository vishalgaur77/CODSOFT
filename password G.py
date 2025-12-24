# Task: CodSoft Internship
# Project: Calculator / Todo / roket game/password g./ complete
# all task
# Author: Vishal Gaur
# Description: using Python


import random
import string

print("=== Password Generator ===")

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation
password = ""

for i in range(length):
    password += random.choice(characters)

print("Generated Password:", password)




