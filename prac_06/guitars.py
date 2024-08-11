"""
Guitars
Current time: 21:02
Estimate: 30 minutes
Actual:   39 minutes
"""

from prac_06.guitar import Guitar
from operator import attrgetter

print("My guitars!")

guitars = []
guitar_name = input("Name: ")
while guitar_name != '':
    guitar_year = int(input("Year: "))
    guitar_cost = float(input("Cost: $"))
    guitar = Guitar(guitar_name, guitar_year, guitar_cost)
    guitars.append(guitar)
    print(f"{guitar} added.")
    print()
    guitar_name = input("Name: ")

print("These are my guitars:")

name_width = max(len(guitar.name) for guitar in guitars)
cost_width = max(len(f'{guitar.cost:,.2f}') for guitar in guitars)

guitars.sort(key=attrgetter('year'))
for i, guitar in enumerate(guitars, 1):
    vintage_string = '(vintage)' if guitar.is_vintage() else ''
    print(f"Guitar {i}: {guitar.name:>{name_width}} ({guitar.year}), "
          f"worth ${guitar.cost:{cost_width},.2f} {vintage_string}")
