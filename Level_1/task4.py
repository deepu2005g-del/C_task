while True:
    try:
        num1 = float(input("Enter first number: "))
        break
    except ValueError:
        print("Please enter a valid number")

while True:
    try:
        num2 = float(input("Enter second number: "))
        break
    except ValueError:
        print("Please enter a valid number")

while True:
    op = input("Enter operator (+, -, *, /, %): ")
    if op in ["+", "-", "*", "/", "%"]:
        break
    else:
        print("Invalid operator")

if op == "+":
    print("Addition:", num1 + num2)
elif op == "-":
    print("Subtraction:", num1 - num2)
elif op == "*":
    print("Multiplication:", num1 * num2)
elif op == "/":
    if num2 != 0:
        print("Division:", num1 / num2)
    else:
        print("Cannot divide by zero")
elif op == "%":
    if num2 != 0:
        print("Modulus:", num1 % num2)
    else:
        print("Cannot divide by zero")