# 04. Create a list of tuples containing a food item and its price. Sort the tuples in descending order by price.

import operator

def pricewise_sort():
    lst = [("Banana",40),("Apple",160),("Guava",140),("Mango",120),("Strawberry",200)]

    print (sorted(lst, key = operator.itemgetter(1), reverse = True))

pricewise_sort()