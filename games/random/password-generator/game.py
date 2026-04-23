import random
import string

AUTHOR = "SouLCodes-main"

def generate_password(length: int) -> str:
    """Generate a random password of the given length."""
    characters = string.ascii + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def run():
    print(f"Welcome to the Password Generator by {AUTHOR} !")
    Length = int(input("Enter the desired password length: "))
    password = generate_password(Length)
    print(f"Generated password: {password}")
