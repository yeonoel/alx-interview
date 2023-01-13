#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """calculates the fewest number of operations needed
    to result in exactly n H characters in the file."""
    if (n < 2):
        return 0

    operations, i = 0, 2

    while i <= n:
        if n % i == 0:
            operations += i
            n = n / i
            i -= 1
        i += 1
    return
