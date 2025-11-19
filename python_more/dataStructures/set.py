import random

# Generate random set of numbers between 1 and 10
numbers = [random.randint(1, 10) for _ in range(10)]

# Convert to a set to remove duplicates
unique_numbers = set(numbers)

print("Generated numbers:", numbers)
print("Unique numbers:", unique_numbers)
# This script demonstrates basic set operations in Python.
