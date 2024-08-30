def gcd(a, b):
    """
    Calculates the greatest common divisor (GCD) of two integers using Euclid's algorithm.
    
    Args:
        a (int): The first integer.
        b (int): The second integer.
    
    Returns:
        int: The greatest common divisor of a and b.
    """
    while b != 0:
        a, b = b, a % b
    return a

# Example usage
print(gcd(700, 2))  # Output: 1
