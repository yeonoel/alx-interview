#!/usr/bin/python3

def island_perimeter(grid):
    """ return island perimeter. """
    perimeter = 0
    grid_len = len(grid)

    for j in range(grid_len):
        row_len = len(grid[j])
        for i in range(row_len):
            if grid[j][i] == 1:
                if i == 0 or grid[j][i-1] == 0:
                    perimeter += 1
                if i == row_len - 1 or grid[j][i+1] == 0:
                    perimeter += 1
                if j == 0 or grid[j+1][i] == 0:
                    perimeter += 1
                if j == grid_len - 1 or grid[j-1][i] == 0:
                    perimeter += 1

    return perimeter
