"""
CP1404/CP5632 - Practical
temperature conversion with functions used

"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """Covert temprature """
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = get_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: " + "\n"))
            celsius = get_celsius(fahrenheit)
            print("Results: {:.2f} C".format(celsius))

        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you.")


def get_fahrenheit(celsius):
    """Convert celsius to fahrenheit"""
    celsius * 9.0 / 5 + 32
    return celsius


def get_celsius(fahrenheit):
    """Convert fahrenheit to celsius"""
    return (5 / 9) * (fahrenheit - 32)


main()