# Simple Temprature Convertor

print("Welcome to my app ( Simple Temprature Convertor ) !")

temp = float(input("Enter temprature: "))
unit = input("Celsius(C) or Fahrenheit(F) or Kelvin(K)? ").lower()
output_unit = input("Convert to: Celsius(C) or Fahrenheit(F) or Kelvin(K)? ").lower()
result = 0

def convert():
    if unit == output_unit:
        return "Error: you entered the same unit!"
    elif unit == "c":
        if output_unit == "k":
            return temp + 273.15
        else:
            return temp * (9/5) + 32
    elif unit == "k":
        if output_unit == "c":
            return temp - 273.15
        else:
            return (temp - 273.15) * (9 / 5) + 32
    elif unit == "f":
        if output_unit == "c":
            return (temp - 32) * (5 / 9)
        else:
            return (temp - 32) * (5 / 9) + 273.15
    else:
        return "Error: Invalid Input!"



if type(convert()) is float:
    print(f"Result: {round(convert(), 2)} {output_unit}.")
else:
    print(convert())