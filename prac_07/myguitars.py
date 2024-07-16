from prac_07.guitar import Guitar

FILENAME = 'guitars.csv'


def main():
    guitars = load_guitars(FILENAME)
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def load_guitars(filename):
    guitars = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            part = line.strip().split(',')
            guitar = Guitar(part[0], part[1], float(part[2]))
            guitars.append(guitar)
    return guitars


main()
