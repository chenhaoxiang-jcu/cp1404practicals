"""
Emails
Estimate: 20 minutes
Actual:   22 minutes
"""


def main():
    """Get user's email address and name to print."""
    email_to_name = {}
    email = input('Email: ')
    while email != '':
        name = extract_name(email)
        name_check = input(f"Is your name {name}? (Y/N) ").upper()
        if name_check != 'Y' and name_check != '':
            name = input('Name: ')
        email_to_name[email] = name
        email = input('Email: ')
    print()
    display_name_and_email(email_to_name)


def extract_name(email: str):
    """Extract name from email."""
    name = email.split('@')[0].replace('.', ' ').title()
    return name


def display_name_and_email(email_to_name: dict):
    """Print name and email."""
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


main()
