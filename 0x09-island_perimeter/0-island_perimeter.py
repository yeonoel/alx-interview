#!/usr/bin/python3
""" Island perimeter"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid. """
    perimeter = 0
    grid_len = len(grid)
    col = len(grid[0]) if grid_len else 0

    for i in range(grid_len):
        row_len = len(grid[i])
        for j in range(row_len):
            index = [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]
            check = [1 if k[0] in range(grid_len) and k[1] in range(col)
                     else 0 for k in index]

            if grid[i][j]:
                perimeter += sum([1 if not r or not grid[k[0]][k[1]] else 0
                                  for r, k in zip(check, index)])

    return perimeter
