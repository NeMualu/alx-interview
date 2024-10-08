#!/usr/bin/python3
"""
This function works as follows:

It checks if n <= 0, and if so, returns an empty list.
It initializes the triangle with the first row, [1].
For each subsequent row, it starts and ends with 1. The intermediate elements are calculated by summing the two elements directly above it in the previous row.
The result is returned as a list of lists representing Pascal's triangle.
"""

def pascal_triangle(n):
    if n <= 0:
        return []
"""
    # Initialize Pascal's triangle with the first row
"""
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

