book = {
    "title": "Atomic Habits",
    "author": "James Clear",
    "genre": "Self-help"
}

# Retrieve the genre using get()
print(book.get("genre"))
# Add a new key-value pair for publication year
book["publication_year"] = 2018
print(book)
# Update the author name
book["author"] = "J. Clear"
print(book)
# Remove the genre key-value pair
book.pop("genre")
print(book)
# This script demonstrates basic dictionary operations in Python.   