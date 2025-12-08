def divide(x, y):
  if y == 0:
    raise ZeroDivisionError("Division by zero is not allowed")
  return x / y

try:
    print(divide(10, 2))
    print(divide(5, 0))  # This will be caught
except ZeroDivisionError as e:
    print("Error:", e)

