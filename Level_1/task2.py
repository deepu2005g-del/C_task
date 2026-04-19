# Task 2: temperature conversion

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

while True:
    try:
        value = float(input("Enter the temperature value: "))
        break
    except ValueError:
        print("Please enter a valid temperature value")

while True:  
    unit = input("Enter the unit (C/F): ").upper()

    if unit == "C":
        result = celsius_to_fahrenheit(value)
        print("Fahrenheit: ", result)
        break
    elif unit == "F":   
        result = fahrenheit_to_celsius(value)
        print("Celsius: ", result)
        break
    else:
        print("Please enter a valid unit")
    