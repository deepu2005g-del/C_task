# Task 1: Guessing Game

import random

number = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess a number (1-100): "))
    except ValueError:
        print("Please enter a valid number")
        continue

    if guess < 1 or guess > 100:
        print("Enter number between 1 and 100")
    elif guess < number:
        print("The value you guessed is too low")
    elif guess > number:
        print("The value you guessed is too high")
    else:
        print("Correct! You guessed it.")
        break