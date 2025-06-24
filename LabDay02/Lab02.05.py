# 05. Accept age of a person. If age is less than 18, print minor otherwise Major.

def checkAge():
    a = float(input("Enter your current age : "))

    if(a>=18):
        print("You are Major.")
    else:
        print("You are Minor.")    


checkAge()