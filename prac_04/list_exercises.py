numbers = []
NUMBER_OF_NUMBERS = 5

for i in range(NUMBER_OF_NUMBERS):
    number = int(input("Number: "))
    numbers.append(number)

first_number = numbers[0]
last_number = numbers[-1]
smallest_number = min(numbers)
largest_number = max(numbers)
average = sum(numbers) / len(numbers)

print(f"The first number is {first_number}\n"
      f"The last number is {last_number}\n"
      f"The smallest number is {smallest_number}\n"
      f"The largest number is {largest_number}\n"
      f"The average of the numbers is {average}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
