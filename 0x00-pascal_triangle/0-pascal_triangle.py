#!/usr/bin/python3
#!/usr/bin/python3
"""
This module contains the pascal_triangle function, which generates
Pascal's triangle up to a given number of rows.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to n rows.
    
    Args:
        n (int): The number of rows to generate.

    Returns:
        List[List[int]]: A list of lists where each inner list represents
        a row of Pascal's triangle. Returns an empty list if n <= 0.
    """
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

