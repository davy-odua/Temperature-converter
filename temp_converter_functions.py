
# TEMPERATURE CONVERTER
# 1. Ask for temperature value
# 2. Ask for unit to convert from
# 3. Ask for unit to convert to
# 4. Display the result

units = ("C", "K", "F")
def user_input():
    value = float(input("Enter the temperature value: "))
    unit1 = input("Enter the unit to convert from: ").upper()
    unit2 = input("Enter the unit to convert to: ").upper()
    return value, unit1, unit2

def check_for_valid_inputs(unit1, unit2):
    if unit1 not in units or unit2 not in units:
        print("Invalid input, Please enter C, K , F!")
        return False
    return True

def similar_inputs(unit1, unit2, value):
    if unit1 == unit2:
        print(f"The unit is already in {unit1}: {value} ")
        return True
    return False

def celsius_to_fahrenheit(value):
    return (value * 9 / 5) + 32

def celsius_to_kelvin(value):
    return  value + 273.15

def fahrenheit_to_celsius(value):
    return (value - 32) * 5 / 9

def fahrenheit_to_kelvin(value):
    return (value - 32) * 5 / 9 + 273.15

def kelvin_to_celsius(value):
    return value - 273.15

def kelvin_to_fahrenheit(value):
    return (value - 273.15) * 9 / 5 + 32

def main():
    while True:
        try:
            # Defining user inputs
            value, unit1, unit2 = user_input()

            # checking for invalid inputs
            check_for_valid_inputs(unit1, unit2)
            if not check_for_valid_inputs(unit1, unit2):
                continue
            #Similar inputs
            similar_inputs(unit1, unit2, value)
            if similar_inputs(unit1, unit2, value):
                continue

            # Celsius to Fahrenheit / celsius to Kelvin
            if unit1 == "C" and unit2 == "F":
                result = celsius_to_fahrenheit(value)

            elif unit1 == "C" and unit2 == "K":
                result = celsius_to_kelvin(value)

            # Kelvin to Celsius / Kelvin to Fahrenheit
            elif unit1 == "K" and unit2 == "C":
                result = kelvin_to_celsius(value)

            kelvin_to_fahrenheit(value)
            if unit1 == "K" and unit2 == "F":
                result = kelvin_to_fahrenheit(value)

            # Fahrenheit to Celsius / Fahrenheit to Kelvin
            if unit1 == "F" and unit2 == "C":
                result = fahrenheit_to_celsius(value)

            fahrenheit_to_kelvin(value)
            if unit1 == "F" and unit2 == "K":
                result = fahrenheit_to_kelvin(value)


            print(f"The result is {result}{unit2}")


        except ValueError:
            print("Invalid input, Try again!")
        # Ask the user whether to continue with the convertion or not
        continuation = input("Do you want to continue (y/n): ").lower()
        if continuation == "n":
            print("Goodbye")
            break

main()
#HELLO