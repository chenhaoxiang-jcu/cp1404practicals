from prac_09.taxi import Taxi

# Create a new taxi object, my_taxi, with name "Prius 1", 100 units of fuel and price of $1.23
my_taxi = Taxi('Prius 1', 100, 1.23)
# Drive the taxi 40 km
my_taxi.drive(40)
# Print the taxi's details and the current fare
print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare()}")
# Restart the meter (start a new fare) and then drive the car 100 km
my_taxi.start_fare()
my_taxi.add_fuel(100)  # current fuel isn't enough
my_taxi.drive(100)
# Print the details and the current fare
print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare()}")
