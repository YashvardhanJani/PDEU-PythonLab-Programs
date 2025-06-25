# 07. Create a class Weather that has a list containing weather parameters. Define an overloaded in operator that checks whether an item is present in the list. (Hint: define the function __contains__( )in a class.)

class Weather:
    def __init__(self, parameters):
        self.parameters = parameters

    def __contains__(self, item):
        return item.lower() in (param.lower() for param in self.parameters)

    def display(self):
        print("Weather Parameters:", ', '.join(self.parameters))


# Main Program
def main():
    # Create a weather object with a few parameters
    weather = Weather(["Temperature", "Humidity", "Pressure", "Wind Speed"])

    # User input to check a parameter
    search = input("\nEnter a weather parameter to check: ")

    if search in weather:
        print(f"{search} is recorded in the weather data.")
    else:
        print(f"{search} is NOT recorded in the weather data.")


if __name__ == "__main__":
    main()