def pascal_triangle(n):

    triangle = []
    elem = 0
    for row in range(n):
        current_row = []

        for col in range(row + 1):
            if (col == 0 or col == row):
                current_row.append(1)
            else:
                elem = triangle[row - 1][col - 1] + triangle[row - 1][col]
                current_row.append(elem)

        triangle.append(current_row)

    return (triangle)
