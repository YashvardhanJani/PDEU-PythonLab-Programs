# 10. Generate N numbers of Fibonacci series.

def fibonacci(n):
    fib_series = [0, 1]
    for _ in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

N = int(input("Enter the number of Fibonacci numbers to generate: "))
print(fibonacci(N))
