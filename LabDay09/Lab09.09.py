# 09. Write a program that defines a function count_alpha_digits() that accepts a string and calculates the number of alphabets and digits in it. It should return these values as a dictionary.

def count_alpha_digits(str):
    count_alpha = 0
    count_digit = 0

    for element in str:
        if(65<=ord(element)<=90 or 97<=ord(element)<=122):
            count_alpha+=1

    for element in str:
        if(48<=ord(element)<=57):
            count_digit+=1
            
    print({"No. of alphabets in the string is" : count_alpha, "No. of digits in the string is" : count_digit})

str = input("Enter the string : ")
count_alpha_digits(str)
