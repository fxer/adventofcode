import numpy as np

with open('day06.input') as f:
    data = []
    # read instructions line by line
    for line in f:
        row = []
        # split line into individual words/coords
        for value in line.strip().split(' '):
            # command is stored at front of row
            if value == 'on' or value == 'off' or value == 'toggle':
                row.append(value)
            # when we hit starting and ending coords, store them too
            elif value[0].isdigit():
                row.append([int(x) for x in value.split(',')])
        data.append(row)

def part1(instructions):
    # create light grid with all lights off
    grid = [[False for i in range(1000)] for j in range(1000)]

    # loop over each instruction
    for row in instructions:
        # loop starting from top x coord (range is non-inclusive of "end" so add 1)
        for x in range(row[1][0], row[2][0]+1):
            for y in range(row[1][1], row[2][1]+1):
                # command tells us what to do with the cell
                if row[0] == 'toggle':
                    # invert the boolean
                    grid[x][y] = not grid[x][y]
                elif row[0] == 'on':
                    grid[x][y] = True
                elif row[0] == 'off':
                    grid[x][y] = False

    # numpy will count up all the True booleans
    return np.count_nonzero(grid)

def part2(instructions):
    # create light grid with all lights at zero brightness
    grid = [[0 for i in range(1000)] for j in range(1000)]

    # loop over each instruction
    for row in instructions:
        # loop starting from top x coord (range is non-inclusive of "end" so add 1)
        for x in range(row[1][0], row[2][0]+1):
            for y in range(row[1][1], row[2][1]+1):
                # command tells us what to do with the cell
                if row[0] == 'toggle':
                    grid[x][y] += 2
                elif row[0] == 'on':
                    grid[x][y] += 1
                elif row[0] == 'off':
                    grid[x][y] = max(0, grid[x][y]-1)

    return np.sum(grid)


print(part1(data))
print(part2(data))
