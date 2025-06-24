# 02. Generate 20 random integers and store them in a list. Accept a number from the user and print position of all occurrences of that number in the list.

import random

def position_of_num():
    random_numbers = [random.randint(1, 50) for _ in range(20)]

    print("Generated list:", random_numbers)

    user_number = int(input("Enter a number to find its positions in the list: "))

    positions = [index for index, value in enumerate(random_numbers) if value == user_number]

    if positions:
        print(f"The number {user_number} is found at positions: {positions}")
    else:
        print(f"The number {user_number} is not in the list.")

position_of_num()        