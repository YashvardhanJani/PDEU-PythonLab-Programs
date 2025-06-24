# 10. Given the length and breadth of a rectangle, write a program to find whether the area of the rectangle is greater than its perimeter.

def perimeterGreaterthanArea():
    l, b = map(float, input("Enter the length & breadth of Rectangle separated by spaces : ").split())
    
    area = (l*b)
    perimeter = (2*(l+b))

    if(area>perimeter):
        print("Area of Rectangle is greater than its Perimeter.")
    elif(perimeter>area):
        print("Perimeter of Rectangle is greater than its Area.")
    else:
        print("Area & Perimeter are same for this Rectangle.")       


perimeterGreaterthanArea()        