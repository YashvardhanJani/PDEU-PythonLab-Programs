# 01. Write a program that receives an integer an input. If a string is entered instead of an integer, then report an error and give another chance to user to enter an integer. Continue this process till correct input is supplied.

def intinput():  
    try:
        a = int(input("Enter an integer: "))
    except ValueError:
        print("Entered value isn't an integer!")
        intinput()
    else:
        print("Program exicution done..")

intinput()        