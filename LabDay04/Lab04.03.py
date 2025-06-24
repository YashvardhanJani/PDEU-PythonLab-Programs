# 03. Count no. of alphabets and no. of digits in any given string.

def count_alphabets(str):
    count = 0
    for element in str:
        if(65<=ord(element)<=90 or 97<=ord(element)<=122):
            count+=1
    return count

def count_digits(str):
    count = 0
    for element in str:
        if(48<=ord(element)<=57):
            count+=1
    return count

str = input("Enter the string : ")

print("No. of alphabets in the string is :",count_alphabets(str))
print("No. of digits in the string is :",count_digits(str))