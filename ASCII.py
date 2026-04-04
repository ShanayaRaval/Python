import string

char = input("Enter a character: ")

if char in string.ascii_letters:
    print(f"'{char}' is an ASCII letter.")
elif char in string.digits:
    print(f"'{char}' is an ASCII digit.")
else:
    print(f"'{char}' is not a standard ASCII letter or digit.")