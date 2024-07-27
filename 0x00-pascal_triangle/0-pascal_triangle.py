#!/usr/bin/python3
"""
This module contains a function that generates Pascal's Triangle
up to a specified number of rows.
"""

def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list of list of int: A list containing lists of integers,
                             representing Pascal's Triangle.
                             Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # The first element is always 1
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)  # The last element is always 1
        triangle.append(new_row)

    return triangle

# Example usage
if __name__ == "__main__":
    print(pascal_triangle(5))
    print(pascal_triangle(1))
    print(pascal_triangle(0))
    print(pascal_triangle(10))
    print(pascal_triangle(100))

