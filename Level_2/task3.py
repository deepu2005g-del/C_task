# Task 3: Password Strength Checker

import re

def check_password(password):
    length = len(password) >= 8
    upper = re.search(r'[A-Z]', password)
    lower = re.search(r'[a-z]', password)
    digit = re.search(r'[0-9]', password)
    special = re.search(r'[@$!%*?&]', password)

    if length and upper and lower and digit and special:
        return "Strong Password"
    else:
        return "Weak Password"

password = input("Enter password: ")
print(check_password(password))