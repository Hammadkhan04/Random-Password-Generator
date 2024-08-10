# #create a generate pasword program

import random
import string

def generate_password(length=20):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

password_len = 20  # Length of the password
generated_password = generate_password(password_len)

print("Your Password is:", generated_password)
