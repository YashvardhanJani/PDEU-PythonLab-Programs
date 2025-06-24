# 07. Accept a year value from the user. Check whether it is a leap year or not.

def checkLeapYear():

    year = int(input("Enter a year : "))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")


checkLeapYear()
