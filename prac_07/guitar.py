CURRENT_YEAR = 2024
VINTAGE_YEAR = 50


class Guitar:
    """Represent information about a guitar."""
    def __init__(self, name='', year=0, cost=0.0):
        """Initialise the guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar."""
        return f'{self.name} ({self.year}) : ${self.cost:,.2f}'

    def __lt__(self, other):
        """Less than, using to sort guitars by year released."""
        return self.year < other.year

    def get_age(self):
        """Return how old the guitar is in years."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if the guitar is 50 or more years old."""
        return self.get_age() >= VINTAGE_YEAR
