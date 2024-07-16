from prac_07.guitar import Guitar

FILENAME = 'guitars.csv'


def main():
    """Load existing guitars and get new guitars, display all guitars in order, then save to file."""
    guitars = load_guitars(FILENAME)
    new_guitars = get_guitars()
    guitars += new_guitars
    guitars.sort()
    print()
    print("Guitars:")
    for guitar in guitars:
        print(guitar)
    save_guitars(FILENAME, guitars)


def load_guitars(filename):
    """Load existing guitars' information from file."""
    guitars = []
    with open(filename, 'r', newline='') as in_file:
        for line in in_file:
            part = line.strip().split(',')
            guitar = Guitar(part[0], int(part[1]), float(part[2]))
            guitars.append(guitar)
    return guitars


def get_guitars():
    """Get guitar objects by user input and store them in a list."""
    guitars = []
    guitar_name = input("Name: ")
    while guitar_name != '':
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))
        guitar = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        guitar_name = input("Name: ")
    return guitars


def save_guitars(filename, guitars):
    """Save guitars to file."""
    with open(filename, 'w', newline='') as out_file:
        for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


main()
