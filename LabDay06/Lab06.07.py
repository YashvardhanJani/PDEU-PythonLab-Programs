# 07. Delete an element of a tuple.

def del_ele_tuple():
    mytuple = ('Shyam','Krushn','Devakinandan','Mohan','Murlidhar')
    print(mytuple)
    
    del_ele = input("Enter element which you want to Delete : ")

    mytuple = tuple(item for item in mytuple if item != del_ele)

    print("After Delete element :",mytuple)
    
del_ele_tuple()