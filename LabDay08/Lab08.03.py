# 03. Create an empty set. Write a program that adds five new names to this set, modifies one existing name and deletes two names from it.

names_set = set()

def add_name():
    for i in range(5):
        name = input(f"Enter name {i+1}: ")
        names_set.add(name)
    print("\nSet of names:", names_set)

def modify_name():
    old_name = input("Enter the name you want to modify: ")
    if old_name in names_set:
        new_name = input("Enter the new name: ")
        names_set.remove(old_name)
        names_set.add(new_name)
    else:
        print("Name not found in the set.")
        modify_name()

def delete_name(m,n):
    for i in range(m,n):
        del_name = input(f"Enter name {i+1} to delete: ")
        if del_name in names_set:
            names_set.remove(del_name)
        else:
            print("Name not found in the set.")
            if (i==0):
                delete_name(0,1)
            else:   
                delete_name(1,2) 


print("-------Add five names from user input-------")
add_name()
print("\n-------Modify one existing name-------")
modify_name()
print("\nSet after modification:", names_set)
print("\n-------Delete two names from user input-------")
delete_name(0,2)    
print("\nFinal set of names:", names_set)  