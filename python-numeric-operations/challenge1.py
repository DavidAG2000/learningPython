fahrenheit = input("What is the temperature in fahrenheit? ")

if fahrenheit.isnumeric():
    celsius = (int(fahrenheit) - 32) * 5/9
    print("Temperature in celsius is: " + str(int(celsius)))
else:
    print("Input is not a number")

# celsius = (fahrenheit - 32) * 5/9