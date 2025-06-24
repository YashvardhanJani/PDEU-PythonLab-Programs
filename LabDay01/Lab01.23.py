# 23. Calculate average of three subjects along with their total.

def avgAndTotal_marks():
    a = float(input("Enter the marks of 1st Subject : "))
    b = float(input("Enter the marks of 2nd Subject : "))
    c = float(input("Enter the marks of 3rd Subject : "))

    print("\n")
    
    print("Average of Marks :",(a+b+c)/3)
    print("Total marks of all three subjects :",(a+b+c))

avgAndTotal_marks()    