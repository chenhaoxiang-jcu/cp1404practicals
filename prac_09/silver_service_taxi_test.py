from prac_09.silver_service_taxi import SilverServiceTaxi

taxis = [SilverServiceTaxi('T-F1', 100, 1),
         SilverServiceTaxi('T-F2', 100, 2),
         SilverServiceTaxi('T-F3', 100, 3),
         SilverServiceTaxi('T-F9.9', 100, 9.9)]

for taxi in taxis:
    print(taxi)
    taxi.drive(50)
    print(taxi)
    print(f"Current fare: ${taxi.get_fare():.2f}")

    taxi.start_fare()
    print(taxi)
    print(f"Current fare: ${taxi.get_fare():.2f}")

    taxi.drive(12)
    print(taxi)
    print(f"Current fare: ${taxi.get_fare():.2f}")

    print(f"Remained fuel: {taxi.fuel}")
    print()
