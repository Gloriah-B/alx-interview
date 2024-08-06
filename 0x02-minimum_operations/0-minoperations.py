#!/usr/bin/python3
"""
This module contains a function to calculate the minimum number of operations 
needed to achieve exactly n H characters in a file using 'Copy All' and 'Paste' operations.
"""

def min_operations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n H characters.

    Parameters:
    n (int): The target number of H characters.

    Returns:
    int: The minimum number of operations needed to achieve n H characters. 
         Returns 0 if n is impossible to achieve.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while factor * factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    if n > 1:
        operations += n

    return operations

# Example usage
if __name__ == "__main__":
    n = 9
    print(min_operations(n))  # Output: 6

