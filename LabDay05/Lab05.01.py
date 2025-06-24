# 01. Create a list of 5 odd integers using random nos. Similarly create a list of 4 even integers using random nos. Replace the third element of odd integers with a list of 4 even integers. Flattern, sort and print the list. Provide appropriate message at each stage.

import random

def random_odd_even():
    odd_num = [random.randrange(1,100,2) for _ in range(5)]
    even_num = [random.randrange(2,100,2) for _ in range(4)]

    print(odd_num)
    print(even_num)

    # Replace the third element of odd integers with a list of 4 even integers
    odd_num[2] = even_num
    print("After updating 3rd position of odd numbers' list with inserting even numbers' list :\n",odd_num)

    # Flatten the list
    flattened_list = []
    for item in odd_num:
        if isinstance(item, list):
            flattened_list.extend(item)
        else:
            flattened_list.append(item)
    print("Flattened list:", flattened_list)

    # Sort the list
    flattened_list.sort()
    print("Sorted list:", flattened_list)


random_odd_even()