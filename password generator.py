import random
import string

# Function to generate password
def generate_password(length):
    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    # Combine all the character sets
    all_characters = lower + upper + digits + special
    
    # Generate a random password using the specified length
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

# Main function to prompt user and display password
def password_generator():
    print("Welcome to the Password Generator!")
    
    try:
        # Ask the user for the desired password length
        length = int(input("Enter the desired password length: "))
        
        if length < 4:
            print("Password length should be at least 4 characters for a strong password.")
        else:
            # Generate and display the password
            password = generate_password(length)
            print(f"Generated password: {password}")
    except ValueError:
        print("Please enter a valid number for the password length.")

# Run the Password Generator
password_generator()
