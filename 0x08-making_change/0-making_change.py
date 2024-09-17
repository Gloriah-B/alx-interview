#!/usr/bin/python3
"""
Coin Change Algorithm
"""


def makeChange(coins, total):
    """Calculate fewest number of coins needed to meet a given total amount

    Args:
        coins (list): A list of coin values available.
        total (int): The target amount.

    Returns:
        int: The fewest number of coins needed to reach the total,
             or -1 if it's not possible.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins.sort(reverse=True)

    ncoins = 0
    cpy_total = total

    for coin in coins:
        if cpy_total <= 0:
            break
        # Use as many of this coin as possible
        num_of_coins = cpy_total // coin
        cpy_total -= num_of_coins * coin
        ncoins += num_of_coins

    # If the total cannot be met, return -1
    return -1 if cpy_total > 0 else ncoins
