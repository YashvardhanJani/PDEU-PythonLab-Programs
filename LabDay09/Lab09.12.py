# 12. If a positive integer is entered through the keyword, write a recursive function to obtain the prime factors of the number. 

def prime_factors(n, divisor=2):
    if n <= 1:
        return []
    if n % divisor == 0:
        return [divisor] + prime_factors(n // divisor, divisor)
    else:
        return prime_factors(n, divisor + 1)

num = int(input("Enter a positive integer: "))
if num > 0:
    print("Prime factors:", prime_factors(num))
else:
    print("Please enter a positive integer.")
