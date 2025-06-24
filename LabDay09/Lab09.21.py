# 21. Suppose there are two lists, one containing numbers from 1 to 6, and other containing numbers from 6 to 1. Write a program to obtain a list that contains elements obtained by adding corresponding elements of the two lists. (hint: use map and lambda functions)

def add_elements_of_lists():
    lst1 = [1,2,3,4,5,6]
    lst2 = [6,5,4,3,2,1]

    lst = list(map(lambda i, j : i + j, lst1, lst2))
    print(lst)

add_elements_of_lists()    