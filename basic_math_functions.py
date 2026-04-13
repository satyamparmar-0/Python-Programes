import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def modulus(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x % y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error: Cannot take square root of a negative number"
    return math.sqrt(x)

def floor_division(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x // y

def absolute_value(x):
    return abs(x)

def factorial(x):
    if x < 0:
        return "Error: Factorial is not defined for negative numbers"
    if not isinstance(x, int):
        return "Error: Factorial requires an integer"
    return math.factorial(x)

while True:
    print("\n--- Basic Mathematics Functions ---")
    print("1.  Addition")
    print("2.  Subtraction")
    print("3.  Multiplication")
    print("4.  Division")
    print("5.  Modulus")
    print("6.  Power")
    print("7.  Square Root")
    print("8.  Floor Division")
    print("9.  Absolute Value")
    print("10. Factorial")
    print("0.  Exit")

    choice = input("\nEnter your choice: ").strip()

    if choice == '0':
        print("Goodbye!")
        break
    elif choice in ('1', '2', '3', '4', '5', '6', '8'):
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        if choice == '1':
            print("Result:", add(x, y))
        elif choice == '2':
            print("Result:", subtract(x, y))
        elif choice == '3':
            print("Result:", multiply(x, y))
        elif choice == '4':
            print("Result:", divide(x, y))
        elif choice == '5':
            print("Result:", modulus(x, y))
        elif choice == '6':
            print("Result:", power(x, y))
        elif choice == '8':
            print("Result:", floor_division(int(x), int(y)))
    elif choice == '7':
        x = float(input("Enter number: "))
        print("Result:", square_root(x))
    elif choice == '9':
        x = float(input("Enter number: "))
        print("Result:", absolute_value(x))
    elif choice == '10':
        x = int(input("Enter a non-negative integer: "))
        print("Result:", factorial(x))
    else:
        print("Invalid choice. Please try again.")
