# 02. Print largest and smallest values out of three.

def largeAndSmallNum():
    a = float(input("Enter the first number : "))
    b = float(input("Enter the second number : "))
    c = float(input("Enter the third number : "))

    if(a>b and a>c):
        print("Largest Number :",a)
        if(b>c):
            print("Smallest Number :",c)
        else:
            print("Smallest Number :",b)

    elif(b>c and b>a):
        print("Largest Number :",b)
        if(a>c):
            print("Smallest Number :",c)
        else:
            print("Smallest Number :",a)  

    elif(c>a and c>b):
        print("Largest Number :",c)
        if(a>b):
            print("Smallest Number :",b)
        else:
            print("Smallest Number :",a)      

    else:
        print("Please, do not input idential numbers.")                   
    

largeAndSmallNum() 