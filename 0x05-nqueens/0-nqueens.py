#!/usr/bin/python3

import sys

def solve_nqueens(n, i, a, b, c, solution=[]):
    """ solve nqueens. """
    if i == n:
        yield solution
        return
    for j in range(n):
        if j not in a and i+j not in b and i-j not in c:
            yield from solve_nqueens(n, i+1, a+[j], b+[i+j], c+[i-j], solution + [[i, j]])

def nqueens(n):
    """ nqueens. """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    for solution in solve_nqueens(n, 0, [], [], []):
        print (solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    n = int(sys.argv[1])
    nqueens(n)

