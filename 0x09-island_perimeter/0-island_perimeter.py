#!/usr/bin/python3
"""
def island_perimeter(grid): that returns the perimeter of the island
described in grid
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.

    Args:
        grid (list of list of int): A 2D grid representing water
         (0) and land (1).

    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:  # Land cell
                # Add 4 for the land cell
                perimeter += 4
                # Subtract 1 for each neighboring land cell
                if row > 0 and grid[row - 1][col] == 1:  # Top neighbor
                    perimeter -= 1
                # Bottom neighbor
                if row < rows - 1 and grid[row + 1][col] == 1:
                    perimeter -= 1
                if col > 0 and grid[row][col - 1] == 1:  # Left neighbor
                    perimeter -= 1
                # Right neighbor
                if col < cols - 1 and grid[row][col + 1] == 1:
                    perimeter -= 1

    return perimeter
