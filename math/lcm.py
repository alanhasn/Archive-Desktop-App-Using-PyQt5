# def gcd(a, b):
#     """
#     Computes the Greatest Common Divisor (GCD) of two numbers.
    
#     Args:
#         a (int): The first number.
#         b (int): The second number.
    
#     Returns:
#         int: The GCD of a and b.
#     """
#     while b != 0:
#         a, b = b, a % b
#     return a

# def lcm(a, b):
#     """
#     Computes the Least Common Multiple (LCM) of two numbers.
    
#     Args:
#         a (int): The first number.
#         b (int): The second number.
    
#     Returns:
#         int: The LCM of a and b.
#     """
#     return (a * b) // gcd(a, b)

# # Example usage 2011
# print(lcm(43,23))  

import math

def calculate(operation, *args):
    """
    Performs the specified mathematical operation on the given arguments and shows the step-by-step solution.
    
    Parameters:
    operation (str): The mathematical operation to perform. Can be one of the following: 
                     'add', 'subtract', 'multiply', 'divide', 'power', 'sqrt', 'sin', 'cos', 'tan'.
    *args (float): The numbers to perform the operation on.
    
    Returns:
    float or str: The result of the mathematical operation, or an error message if the input is invalid.
    """
    operations = {
        'add': lambda x, y: (f"{x} + {y}", x + y),
        'subtract': lambda x, y: (f"{x} - {y}", x - y),
        'multiply': lambda x, y: (f"{x} * {y}", x * y),
        'divide': lambda x, y: (f"{x} / {y}", x / y),
        'power': lambda x, y: (f"{x} ^ {y}", x ** y),
        'sqrt': lambda x: (f"√{x}", math.sqrt(x)),
        'sin': lambda x: (f"sin({x})", math.sin(x)),
        'cos': lambda x: (f"cos({x})", math.cos(x)),
        'tan': lambda x: (f"tan({x})", math.tan(x))
    }
    
    if operation not in operations:
        return "Invalid operation"
    
    if operation in ['add', 'subtract', 'multiply', 'divide', 'power']:
        if len(args) != 2:
            return "Invalid number of arguments"
        step, result = operations[operation](*args)
        print(f"Step: {step}")
        return result
    else:
        if len(args) != 1:
            return "Invalid number of arguments"
        step, result = operations[operation](*args)
        print(f"Step: {step}")
        return result

# Example usage
# print(calculate('add', 5, 3))   # Output: Step: 5 + 3
                            #   Output: 8.0
# print(calculate('subtract', 10, 4))  # Output: Step: 10 - 4
#                                    # Output: 6.0
# print(calculate('multiply', 2, 6))  # Output: Step: 2 * 6
#                                   # Output: 12.0
print(calculate('divide', 3434, 23))   # Output: Step: 15 / 3
#                                   # Output: 5.0
# print(calculate('power', 2, 3))    # Output: Step: 2 ^ 3
#                                  # Output: 8.0
# print(calculate('sqrt', 16))       # Output: Step: √16
#                                  # Output: 4.0
# print(calculate('sin', math.pi/2)) # Output: Step: sin(π/2)
#                                  # Output: 1.0
# print(calculate('cos', 0))         # Output: Step: cos(0)
#                                  # Output: 1.0
# print(calculate('tan', math.pi/4)) # Output: Step: tan(π/4)
#                                  # Output: 0.9999999999999999
# print(calculate('invalid', 2, 3))  # Output: Invalid operation