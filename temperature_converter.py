# TEMPERATURE CONVERTER
# 1. Ask for temperature value
# 2. Ask for unit to convert from
# 3. Ask for unit to convert to
# 4. Display the result

units = ("C", "K", "F")
while True:
    value = float(input("Enter the temperature value: "))
    try:
        unit1 = input("Enter the unit to convert from: ").upper()
        unit2 = input("Enter the unit to convert to: ").upper()
        # From Celsius to kelvin / Celsius to Fahrenheit
        if unit1 == "C":
            if unit2 == "K":
                kelvin = value + 273.15
                print(kelvin)
            elif unit2 == "F":
                Fahrenheit = (value * 9 / 5) + 32
                print(Fahrenheit)

        elif unit1 == "K":
            if unit2 == "C":
                Celsius = value - 273.15
                print(Celsius)
            elif unit2 == "F":
                Fahrenheit = (value - 273.15) * 9 / 5 + 32
                print(Fahrenheit)

        elif unit1 == "F":
            if unit2 == "K":
                kelvin = (value - 32) * 5 / 9 + 273.15
                print(kelvin)
            elif unit2 == "C":
                Celsius = (value - 32) * 5 / 9
                print(Celsius)
    except ValueError:
        print("Invalid input, try again")













