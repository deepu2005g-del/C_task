# Task 4: Fibonacci Sequence

def fibonacci(n):
    print("Fibonacci Sequence:")
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

while True:
    try:
        num = int(input("Enter number of terms: "))
        if num > 0:
            break
        else:
            print("Please enter a positive number")
    except ValueError:
        print("Please enter a valid number")
fibonacci(num)