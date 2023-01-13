#!/usr/bin/python3
"""Minimum Operations."""


def minOperations(n):
    """calculates the fewest number of operations needed
        to result in exactly n H characters in the file.
    """
    if n <= 0:
        return 0
    opers = 0
    while n > 2:
        if n % 2 == 0:
            opers += 1
            n = n // 2
        else:
            return 0
    return opers + (n - 1)
