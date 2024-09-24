# 1. Ask the user to input the temperature
temperature = float(input("Input the temperature: "))

# 2. Display the conversion types
print("\nConversions:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

# 3. Ask the user to select the conversion types
conversion_type = input("\nSelect the number for conversion type: ")

# 4. Create the conditions
if conversion_type == "1":
    result = (temperature * 9 / 5) + 32  # formula to convert °C to °F
    print(f"\nThe conversion of {temperature}°C to Fahrenheit is: {round(result, 2)}°F")
elif conversion_type == "2":
    result = (temperature - 32) * 5 / 9  # formula to convert °F to °C
    print(f"\nThe conversion of {temperature}°F to Celsius is: {round(result, 2)}°C")
else:
    print("\n\033[91mInvalid character/number!\033[0m")  # show error message for invalid input