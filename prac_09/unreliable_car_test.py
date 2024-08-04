from prac_09.unreliable_car import UnreliableCar

black_car = UnreliableCar('Black', 100, 80)
white_car = UnreliableCar('White', 100, 20)
blue_car = UnreliableCar('Blue', 100, 100)
green_car = UnreliableCar('Green', 100, 0)

cars = [UnreliableCar('Car-100', 100, 100),
        UnreliableCar('Car-80', 100, 80),
        UnreliableCar('Car-50', 100, 50),
        UnreliableCar('Car-20', 100, 20),
        UnreliableCar('Car-00', 100, 0)]

for car in cars:
    print(car)
    print(car.drive(99))
    print(car)
    print()
