# 11. Write a function create_list() that creates and returns a list which is an intersection of two lists passed to it.

def create_list():
    list1 = input("Enter the elements for list1 separated by space : ").split()
    list2 = input("Enter the elements for list2 separated by space : ").split()

    return list(set(list1) & set(list2))


print("Intersection of Two Lists :-",create_list())  
