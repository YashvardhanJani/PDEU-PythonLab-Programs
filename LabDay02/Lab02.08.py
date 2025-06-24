# 08. Check whether a triangle is valid or not, when the three angles of the triangle are entered through the keyboard. A triangle is valid if the sum of all the three angles is equal to 180 degrees.

def validTriangle():
    angle1, angle2, angle3 = map(int, input("Enter three angles of Triangle separated by spaces : ").split())

    if(angle1+angle2+angle3==180):
        print("Triangle is a Valid Triangle.")
    else:
        print("Triangle isn't a Valid Triangle.")


validTriangle()
