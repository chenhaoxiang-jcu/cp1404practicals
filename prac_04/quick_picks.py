import random

NUMBER_POOL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
               26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
COLUMN = 6

number_of_picks = int(input("How many quick picks? "))
for i in range(number_of_picks):
    random_numbers = []
    for j in range(COLUMN):
        number = random.choice(NUMBER_POOL)
        while number in random_numbers:
            number = random.choice(NUMBER_POOL)
        random_numbers.append(number)
    random_numbers.sort()
    [print(f'{number:2}', end=' ') for number in random_numbers]
    print()
