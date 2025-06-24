# 22. Generate the list of 10 different random numbers between -15 and 15. Create a new list by obtaining square of all numbers in a list.

import random

def square_of_random_nums():
    lst = [random.randrange(-15,16) for _ in range(10)]
    print(f"Original List of Numbers : {lst}")
    lst = list(map(lambda x : x*x, lst))
    print(f"List of square of Numbers : {lst}")

square_of_random_nums()    