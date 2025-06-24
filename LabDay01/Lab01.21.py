# 21. Calculate net salary where net salary = gross salary + allowance – deduction. Allowances are 10% while deductions are 3% of gross salary

def netSalary():
    g = float(input("Enter the value of Gross Salaray : "))
    n = g + (0.1*g) - (0.03*g)

    print("Net Salaray :",n)

netSalary()  