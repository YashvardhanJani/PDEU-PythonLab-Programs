# 19. Write a recursive function to obtain length of a given string.

def string_length_recursive(s, index=0):
    if index == len(s):
        return index
    return string_length_recursive(s, index + 1)

s = input("Enter a string : ")
print("Length of the string:", string_length_recursive(s))
