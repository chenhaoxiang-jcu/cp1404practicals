NAME_FILE = 'name.txt'
NUMBER_FILE = 'numbers.txt'

name_writing = input("Enter your name: ")
out_file = open(NAME_FILE, "w")
out_file.write(name_writing)
out_file.close()

in_file = open(NAME_FILE, "r")
name_reading = in_file.read()
in_file.close()
print(f"Hi {name_reading}!")

with open(NUMBER_FILE, "r") as in_numeric_file:
    first_line = int(in_numeric_file.readline())
    second_line = int(in_numeric_file.readline())
    print(first_line + second_line)

with open(NUMBER_FILE, "r") as in_numeric_file:
    total = 0
    for line in in_numeric_file:
        total += int(line)
    print(total)
