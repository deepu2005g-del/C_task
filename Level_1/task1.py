# Task 1: string reversal

def reverse_string(s):
    return s[::-1]

text = input("Enter a string to reverse: ")
result = reverse_string(text)
print("Reversed string: ", result)