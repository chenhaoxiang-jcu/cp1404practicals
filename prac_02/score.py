def main():
    """Ask the user for their score and print the result."""
    score = float(input("Enter score: "))
    message = determine_message(score)
    print(message)


def determine_message(score):
    """Determine the appropriate message based on the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    if score < 50:
        return "Bad"
    if score < 90:
        return "Pass"
    return "Excellent"


main()
