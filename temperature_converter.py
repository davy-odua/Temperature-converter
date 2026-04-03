# TEMPERATURE CONVERTER
# 1. Ask for temperature value
# 2. Ask for unit to convert from
# 3. Ask for unit to convert to
# 4. Display the result

units = ("C", "K", "F")
while True:
    try:
        value = float(input("Enter the temperature value: "))
        unit1 = input("Enter the unit to convert from: ").upper()
        unit2 = input("Enter the unit to convert to: ").upper()

        if unit1 not in units or unit2 not in units:
            print("Invalid unit, please enter C, K or F")

        elif unit1 == unit2:
            print(f"The temperature is already in {unit1}: {value}")
        # From Celsius to kelvin / Celsius to Fahrenheit
        elif unit1 == "C":
            if unit2 == "K":
                kelvin = value + 273.15
                print(f"The result is {kelvin:.2f} {unit2}")
            elif unit2 == "F":
                fahrenheit = (value * 9 / 5) + 32
                print(f"The result is {fahrenheit:.2f} {unit2}")
        # From Kelvin to Celsius / Kelvin to Fahrenheit
        elif unit1 == "K":
            if unit2 == "C":
                celsius = value - 273.15
                print(f"The result is {celsius:.2f} {unit2}")
            elif unit2 == "F":
                fahrenheit = (value - 273.15) * 9 / 5 + 32
                print(f"The result is {fahrenheit:.2f} {unit2}")
        # From Fahrenheit to kelvin / Fahrenheit to Celsius
        elif unit1 == "F":
            if unit2 == "K":
                kelvin = (value - 32) * 5 / 9 + 273.15
                print(f"The result is {kelvin:.2f} {unit2}")
            elif unit2 == "C":
                celsius = (value - 32) * 5 / 9
                print(f"The result is {celsius:.2f} {unit2}")
    except ValueError:
        print("Invalid input, try again")

    cont = input("Do you want to continue (y/n): ").lower()
    if cont == "n":
        print("Goodbye")
        break
#HELLO
#HELLO