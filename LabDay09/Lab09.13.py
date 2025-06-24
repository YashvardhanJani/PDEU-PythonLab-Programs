# 13. A positive integer is entered through the keyboard. Write a function to find its binary equivalent of this number.

def binary_equivalent(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return binary_equivalent(n // 2) + str(n % 2)

num = int(input("Enter a positive integer: "))
if num >= 0:
    print("Binary equivalent:", binary_equivalent(num))
else:
    print("Please enter a non-negative integer.")
