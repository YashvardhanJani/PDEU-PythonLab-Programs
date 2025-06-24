# 03. Write a program that defines a function create_array() to create and return a 3D array whose dimensions are passed to the function. Also initialize each element of this array to a value passed to the function. e.g. create_array(3,4,5,n) where first three arguments are 3D array dimensions and 4th value is for initialing each value of the 3D array

def create_array(x, y, z, value):
    return [[[value for _ in range(z)] for _ in range(y)] for _ in range(x)]

array = create_array(3, 4, 5, 7)
for layer in array:
    print(layer)
