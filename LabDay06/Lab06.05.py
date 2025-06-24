# 05. Remove empty tuple(s) from the list of tuples.

def remove_empty_tuple():
    lst = [5, 7, (), 9, 5, ()]

    lst = [ele for ele in lst if ele != ()]

    print(lst)

remove_empty_tuple()   