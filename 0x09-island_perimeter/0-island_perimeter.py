def island_perimeter(grid):
""" initialize perimeter to """
    perimeter = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:  # if the cell contains land
                # check if the cell is on the perimeter
                if i == 0 or grid[i-1][j] == 0:  # top edge
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:  # left edge
                    perimeter += 1
                if i == len(grid)-1 or grid[i+1][j] == 0:  # bottom edge
                    perimeter += 1
                if j == len(grid[0])-1 or grid[i][j+1] == 0:  # right edge
                    perimeter += 1
    
    return perimeter

