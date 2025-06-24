# 01. Count how many vowels are there in a string. Accept the string from the user.

def count_vowels():
    string = input("Enter the string : ")
    
    vowel_count = 0
    vowels = "aeiouAEIOU"

    for char in string:
        if char in vowels:
            vowel_count += 1

    print("No. of vowels present in the string is :",vowel_count)
    

count_vowels()