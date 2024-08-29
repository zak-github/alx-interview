#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 1:
                # look up
                if y == 0:
                    count += 1
                elif grid[y-1][x] == 0:
                    count += 1
                # look down
                if y == (len(grid) - 1):
                    count += 1
                elif grid[y+1][x] == 0:
                    count += 1
                # look left
                if x == 0:
                    count += 1
                elif grid[y][x-1] == 0:
                    count += 1
                # look right
                if x == (len(grid[y]) - 1):
                    count += 1
                elif grid[y][x+1] == 0:
                    count += 1
    return count
