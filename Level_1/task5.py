# Task 5: palindrome checker

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

text = input("Enter a string: ")

if is_palindrome(text):
    print("Palindrome")
else:
    print("Not a Palindrome")