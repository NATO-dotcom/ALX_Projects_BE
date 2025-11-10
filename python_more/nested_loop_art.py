#isosceles triangle art using nested loops
rows=5
count=1
while count <= rows:
    # Print leading spaces
    for space in range(rows - count):
        print(" ", end="")
    
    # Print asterisks
    for star in range(2 * count - 1):
        print("*", end="")
    
    print()  # Move to the next line
    count += 1
