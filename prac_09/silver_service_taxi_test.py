from prac_09.silver_service_taxi import SilverServiceTaxi

red_taxi = SilverServiceTaxi('Red', 100, 3)
print(red_taxi)

red_taxi.drive(50)
print(red_taxi)
print(red_taxi.get_fare())

red_taxi.start_fare()
print(red_taxi)
print(red_taxi.get_fare())

red_taxi.drive(30)
print(red_taxi)
print(red_taxi.get_fare())

print(red_taxi.fuel)  # remained fuel should be 20
