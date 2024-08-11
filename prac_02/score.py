import random

PASS_THRESHOLD = 50
EXCELLENT_THRESHOLD = 90


def main():
    """Ask the user for their score and print the result, then get a random score and print the result."""
    score = float(input("Enter score: "))
    message = determine_message(score)
    print(message)
    score = random.randint(0, 100)
    message = determine_message(score)
    print(f"{score} is considered {message}")


def determine_message(score):
    """Determine the appropriate message based on the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    if score < PASS_THRESHOLD:
        return "Bad"
    if score < EXCELLENT_THRESHOLD:
        return "Pass"
    return "Excellent"


main()
