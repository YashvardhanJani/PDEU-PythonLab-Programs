# 05. Pangram is a sentence that uses every letter of the alphabet. Write a program to check whether a given string is pangram or not, through a user-defined function ispangram(). Test the function with “The quick brown fox jumps over the lazy dog” or “Crazy Fredrick bought many very exquisite opal jewels”. Hint: use set() to convert the string into a set of characters present in the string and use <= to check whether alphaset is a subset of the given string.

import string

def ispangram(s):
    alphabet_set = set(string.ascii_lowercase)
    return alphabet_set <= set(s.lower())

test_sentences = [
    "The quick brown fox jumps over the lazy dog",
    "Crazy Fredrick bought many very exquisite opal jewels"
]

for sentence in test_sentences:
    print(f'"{sentence}" is a pangram: {ispangram(sentence)}')

str = input("\nEnter the string : ")
print(f'"{str}" is a pangram: {ispangram(str)}')