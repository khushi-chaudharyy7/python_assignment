#Celsius to fahrenheit

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 1.8) + 32
print(f"{celsius:.2f} degree Celsius is equal to {fahrenheit:.2f} degree Fahrenheit")


#Fahrenheit to celsius

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) / 1.8
print(f"{fahrenheit:.2f} degree Fahrenheit is equal to {celsius:.2f} degree Celsius")