# 08. Print factorial of a given number.

def factorial(n):
    if n == 0:
        return 1
    else :
        return n*factorial(n-1)
    
n = int(input("Enter the number : "))
print(f"Factorial of {n} is",factorial(n))    