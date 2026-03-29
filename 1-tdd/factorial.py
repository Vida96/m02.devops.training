# define your solution
def factorial(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    return 1 if n == 0 else n * factorial(n - 1)

