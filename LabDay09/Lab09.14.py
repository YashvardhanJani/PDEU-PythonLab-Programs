# 14. A string is entered through the keyboard. Write a recursive function that counts the number of vowels in this string.

def count_vowels(s, index=0):
    vowels = "aeiouAEIOU"
    if index == len(s):
        return 0
    return (1 if s[index] in vowels else 0) + count_vowels(s, index + 1)

user_input = input("Enter a string: ")
print(f"Number of vowels in the string: {count_vowels(user_input)}")
