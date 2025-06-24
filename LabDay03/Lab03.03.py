# 03. Accept two strings. Check whether one string is there in another string.

def check_string():
    str1 = input("Enter the first string : ")
    str2 = input("Enter the second string : ")

    if str1 in str2 :
        print(f"{str1} is present in {str2}")
    elif str2 in str1 :
        print(f"{str2} is present in {str1}")    
    else:
        print("one string is not there in another string.")

check_string()