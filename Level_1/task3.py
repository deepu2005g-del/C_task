import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z][a-zA-Z0-9]+@(gmail\.com|yahoo\.com|outlook\.com)$'
    return re.match(pattern, email)

email = input("Enter email: ")

if is_valid_email(email):
    print("Valid Email")
else:
    print("Invalid Email")

