# 01. Write a program that converts words present in a list into uppercase and stores them in a set.

def list_to_set():

    list = input("Enter the words separated by space : ").split()
    list = [str.upper() for str in list]

    print("List of words :",list)

    print("Set of words :",set(list))

list_to_set()
