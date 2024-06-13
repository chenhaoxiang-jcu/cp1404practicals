import random

MIN_NUMBER = 1
MAX_NUMBER = 45
COLUMN = 6

number_of_picks = int(input("How many quick picks? "))
for i in range(number_of_picks):
    quick_picks = []
    for j in range(COLUMN):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        while number in quick_picks:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
        quick_picks.append(number)
    quick_picks.sort()
    [print(f'{number:2}', end=' ') for number in quick_picks]
    print()
