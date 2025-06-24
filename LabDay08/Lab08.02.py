# 02. Write a program to create a set containing 10 random numbers in the range 15 to 45. Count how many of these numbers are less than 30. Delete all numbers that are greater than 35.

import random

def set_operations():
    random_num = {random.randint(15,45) for _ in range(10)}
    print("Set of 10 random numbers in the range 15 to 45 =",random_num)

    count_lessthan_30 = sum(1 for num in random_num if num < 30)
    print("Count of numbers which are less than 30 =",count_lessthan_30)

    random_num = {num for num in random_num if num <= 35} # to delete num > 35
    print("Set after deletion of numbers greter than 35 =",random_num)
    
set_operations()    