fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
  print(fruit)

  colors = ("red", "green", "blue")

for color in colors:
  print(color)

  message = "Hello, world!"

for character in message:
  print(character)

for number in range(1, 6):
  print(number)


for x in range(5):
  for y in range(3):
    print(f"({x}, {y})")

numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
  total += num
print("Numbers:", numbers)
print("Total:", total)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# multiplication table
for i in range(1, 11):
  # Outer loop iterates through rows (multiplication factors)
  for j in range(1, 11):
    # Inner loop iterates through columns (other factors)
    product = i * j
    print(f"{i} x {j} = {product}", end="\t")  # Print with tabs for better formatting
  print()  # Move to a new line after each row


#rught angle triangle of asterisks
rows = 5

for i in range(1, rows + 1):
  # Outer loop controls the number of rows
  for j in range(1, i + 1):
    # Inner loop prints asterisks for each row
    print("*", end="")
  print()  # Move to a new line after each row of asterisks

