# 06. Modify an element of a tuple.

def modify_tuple():
    input_string = input("Enter elements of the tuple separated by spaces: ")
    my_tuple = tuple(input_string.split())
    print("Original Tuple:", my_tuple)

    index_to_modify = int(input("Enter index no. to modify item : "))
    new_value = input("Enter new item : ")

    new_tuple = my_tuple[:index_to_modify - 1] + (new_value,) + my_tuple[index_to_modify:]

    print("Modified Tuple:", new_tuple)

modify_tuple()    