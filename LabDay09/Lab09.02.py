# 02. Write a program that defines a function compute() that calculates the value of n + nn + nnn + nnnn, where n is digit received by the function. test the function for digits 4 to 7.

def compute(n):
    nn = int(str(n) * 2)
    nnn = int(str(n) * 3)
    nnnn = int(str(n) * 4)
    
    return n + nn + nnn + nnnn

for i in range(4, 8):
    print(f"compute({i}) = {compute(i)}")
