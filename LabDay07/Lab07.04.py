# 04. Write a program that reads a string from the keyboard and creates dictionary containing frequency of each character occurring in the string. 

def char_frequency():
    input_str = input("Enter a string: ")  
    char_frq = {}

    for char in input_str:
        if char in char_frq:
            char_frq[char] += 1
        else:
            char_frq[char] = 1

    print("Character frequency:", char_frq)


char_frequency()

# Note :- Here 'A' & 'a' are count as different character.