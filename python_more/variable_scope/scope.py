# Global variable
name = "Global Name"

def show_name():
    # Local variable with the same name
    name = "Local Name"
    print("Inside function:", name)

show_name()
print("Outside function:", name)
# This script demonstrates the use of variable scope in Python.