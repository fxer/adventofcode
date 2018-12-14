import re
import numpy as np

# print big ol' grids
np.set_printoptions(threshold=np.nan)

# Parse each line into the format:
# [id, x, y, width, height]
with open('day03.input') as f:
    data = []
    for line in f:
        data.append([int(x) for x in re.findall(r'\d+', line)])

def solve(gridsize):
    # create fabric grid
    grid = np.zeros(gridsize, np.int8)

    # Build grid with number of claims for each square
    for id, x, y, width, height in data:
        for row in range(height):
            for col in range(width):
                grid[y+row][x+col] += 1

    # Search grid for single claim that has only one claim for each square
    claim = -1
    for id, x, y, width, height in data:
        # Take a slice of the grid
        # first slice (y:y+height): selects your rows
        # second slice (x:x+width): selects the columns within those rows
        s = grid[y:y+height, x:x+width]

        # If every cell grid-slice equals one (ie: a single claim on each cell)
        # it will equal the area (width*height), and we've got our winner!
        if s.sum() == width*height:
            claim = id
            break;

    # Ignore squares that have 0 or 1 claims, that's fine it isn't double-booked!
    return (np.count_nonzero(grid[grid > 1]), claim)

print(solve((1000,1000)))
