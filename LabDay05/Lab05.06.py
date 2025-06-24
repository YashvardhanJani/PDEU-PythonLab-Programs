# 06. Convert list of temperatures in Fahrenheit degrees to equivalent Celsius degrees.

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


fahrenheit_temps = list(map(float, input("Enter a list of temperatures in Fahrenheit (separated by spaces): ").split()))

celsius_temps = [round(fahrenheit_to_celsius(temp), 2) for temp in fahrenheit_temps]

print("Temperatures in Celsius:", celsius_temps)