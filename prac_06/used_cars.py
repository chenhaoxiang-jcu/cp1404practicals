"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    limo = Car(100)
    limo.add_fuel(20)
    print(limo.fuel)
    limo.drive(115)

    harry_car = Car('Nimbus-2000', 2000)
    print(harry_car)
    harry_car.add_fuel(1000)
    harry_car.drive(2000)
    print(harry_car)


main()
