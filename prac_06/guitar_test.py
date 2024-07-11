from prac_06.guitar import Guitar

gibson_guitar = Guitar('Gibson L-5 CES', 1922, 16035.4)
another_guitar = Guitar('Another Guitar', 2013)

print(f"{gibson_guitar.name} get_age() - Expected {2024 - 1922}. Got {gibson_guitar.get_age()}")
print(f"{another_guitar.name} get_age() - Expected {2024 - 2013}. Got {another_guitar.get_age()}")
print(f"{gibson_guitar.name} is_vintage() - Expected {2024 - 1922 >= 50}. Got {gibson_guitar.is_vintage()}")
print(f"{another_guitar.name} is_vintage() - Expected {2024 - 2013 >= 50}. Got {another_guitar.is_vintage()}")
print()

old_guitar = Guitar('50-year old guitar', 1974)
print(f"{old_guitar.name} is_vintage() - Expected {2024 - 1974 >= 50}. Got {old_guitar.is_vintage()}")
