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
