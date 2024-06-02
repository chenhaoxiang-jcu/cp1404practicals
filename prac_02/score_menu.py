MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    """Menu_driven score determining program with options to print the result and stars."""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            message = determine_message(score)
            print(message)
        elif choice == "S":
            print('*' * score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


def get_valid_score():
    """Get valid score which is 0 to 100 inclusive"""
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Score: "))
    return score


def determine_message(score):
    """Determine the appropriate message based on the score."""
    if score < 50:
        return "Bad"
    if score < 90:
        return "Pass"
    return "Excellent"


main()
