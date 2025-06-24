# 09. Take two lists of numbers. Create third list of numbers for only those numbers from first list which are not there in 2nd list (use list comprehension).

def not_common_item():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list2 = [2, 4, 6, 8, 10, 12, 14, 16]

    set2 = set(list2)

    list3 = [num for num in list1 if num not in set2]

    print("List 1:", list1)
    print("List 2:", list2)
    print("List 3 (numbers in List 1 but not in List 2):", list3)

not_common_item()