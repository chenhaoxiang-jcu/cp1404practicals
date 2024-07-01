"""
Wimbledon
Estimate: 30 minutes
Actual:   36 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    """Read wimbledon file, process the data and display processed information."""
    data = extract_data()
    champion_to_count = count_champions(data)
    countries_string = collect_countries(data)
    print("Wimbledon Champions: ")
    for champion, count in champion_to_count.items():
        print(f"{champion} {count}")
    print()
    number_of_countries = len(countries_string.split())
    print(f"These {number_of_countries} countries have won Wimbledon: ")
    print(countries_string)


def extract_data():
    """Extract needed data from wimbledon.csv file."""
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        data = [record.split(',')[1:3] for record in in_file.readlines()]
    return data


def count_champions(data):
    """Count number of champions and store them in a dictionary."""
    champion_to_count = {}
    for record in data:
        champion_to_count[record[1]] = champion_to_count.get(record[1], 0) + 1
    return champion_to_count


def collect_countries(data):
    """Collect the countries of the champions in alphabetical order and store them in a string."""
    countries = sorted({record[0] for record in data})
    countries_string = ', '.join(countries)
    return countries_string


main()
