def fibonacci_recursive(n):
    if n <= 0:
        return "Input must be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_iterative(n):
    if n <= 0:
        return "Input must be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a

# Example usage
num = int(input("Enter a number: "))
print(f"Fibonacci (Recursive) of {num}: {fibonacci_recursive(num)}")
print(f"Fibonacci (Iterative) of {num}: {fibonacci_iterative(num)}")
