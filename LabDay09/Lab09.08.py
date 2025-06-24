# 08. Write a program that defines a function convert() that receives a string containing a sequence of whitespace separated words and returns a string after removing all duplicate words and sorting them alphanumerically. Hint: use set(), list () , sorted(), join().

def convert(s):
    unique_sorted_words = sorted(set(s.split()))
    return ' '.join(unique_sorted_words)

test_string = "banana apple orange apple mango banana"
print(convert(test_string))

str = input("\nEnter the string : ")
print(convert(str))
