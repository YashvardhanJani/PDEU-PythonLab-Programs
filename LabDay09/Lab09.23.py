""" 23. Consider the following list:
lst = ['madam','Python',"malayalam",12321]
Write a program to print those strings which are palindromes. """

def check_palindrom():
    lst = ['madam','Python','malayalam',12321]
    lst = list(filter(lambda s: str(s) == str(s)[::-1], lst))
    print(lst)

check_palindrom()    