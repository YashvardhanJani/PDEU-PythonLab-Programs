#15. Convert Fahrenheit into celcius. C = 5/9 * (F – 32)

def fToc():
    a = float(input("Enter the value of Temp. in Fahrenheit : "))
    b = 5/9 * (a - 32)

    print(a,"F =",b,"°C")

fToc()    