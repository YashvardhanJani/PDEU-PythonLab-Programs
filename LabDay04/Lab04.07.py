# 07. Print nCr and nPr.

def factorial(n):
    if n == 0:
        return 1
    else :
        return n*factorial(n-1)
    
def nCr(n,r):
    return factorial(n) // (factorial(r)*factorial(n-r))

def nPr(n,r):
    return factorial(n) // factorial(n-r)

n = int(input("Enter the value of n :"))
r = int(input("Enter the value of r :"))

if n < r:
    print("Error : n should be greater than or equal to r")
else:
    print("nCr = ",nCr(n,r))
    print("nPr = ",nPr(n,r))