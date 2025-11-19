# calculator.py
#user input
#a = float(input("Enter first number: "))
#b = float(input("Enter second number: "))
#operation = input("Enter operation (+, -, *, /): ")
# functions for operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b
