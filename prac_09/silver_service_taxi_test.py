from prac_09.silver_service_taxi import SilverServiceTaxi

red_taxi = SilverServiceTaxi('Red', 100, 3)
print(red_taxi)

red_taxi.drive(50)
print(red_taxi)
print(f"Current fare: ${red_taxi.get_fare():.2f}")

red_taxi.start_fare()
print(red_taxi)
print(f"Current fare: ${red_taxi.get_fare():.2f}")

red_taxi.drive(12)
print(red_taxi)
print(f"Current fare: ${red_taxi.get_fare():.2f}")

print(f"Remained fuel: {red_taxi.fuel}")
