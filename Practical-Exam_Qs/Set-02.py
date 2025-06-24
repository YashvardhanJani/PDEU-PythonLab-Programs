"""Create a text file having following data in any order in multiple lines: any data type/any variable name/any number (int or float)
write a python program to read one line at a time, identify the word and generate the output keyword, identifier or number respectively."""

import keyword
import builtins

# Get all built-in names (like float, list, boolean etc.)
builtin_names = dir(builtins)

def classify(word):
    if word in keyword.kwlist or word in builtin_names:
        return "Keyword"
    try:
        float(word)  # checks for int or float
        return "Number"
    except ValueError:
        return "Identifier"

# Read the file and classify each line
filename = "Practical-Exam_Qs/input.txt" 
with open(filename, 'r') as file:
    for line in file:
        word = line.strip()
        if word:
            print(f"{word} -> {classify(word)}")


print(builtin_names)