# Develop a program that inputs a sentence as a string input, find the longest word from this sentence using reduce.

from functools import reduce

def find_longest_word(sentence):
    words = sentence.split()
    longest = reduce(lambda a, b: a if len(a) >= len(b) else b, words)
    return longest

sentence = input("Enter a sentence: ")

print("The longest word is:", find_longest_word(sentence))