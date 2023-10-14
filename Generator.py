import random
import string
import time

def generate_lowercase():
    return random.choice(string.ascii_lowercase)

def generate_uppercase():
    return random.choice(string.ascii_uppercase)

def generate_digits():
    return random.choice(string.digits)

def generate_symbols():
    symbols = "[]{}#()*;._-"
    return random.choice(symbols)

def generate_password():
    password = [
        generate_lowercase(),
        generate_uppercase(),
        generate_digits(),
        generate_symbols()
    ]

    remaining_length = 10 - len(password)
    all_characters = string.ascii_letters + string.digits + "[]{}#()*;._-"
    password.extend(random.choices(all_characters, k=remaining_length))
    random.shuffle(password)

    return ''.join(password)

def display_loading_screen():
    print("Wird generiert...")
    time.sleep(4)  # Simulate a loading delay

def display_password(password):
    print("Das Passwort lautet:", password)

def main():
    display_loading_screen()
    generated_password = generate_password()
    display_password(generated_password)

if __name__ == "__main__":
    main()
