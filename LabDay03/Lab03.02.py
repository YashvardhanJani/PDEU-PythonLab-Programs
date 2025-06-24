# 02. Write your own functions (without using built-in functions) to convert all characters of a string into lower case/upper case/toggle case.

def to_lowercase(string):
    result = ""

    for char in string:
        if("A" <= char <= "Z"):
            result += chr(ord(char)+32)
        else:
            result += char

    return result

def to_uppercase(string):
    result = ""

    for char in string:
        if("a" <= char <= "z"):
            result += chr(ord(char)-32)
        else :
            result += char

    return result

def to_togglecase(string):
    result = ""

    for char in string:
        if("A" <= char <= "Z"):
            result += chr(ord(char)+32)
        elif("a" <= char <= "z"):
            result += chr(ord(char)-32)
        else :
            result += char

    return result

string = input("Enter the string : ")

print("Lowercase :", to_lowercase(string))
print("Uppercase :", to_uppercase(string))
print("togglecase :", to_togglecase(string))