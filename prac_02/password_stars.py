MINIMUM_LENGTH = 8


def main():
    """Get password and print asterisks."""
    password = get_valid_password()
    display_asterisks(password)


def get_valid_password():
    """Get password with valid length."""
    password = input("Password: ")
    while len(password) < MINIMUM_LENGTH:
        print(f"Password must be at least {MINIMUM_LENGTH} characters long.")
        password = input("Password: ")
    return password


def display_asterisks(password):
    """Print asterisks based on password length."""
    password_length = len(password)
    print('*' * password_length)


main()
