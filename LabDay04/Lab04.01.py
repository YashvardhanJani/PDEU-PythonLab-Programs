# 01. Print all alphabets in upper case and in lower case.

def alphabets_uppercase():
    for ch in range(65, 91):  
        print(chr(ch), end=" ")

def alphabets_lowercase():
    for ch in range(97, 123):  
        print(chr(ch), end=" ")

print("Uppercase letters:")
alphabets_uppercase()

print("\n")

print("Lowercase letters:")
alphabets_lowercase()


