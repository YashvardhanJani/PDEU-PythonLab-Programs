# 06. Write a function to create and return a list containing tuples of the form (x,x2,x3) for all x between 1 and given ending value (both inclusive).

def create_tuple_list(end_value):
    return [(x, x**2, x**3) for x in range(1, end_value + 1)]

end_value = int(input("Enter the End Value : "))
print(create_tuple_list(end_value))

