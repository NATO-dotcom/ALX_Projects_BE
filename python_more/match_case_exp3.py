def has_id(user):
    # Add your ID verification logic here
    return True  # For demonstration, always returns True

# Example usage:
age = 18
user = {}  # Add user object or get it from your system

match age:
    case 18 | 19:  # Match multiple values with pipe (|)
        if age >= 18 and has_id(user):  # Guard using a function call
            print("You are eligible to vote.")
        else:
            print("You need a valid ID to vote.")
    case _:
        print("You are not yet eligible to vote.")