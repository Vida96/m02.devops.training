# define your solution
def fibonacci(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)

