# 01. Write a program that defines a function count_lower_upper() that accepts a string and calculates the number of uppercase and lowercase alphabets in it. It should return these values as a dictionary. Call this function for some sample string.

def count_lower_upper(str):
    count_upper = 0
    count_lower = 0
    for char in str:
        if("A" <= char <= "Z"):
            count_upper += 1
        else:
            count_lower += 1    
    return {'No. of uppercase alphabets': count_upper ,'No. of lowercase alphabets': count_lower}

str = input("Enter the string which only contains alphabets : ")
print(count_lower_upper(str))