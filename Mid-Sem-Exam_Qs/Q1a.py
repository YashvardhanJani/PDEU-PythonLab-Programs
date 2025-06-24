# 01.(a) Write a python program to remove duplicate values from the list.

def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

original_list = input("Enter the list elements separated by space : ").split()
print("Original List:", original_list)
print("List without duplicates:", remove_duplicates(original_list))


"""   BY USING set() :-

original_list = input("Enter the list elements separated by space : ").split()
print("Original List:", original_list)
print("List without duplicates:", list(set(original_list)))

"""
