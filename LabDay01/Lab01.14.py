#14. Convert celcius into Fahrenheit. F = (9/5 * C) + 32

def cTof():
    a = float(input("Enter the value of Temp. in Celcius : "))
    b = (9/5 * a) + 32

    print(a,"°C =",b,"F")

cTof()    