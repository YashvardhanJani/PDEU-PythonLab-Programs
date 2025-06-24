# 04. Check whether a given number is divisible by 10 or not

def oddOReven():
    a = float(input("Enter an Integer : "))

    if(a%10==0):
        print(a,"is divisible by 10.")
    else:
        print(a,"is not divisible by 10.")

oddOReven()  