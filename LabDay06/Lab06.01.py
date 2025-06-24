# 01. A list contains names of boys and girls as its elements. Boys’ names are stored as tuples. Write a program to find out number of boys and girls in the list. (Hint: use isinstance(ele,tuple))

def count_boys_girls():
    lst = ['Radha','Yamuna',('Shyam','Ram'),'Devhuti',('Arjun','Bhisma')]
    i,j = 0,0

    for ele in lst:
        if isinstance(ele, tuple):
            i += len(ele)
        else:
            j+=1 

    print(f"Boys = {i} & Girls = {j}")        

count_boys_girls()               