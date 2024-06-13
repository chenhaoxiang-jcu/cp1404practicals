"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print(data)
    display_information(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        data.append(parts)
    input_file.close()
    return data


def display_information(data):
    """Print subject details line by line."""
    max_name_length, max_number_length = determine_aligning_length(data)
    for part in data:
        print(f"{part[0]} is taught by {part[1]:{max_name_length}} and has {part[2]:{max_number_length}} students")


def determine_aligning_length(data):
    """Determine the length of the text alignment of name and number of student."""
    max_name_length = max([len(part[1]) for part in data])
    max_number_length = max([len(str(part[2])) for part in data])
    return max_name_length, max_number_length


main()
