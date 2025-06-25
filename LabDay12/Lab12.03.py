# 03. Write a program to create a class that can calculate the surface area and volume of a solid. The class should also have a provision to accept the data relevant to the solid.

import math

class Solid:
    def __init__(self):
        pass

    def input_data(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def surface_area(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def volume(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Cube(Solid):
    def input_data(self):
        self.side = float(input("\nEnter the side length of the cube: "))

    def surface_area(self):
        return 6 * self.side ** 2

    def volume(self):
        return self.side ** 3

class Sphere(Solid):
    def input_data(self):
        self.radius = float(input("\nEnter the radius of the sphere: "))

    def surface_area(self):
        return 4 * math.pi * self.radius ** 2

    def volume(self):
        return (4/3) * math.pi * self.radius ** 3

class Cylinder(Solid):
    def input_data(self):
        self.radius = float(input("\nEnter the radius of the cylinder: "))
        self.height = float(input("Enter the height of the cylinder: "))

    def surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def volume(self):
        return math.pi * self.radius ** 2 * self.height


# Main function
def main():
    print("Choose a solid to work with:")
    print("1. Cube")
    print("2. Sphere")
    print("3. Cylinder")

    choice = input("Enter your choice (1/2/3): ")

    solids = {'1': Cube, '2': Sphere, '3': Cylinder}

    solid_class = solids.get(choice)
    if solid_class:
        solid = solid_class()
        solid.input_data()
        print("\nSurface Area:", round(solid.surface_area(), 2))
        print("Volume:", round(solid.volume(), 2))
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()