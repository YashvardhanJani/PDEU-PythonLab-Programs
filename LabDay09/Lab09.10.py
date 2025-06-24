# 10. Write a program that defines a function called frequency() which computes the frequency of words present in a string passed to it. The frequencies should be returned in sorted order of words in the string.

from collections import defaultdict
import string

def frequency(input_string):

    # Remove punctuation from the input string
    translator = str.maketrans('', '', string.punctuation)
    cleaned_string = input_string.translate(translator)
    # Split the cleaned string into words
    words = cleaned_string.split()

    word_freq = defaultdict(int)
    for word in words:
        word_freq[word] += 1
    sorted_words = sorted(word_freq.keys())
    sorted_freq = {word: word_freq[word] for word in sorted_words}
    return sorted_freq

input_string = input("Enter the string : ")
result = frequency(input_string)
print(result)