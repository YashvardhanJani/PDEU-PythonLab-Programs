# 01. Print largest and smallest values out of two.

def largeAndSmallNum():
    a = float(input("Enter the first number : "))
    b = float(input("Enter the second number : "))

    if (a>b):
        print("Largest Number :",a)
        print("Smallest Number :",b)
    else:
        print("Largest Number :",b)
        print("Smallest Number :",a)


largeAndSmallNum()        