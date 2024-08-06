#!/usr/bin/python3
"""
This module contains a function to calculate the minimum number of operations
needed to achieve exactly n H characters in a file
using 'Copy All' and 'Paste' operations.
"""


def minOperations(n):
    """
    Calculate fewest no. of operations needed to result in exactly n H chars

    Parameters:
    n (int): The target number of H characters.

    Returns:
    int: The minimum number of operations needed to achieve n H characters
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
