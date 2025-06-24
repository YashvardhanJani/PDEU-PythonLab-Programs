# 11. Calculate sin(x); x is a radian value. The formula is as under: (hint: degrees can be converted into radians by 3.14159 / 180.)

import math

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def sine_taylor_series(x, terms=10):
    sin_x = 0
    for n in range(terms):
        sign = (-1) ** n
        sin_x += (sign * (x ** (2 * n + 1))) / factorial(2 * n + 1)
    return sin_x

degree = float(input("Enter angle in degrees: "))
radian = degree * (math.pi / 180) 

print(f"sin({degree} degrees) ≈ {sine_taylor_series(radian)}")
