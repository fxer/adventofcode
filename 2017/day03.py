'''
This one killed me.

Part 1 havily borrowed from:
https://www.reddit.com/r/adventofcode/comments/7h7ufl/2017_day_3_solutions/dqp3pqq/

Part 2 heavily borrowed from:
https://github.com/vesche/adventofcode-2017/blob/master/day03.py

'''

from math import sqrt, ceil
import sys

if len(sys.argv) > 1:
    input = int(sys.argv[1])
else:
    with open('day03.input') as f:
        input = int(f.read().rstrip())

def side_length(num):
    side = ceil(sqrt(num))
    side = side if side % 2 != 0 else side + 1
    return side

def ring(num):
    # calculate dimensions of board to hold our given location
    # for i in range(1,1000):
    #     if (i*2-1)**2 >= location:
    #         print(i, (i*2-1)**2)
    #         break
    #
    # solve above for i, which gives maximum value appearing in a ring
    return ceil(sqrt(num)) // 2 + 1

def part1(num):
    side = side_length(num)
    steps_to_center_from_axis = (side - 1) // 2

    # a) side**2 is the highest number in the current ring
    # b) to find the axis from here, move backwards half the length of a side (rounded down)
    # c) to find the next axis, go back an entire side length minus 1
    # d) repeat step c to find all four sides
    axes = [side**2 - (side // 2) - (side - 1)*n for n in range(4)]

    # which axis is closest to our location?
    nearest_axis = min(axes, key=lambda x: abs(x - num))

    # how far are we from that nearest axis?
    axis_distance = abs(nearest_axis - num)

    return axis_distance + steps_to_center_from_axis

def part2(num):

    # list of offset coordinates that surround a given cell
    coords = [(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]

    # track our x and y coords, starting at zero
    x = y = 0

    # Track how our x coord will change
    delta_x = 0

    # Track how our y coord will change
    delta_y = -1

    # keep a dict of the cells we have calculated
    grid = {}

    while True:
        # track sum of surrounding cells
        total = 0

        # loop over each offset from the current cell
        for offset_x, offset_y in coords:
            if (x + offset_x, y + offset_y) in grid:
                total += grid[(x + offset_x, y + offset_y)]

        # if the total for this cell is greater than our input we're done!
        if total > num:
            return total

        # special case for the starting cell
        if (x,y) == (0,0):
            grid[(0,0)] = 1
        else:
            grid[(x,y)] = total

        # calculate change in x and y for the next cell
        # when x == y, you've hit the "top right" or "bottom left" corner
        # when x is negative and equals inverse y, you've hit the "top left" corner
        # when x is positive and equals 1-y, you've expanded into the next ring
        if (x == y) or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            delta_x, delta_y = -delta_y, delta_x

        # move to the next coordinate
        x, y = x+delta_x, y+delta_y


print(part1(input))
print(part2(input))
