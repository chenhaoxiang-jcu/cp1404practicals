MINIMUM_LENGTH = 8

password = input("Password: ")
while len(password) < MINIMUM_LENGTH:
    print(f"Password must be at least {MINIMUM_LENGTH} characters long.")
    password = input("Password: ")
password_length = len(password)
print('*' * password_length)
