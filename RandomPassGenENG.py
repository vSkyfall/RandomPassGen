import random
import string

# Function to generate a password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    # string.ascii_letters: Lowercase and uppercase letters (a-z, A-Z).
    # string.digits: Numbers (0-9).
    # string.punctuation: Symbols (like !@#$%^&*).
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    # random.choice(characters): Selects a random character from the pool.
    # for _ in range(length): Repeats the selection for the specified length.
    # ''.join(...): Combines the selected characters into a single string (the password).
    
    return password

# Get the password length from the user
try:
    length = int(input("Enter the password length: "))
    if length < 6:
        print("The password must be at least 6 characters long.")
    else:
        print("Generated password:", generate_password(length))
except ValueError:
    print("Please enter a valid number.")
