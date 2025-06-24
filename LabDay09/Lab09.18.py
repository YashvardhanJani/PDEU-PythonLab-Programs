# 18. Write a recursive function to obtain average of all numbers present in a given list.

def average_recursive(lst, index=0, total=0):
    if index == len(lst):
        return total / len(lst) if len(lst) > 0 else 0
    return average_recursive(lst, index + 1, total + lst[index])

lst = list(map(int, input("Enter list elements separated by space: ").split()))

avg = average_recursive(lst)
print("Average of the list:", avg)