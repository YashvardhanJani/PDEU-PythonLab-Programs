# 16. Calculate interest where I = PRN/100

def interest():
    p = float(input("Enter the Prize Rs. : "))
    r = float(input("Enter the Rate in % : "))
    n = float(input("Enter the Time-Duration in years : "))

    print("The Simple Interest is :",(p*r*n)/100)

interest()    