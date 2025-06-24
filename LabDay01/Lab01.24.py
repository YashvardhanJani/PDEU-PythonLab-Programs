# 24. Swap two values.

def swapNum():
    a = float(input("Enter the first number : "))
    b = float(input("Enter the sencond number : "))

    print("Before :",a,b)
    a,b = b,a
    print("Now :",a,b)

swapNum()    