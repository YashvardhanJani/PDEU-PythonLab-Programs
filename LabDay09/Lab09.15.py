# 15. Write a recursive function that reverses the list of numbers that it receives.

def reverse_list(lst):
    if not lst:  
        return []
    return [lst[-1]] + reverse_list(lst[:-1]) 

numbers = input("Enter the elements for list1 separated by space : ").split()
print("Original List :-",numbers)
print("Reversed List :-",reverse_list(numbers))  
