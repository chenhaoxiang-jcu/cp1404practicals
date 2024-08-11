from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = 'q)uit, c)hoose taxi, d)rive'


def main():
    """Menu-driven taxi simulator with options to choose and drive taxi."""
    current_taxi = None
    bill = 0
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    print(MENU)

    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'c':
            current_taxi = choose_taxi(taxis, current_taxi, bill)
        elif choice == 'd':
            bill = drive_taxi(current_taxi, bill)
        else:
            print("Invalid option")
            print(f"Bill to date: ${bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display the taxi list with indices."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis, current_taxi, bill):
    """Prompt the user to choose a taxi and display the bill."""
    display_taxis(taxis)

    choice = int(input("Choose taxi: "))
    if choice in range(len(taxis)):
        current_taxi = taxis[choice]
    else:
        print("Invalid taxi choice")

    print(f"Bill to date: ${bill:.2f}")
    return current_taxi


def drive_taxi(current_taxi, bill):
    """Drive the taxi if user had already chosen a taxi, show the trip cost and add it to the bill."""
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
    else:
        current_taxi.start_fare()
        distance = float(input("Drive how far? "))
        current_taxi.drive(distance)
        trip_cost = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
        bill += trip_cost

    print(f"Bill to date: ${bill:.2f}")
    return bill


main()
