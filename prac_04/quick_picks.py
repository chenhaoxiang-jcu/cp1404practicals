import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6


def main():
    """Print a number of lines randomly selected numbers in ascending order"""
    number_of_picks = int(input("How many quick picks? "))
    for i in range(number_of_picks):
        random_numbers = pick_numbers()
        [print(f'{number:2}', end=' ') for number in sorted(random_numbers)]
        print()


def pick_numbers():
    """Pick random numbers without repeated and store them in a list"""
    random_numbers = []
    for j in range(NUMBERS_PER_PICK):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        while number in random_numbers:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
        random_numbers.append(number)
    return random_numbers


main()
