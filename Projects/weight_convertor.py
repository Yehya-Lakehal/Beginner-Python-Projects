# Simple Weight Convertor

print("Welcome to my app ( Simple Weight Convertor ) !")

weight = float(input("Enter your weight: "))
unit = input("kilograms(kg) or Pounds(Lb)? ")

if unit.lower() == "kg":
    result = weight * 2.205
    print(f"Result: {round(result, 2)} pounds.")
elif unit.lower() == "kg":
    result = weight / 2.205
    print(f"Result: {round(result, 2)} kilograms.")
else:
    print("Error: Invalid Input!")