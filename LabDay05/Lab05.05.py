# 05. A list contains 5 strings. Convert all these strings to uppercase.

def list_uppercase():
   
    list = input("Enter the strings separated by space : ").split()

    list = [str.upper() for str in list]
    
    print(f"List of all {len(list)} string in uppercase : {list}")

list_uppercase()