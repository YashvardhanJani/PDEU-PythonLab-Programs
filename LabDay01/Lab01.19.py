# 19. Calculate area of a circle. A = pi * R * R

import math

def areaOfCircle():
    r = float(input("Enter the value of radius of Circle : "))

    print("Area of Circle is :",(math.pi)*r**2,"unit²")

areaOfCircle()