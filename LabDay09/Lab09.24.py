# 24. A list contains names of Faculty Members. Write a program to filter out those names whose length is more than 8 characters.

def name_char_check(lst):
    filtered_lst = list(filter(lambda s : len(s) > 8,lst))
    return filtered_lst

lst = input("Enter names of Faculty Members separated by space : ").split()
print(name_char_check(lst))
