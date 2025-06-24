# 16. Calculate a to the power where a and b received through the keyword using recursion.

def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

a = int(input("Enter the base (a): "))
b = int(input("Enter the exponent (b): "))

result = power(a=a, b=b)
print(f"{a}^{b} = {result}")
