"""
Programming Language
Current time: 17:39
Estimate: 20 minutes
Actual:   23 minutes
"""


class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object."""

    def __init__(self, name='', typing='', reflection=False, year=0):
        """Initialize a ProgrammingLanguage object."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string representation of the programming language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Check if the programming language is dynamically typed or not."""
        return self.typing == 'Dynamic'
