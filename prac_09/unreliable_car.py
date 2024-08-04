"""Car class"""

from random import uniform

from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""
    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar object, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()}, have {self.reliability}% chance to drive the car."

    def drive(self, distance):
        """Drive like parent Car but only when a random number is less than reliability."""
        distance_driven = 0
        if uniform(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
        return distance_driven
