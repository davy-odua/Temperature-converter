
units = ("C", "K", "F")

def user_input():
    pass

while True:
    try:
        #Defining user inputs
        value = float(input("Enter the temperature value: "))
        unit1 = input("Enter the unit to convert from: ").upper()
        unit2 = input("Enter the unit to convert to: ").upper()

        #checking for invalid inputs
        if unit1 not in units or unit2 not in units:
            print("Invalid input, Please enter C, K , F!")

        elif unit1 == unit2:
            print(f"The unit is already in {unit1}: {value} ")
        # Celsius to kelvin / celsius to Fahrenheit
        elif unit1 == "C":
            if unit2 == "K":
                kelvin = value + 273.15
                print(f"The result is {kelvin:.2f}{unit2} ")
            elif unit2 == "F":
                fahrenheit = (value * 9 / 5) + 32
                print(f"The result is {fahrenheit:.2f}{unit2} ")
        # Kelvin to Celsius / Kelvin to Fahrenheit
        elif unit1 == "K":
            if unit2 == "C":
                celsius = value - 273.15
                print(f"The result is {celsius:.2f}{unit2}")
            elif unit2 == "F":
                fahrenheit = (value - 273.15) * 9 / 5 + 32
                print(f"The result is {fahrenheit:.2f}{unit2} ")
        # Fahrenheit to Celsius / Fahrenheit to Kelvin
        elif unit1 == "F":
            if unit2 == "C":
                celsius = (value - 32) * 5 / 9
                print(f"The result is {celsius:.2f}{unit2}")
            elif unit2 == "K":
                kelvin = (value - 32) * 5 / 9 + 273.15
                print(f"The result is {kelvin:.2f}{unit2} ")

    except ValueError:
        print("Invalid input, Try again!")
    #Ask the user whether to continue with the convertion or not
    continuation = input("Do you want to continue (y/n): ").lower()
    if continuation == "n":
        print("Goodbye")
        break


#The end