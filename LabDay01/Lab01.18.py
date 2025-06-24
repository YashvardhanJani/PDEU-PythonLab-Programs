# 18. Calculate area & perimeter of a rectangle. A = L*B, P = 2 (L+B)

def areaAndPerimeterOfRectangle():
    l = float(input("Enter the value of SideLength-1 of Rectangle : "))
    b = float(input("Enter the value of SideLength-2of Rectangle : "))

    print("Area of Rectangle is :",l*b,"unit²")
    print("Perimeter of Rectangle is :",(2*(l+b)),"unit")

areaAndPerimeterOfRectangle()