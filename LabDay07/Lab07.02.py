# 02. Write a program to check whether a dictionary is empty or not.

def check_empty_dict(dictname,dict):

    if not dict:
        print(f"{dictname} is Empty.")
    else:
        print(f"{dictname} is not Empty.")   


dict1 = {"01":"Yashvardhan", "02":"Jani"} 
check_empty_dict("dict1",dict1)
dict2 = {}
check_empty_dict("dict2",dict2)
