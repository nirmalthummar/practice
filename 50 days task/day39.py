import random
import string

def generate_password(strength):
    if strength == "weak":
        password_length = 5
    elif strength == "strong":
        password_length = 8
    elif strength == "very strong":
        password_length = 12
    else:
        print("Invalid strength. Please choose from weak, strong, or very strong.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    return password

# Example usage
strength = input("Choose password strength (weak, strong, or very strong): ")
password = generate_password(strength)
print("Generated password:", password)
