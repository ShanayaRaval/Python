import random
import string


def generate_password(length=12):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits

    all_characters = lowercase + uppercase + digits

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
    ]

    for _ in range(length - 3):
        password.append(random.choice(all_characters))

    random.shuffle(password)

    return "".join(password)


password_length = int(input("Enter desired password length: "))
generated_password = generate_password(password_length)
print("Generated Password:", generated_password)