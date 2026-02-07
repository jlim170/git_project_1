"""Basic calculator operations."""
"""This module has functions to add, subtract, multiply, divide, and get the modulo of two input numbers."""

def add(a, b):
    """Add two numbers."""
    print(f"[DEBUG] Adding {a} + {b}")
    result = a + b
    print(f"[DEBUG] Result: {result}")
    return result

def subtract(a, b):
    """Subtract b from a."""
    print(f"[DEBUG] Subtracting {a} - {b}")
    result = a - b
    print(f"[DEBUG] Result: {result}")
    return result

def multiply(a, b):
    """Multiply two numbers."""
    print(f"[DEBUG] Multiplying {a} * {b}")
    result = a * b
    print(f"[DEBUG] Result: {result}")
    return result

def divide(a, b):
    """Divide a by b."""
    print(f"[DEBUG] Dividing {a} / {b}")
    if b == 0:
        print(f"[DEBUG] Error: Division by zero!")
        raise ValueError("Cannot divide by zero")
<<<<<<< HEAD
    return a / b

def modulo(a, b):
    """Return remainder of a divided by b."""
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b
=======
    result = a / b
    print(f"[DEBUG] Result: {result}")
    return result

def power(a, b):
    """Raise a to the power of b."""
    print(f"[DEBUG] Power {a} ** {b}")
    result = a ** b
    print(f"[DEBUG] Result: {result}")
    return result
>>>>>>> cbc5331 (FEATURE: Add power operation support)
