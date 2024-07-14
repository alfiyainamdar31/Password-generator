import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    print("Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("Enter the length of the password you want to generate: "))
            if length <= 0:
                print("Please enter a positive integer for the length.")
                continue
            else:
                password = generate_password(length)
                print("Your generated password is:", password)
                break
        except ValueError:
            print("Please enter a valid integer for the length.")
