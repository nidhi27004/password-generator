import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = " ".join(random.choice(characters) for _ in range(length))
   
    return password
print("Random Password Generator")
try:
    length = int(input("enter desired password length:"))
    if length<4:
        print("Password should be atleast 4 characters long")
    else:
        print("Generated Password",generate_password(length))
except ValueError:
    print("Please enter a valid number")
