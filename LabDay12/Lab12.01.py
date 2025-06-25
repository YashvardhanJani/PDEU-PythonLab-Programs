# 01. Write a program to create a class that represents Complex numbers containing real and imaginary parts and then use it to perform complex number addition, subtraction, multiplication and division.

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    # Using Dunder Functions
    def __str__(self):
        return f"{self.real}{self.img:+}i"

    def __add__(self, other):
        return Complex(self.real + other.real, self.img + other.img)
    
    def __sub__(self, other):
        return Complex(self.real - other.real, self.img - other.img)
    
    def __mul__(self, other):
        return Complex(self.real * other.real, self.img * other.img)
    
    def __truediv__(self, other):
        return Complex(round(self.real / other.real, 1), round(self.img / other.img, 1))

num1 = Complex(7, 1)
num2 = Complex(5, 9)
num3 = Complex(1, 9)

print("Complex Num.1 =",num1)
print("Complex Num.2 =",num2)
print("Addition :",num1 + num2)
print("Subtraction :",num1 - num2)
print("Multiplication :",num1 * num2)
print("Division :",num1 / num2)
print("Complex Num.3 =",num3)
print("Addition of all 3 Complex Num:",num1+num2+num3)