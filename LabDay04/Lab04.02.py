# 02. Print a multiplication table of a given number.

def multiplication_table(n):
    for i in range(1,11):
        print(n,"x",i,"=",n*i)

n = int(input("Enter an integer : "))
print("Multiplication Table of ",n,"\n") 

multiplication_table(n)