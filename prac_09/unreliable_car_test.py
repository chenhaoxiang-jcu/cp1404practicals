from prac_09.unreliable_car import UnreliableCar

black_car = UnreliableCar('Black', 100, 80)
white_car = UnreliableCar('White', 100, 20)

print(black_car)
print(white_car)

print(black_car.drive(90))
print(white_car.drive(90))

print(black_car)
print(white_car)
