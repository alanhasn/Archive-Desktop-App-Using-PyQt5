def prime_factors(n):
    """
    Finds the prime factors of a given number.
    
    Args:
        n (int): The number to be factored.
    
    Returns:
        list: The list of prime factors of n.
    """
    factors = []
    
    # Start with the smallest prime factor (2)
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Check for other prime factors
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    
    # If n is a prime number greater than 2, add it to the list
    if n > 2:
        factors.append(n)
    
    return factors

# Example usage
print(prime_factors(98))   # Output: [2, 2, 3, 5]
