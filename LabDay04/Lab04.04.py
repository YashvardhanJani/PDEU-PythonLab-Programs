# 04. Check whether a given number is prime, is perfect, is Armstrong, is palindrome, is automorphic.

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n <= 1:
        return False
    sum_factors = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            sum_factors += i
            if i != n // i:
                sum_factors += n // i
    return sum_factors == n

def is_armstrong(n):
    num_str = str(n)
    num_length = len(num_str)
    sum_pow = sum(int(digit) ** num_length for digit in num_str)
    return sum_pow == n

def is_palindrome(n):
    num_str = str(n)
    return num_str == num_str[::-1]

def is_automorphic(n):
    square = n * n
    return str(square).endswith(str(n))

def check_number_properties(n):
    print(f"Number: {n}")
    print(f"Is Prime: {is_prime(n)}")
    print(f"Is Perfect: {is_perfect(n)}")
    print(f"Is Armstrong: {is_armstrong(n)}")
    print(f"Is Palindrome: {is_palindrome(n)}")
    print(f"Is Automorphic: {is_automorphic(n)}")

number = int(input("Enter a number: "))
check_number_properties(number)