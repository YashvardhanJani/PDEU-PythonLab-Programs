# 01. Write a program to create three dictionaries and concatenate them to create fourth dictionary.

def create_dict():
    user_dict = {}
    num_entries = int(input("How many key-value pairs do you want to enter? "))

    for i in range(num_entries):
        key = input(f"Enter key {i + 1}: ")
        value = input(f"Enter value for {key}: ")
        user_dict[key] = value

    return user_dict    

print("Create dict1:-")
dict1 = create_dict() 
print("\nCreate dict2:-")    
dict2 = create_dict()
print("\nCreate dict3:-")
dict3 = create_dict()

print("The Dictionary 01 :",dict1)
print("The Dictionary 02 :",dict2)
print("The Dictionary 03 :",dict3)

dict4 = {**dict1, **dict2, **dict3}
print("The Dictionary 04 :",dict4)