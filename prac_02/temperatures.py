MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """Menu-driven temperature convertor with options to convert Celsius to Fahrenheit or vice versa."""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = calculate_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = calculate_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def calculate_celsius(fahrenheit):
    """Converts Celsius based on Fahrenheit"""
    return 5 / 9 * (fahrenheit - 32)


def calculate_fahrenheit(celsius):
    """Calculate Fahrenheit based on Celsius."""
    return celsius * 9 / 5 + 32


main()
