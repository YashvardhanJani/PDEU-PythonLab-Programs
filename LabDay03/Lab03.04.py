# 04. Write a function that removes one string from another string, if present. E.g. Onestring = “abcdef”, removestring = “cd”. The finalstring should contain “abef”.

def remove_substring(onestring, removestring):
    result = ""
    
    i = 0
    while i < len(onestring):
        if onestring[i:i+len(removestring)] == removestring:
            i += len(removestring)
        else:
            result += onestring[i]
            i += 1
    return result

onestring = input("Enter the original string: ")
removestring = input("Enter the string to remove: ")

finalstring = remove_substring(onestring, removestring)
print(f"The final string is: {finalstring}")
