#!/usr/bin/python3
"""
Minimum Operations
"""
import math


def get_largest_factor(n):
    """
    returns the largest factor of a number excluding the number itself
    """
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return n // i
    return 1


def minOperations(n):
    """
    returns the minium number of operations required to generate n consecutive
    'H' characters using 'Copy All' and 'paste' operations.
    """
    if n <= 1:
        return 0
    largest_factor = get_largest_factor(n)
    if largest_factor == 1:
        return n
    return n // largest_factor + minOperations(largest_factor)
