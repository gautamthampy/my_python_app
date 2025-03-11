"""Simple calculator module for demonstrating Jenkins pipeline."""


def add(a, b):
    """Add two numbers and return the result."""
    return a + b


def subtract(a, b):
    """Subtract b from a and return the result."""
    return a - b


def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b


def divide(a, b):
    """Divide a by b and return the result.
    
    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print("Simple Calculator")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"20 / 5 = {divide(20, 5)}")