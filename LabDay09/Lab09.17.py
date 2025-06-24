# 17. A list contains some negative and some positive values. Write a recursive function that sanitizes the list by replacing all negative numbers with 0.

def sanitize_list(lst, index=0):
    if index == len(lst):
        return
    if lst[index] < 0:
        lst[index] = 0
    sanitize_list(lst, index + 1)

lst = list(map(int, input("Enter list elements separated by space: ").split()))

sanitize_list(lst)
print("Sanitized list:", lst)
