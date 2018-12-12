import numpy as np

with open('day06.input') as f:
    data = [[int(x) for x in line.split(',')] for line in f]


def part1():
    grid = get_grid()

    # populate grid with initial coords
    for idx, coords in enumerate(data):
        grid[coords[1]][coords[0]] = idx+1

    for inversecell, v in np.ndenumerate(grid):
        shortest = 9999999
        cell = inversecell[::-1]

        # Don't modify cells with inital coords in them
        if grid[inversecell] == 0:
            for idx, coord in enumerate(data):
                dist = distance(cell, coord)

                # found a new shortest dist
                if dist < shortest:
                    shortest = dist
                    grid[inversecell] = idx+1

                # tied an existing shortest dist, so nobody wins that cell!
                elif dist == shortest:
                    grid[inversecell] = 0

    # print('top:', grid[0])
    # print('left:', grid[:,0])
    # print('right:', grid[:,-1])
    # print('bottom:', grid[-1])

    infinites = set(grid[0]).union(set(grid[:,0]).union(set(grid[:,1]).union(set(grid[-1]))))
    # print(infinites)

    largest_area = 0
    for idx, coords in enumerate(data):
        if idx not in infinites:
            field_size = np.count_nonzero(grid == idx)
            if field_size > largest_area:
                largest_area = field_size

    return largest_area

def part2(distance_limit):
    grid = get_grid()

    for inversecell, v in np.ndenumerate(grid):
        shortest = 9999999
        cell = inversecell[::-1]

        # Compute total distance from every coord for this cell
        total_dist = 0
        for origin in data:
            total_dist += distance(cell, origin)

        # Add total distance to grid cell
        grid[inversecell] = total_dist

    return np.count_nonzero(grid < distance_limit)

def get_grid():
    """
    Return a numpy grid of the correct size for the input list
    """
    width = -1
    height = -1
    for x,y in data:
        if x > width:
            width = x
        if y > height:
            height = y

    return np.zeros((height+1, width+1), np.int64)


def distance(coord1, coord2):
    """
    Return Manhattan Distance between two coordinates
    """
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

print(part1())
print(part2(10000))
