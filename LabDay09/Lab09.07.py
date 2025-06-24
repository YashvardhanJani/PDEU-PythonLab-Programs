# 07. A palindrome is a word or phrase that reads the same in both directions. Write a program that defines a function ispalindrome() which checks whether a given string is a palindrome or not. Ignore spaces and case mismatch while checking for palindrome.

def ispalindrome(s):
    cleaned_s = ''.join(s.lower().split())
    return cleaned_s == cleaned_s[::-1]

print("Examples :-")
test_strings = [
    "Racecar",
    "A man a plan a canal Panama",
    "Hello World"
]

for string in test_strings:
    print(f'"{string}" is a palindrome: {ispalindrome(string)}')

str = input("\nEnter the string : ")
print(f'"{str}" is a palindrome: {ispalindrome(str)}')