# 22. Calculate net sales where net sales = gross sales – 10% discount of gross sales.

def netSales():
    g = float(input("Enter the value of Gross Sales : "))
    n = g - (0.1*g)

    print("Net Sales :",n)

netSales()    