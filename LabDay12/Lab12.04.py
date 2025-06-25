# 04. Write a program to create a class that can calculate the perimeter/circumference and area of a regular shape. The class should also have a provision to accept the data relevant to the shape.

import math

class RegularShape:
    def __init__(self):
        pass

    def input_data(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def area(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Square(RegularShape):
    def input_data(self):
        self.side = float(input("\nEnter the side length of the square: "))

    def perimeter(self):
        return 4 * self.side

    def area(self):
        return self.side ** 2

class Circle(RegularShape):
    def input_data(self):
        self.radius = float(input("\nEnter the radius of the circle: "))

    def perimeter(self):  # Circumference
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

class EquilateralTriangle(RegularShape):
    def input_data(self):
        self.side = float(input("\nEnter the side length of the equilateral triangle: "))

    def perimeter(self):
        return 3 * self.side

    def area(self):
        return (math.sqrt(3) / 4) * self.side ** 2


# Main function
def main():
    print(f"""Choose a regular shape:
    1. Square
    2. Circle
    3. Equilateral Triangle""")

    choice = input("Enter your choice (1/2/3): ")
    shapes = {'1': Square, '2': Circle, '3': EquilateralTriangle}

    shape_class = shapes.get(choice)
    if shape_class:
        shape = shape_class()
        shape.input_data()
        print("\nPerimeter/Circumference:", round(shape.perimeter(), 2))
        print("Area:", round(shape.area(), 2))
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()