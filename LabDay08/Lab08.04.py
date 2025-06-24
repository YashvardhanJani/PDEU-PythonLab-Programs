# 04. A set contains names which begin either with A or with B. Write a program to separate out the names into two sets, one containing names beginning with A and another with B.

def saparete_name():
    name_set = input("Enter names starts with 'A' or 'B' sapareted by space : ").split()
    print("Names :",set(name_set))

    a_names = {name for name in name_set if name.startswith('A')}
    b_names = {name for name in name_set if name.startswith('B')}

    print("Names start with 'A' :",a_names)
    print("Names start with 'B' :",b_names)

saparete_name()