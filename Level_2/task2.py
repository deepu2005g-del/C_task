# Task 2: Number Guesser

import random

while True:
    try:
        low = int(input("Enter lower range: "))
        break
    except ValueError:
        print("Please enter a valid number")

while True:
    try:
        high = int(input("Enter upper range: "))
        if high > low:
            break
        else:
            print("Upper range must be greater than lower range")
    except ValueError:
        print("Please enter a valid number")

number = random.randint(low, high)

while True:
    try:
        guess = int(input(f"Guess a number ({low}-{high}): "))
    except ValueError:
        print("Please enter a valid number")
        continue

    if guess < low or guess > high:
        print(f"Enter number between {low} and {high}")
    elif guess > number:
        print("The value you guessed is too high!")
    elif guess < number:
        print("The value you guessed is too low!")
    else:
        print("Correct! You guessed it.")
        break