#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []

    # Initialize Pascal's triangle with the first row
    triangle = [[1]]

    # Build each row of Pascal's triangle
    for i in range(1, n):
        # The new row starts and ends with 1
        row = [1]

        # Calculate the in-between values
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])

        # End the row with 1
        row.append(1)

        # Add the row to the triangle
        triangle.append(row)

    return triangle

