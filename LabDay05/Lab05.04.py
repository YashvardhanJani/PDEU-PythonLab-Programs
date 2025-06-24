# 04. Generate 30 random numbers and put them in a list. Create two more lists – one containing only +ve numbers and another with –ve nos.

import random

def sort_positive_negative_num():
    random_numbers = [random.randint(-50, 50) for _ in range(30)]

    print("Original list:", random_numbers)

    positive_numbers = [num for num in random_numbers if num > 0]
    negative_numbers = [num for num in random_numbers if num < 0]

    print("Positive numbers:", positive_numbers)
    print("Negative numbers:", negative_numbers)

sort_positive_negative_num()    