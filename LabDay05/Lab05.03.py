# 03. Generate 50 random numbers in the range 1 and 30. Remove all duplicate values from the list.

import random

def remove_duplicate():
    random_numbers = [random.randint(1, 30) for _ in range(50)]

    print("Original list with duplicates:", random_numbers)

    unique_numbers = list(set(random_numbers))

    print("List after removing duplicates:", unique_numbers)

remove_duplicate()    