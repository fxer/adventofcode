#!/usr/bin/env python3

import re
import numpy
import sys


# print big ol' grids
numpy.set_printoptions(threshold=numpy.nan, linewidth=numpy.nan)

def parse_input(filename='day10.input'):
    data = []
    with open(filename) as f:
        for line in f:
            x, y, q, r = map(int, re.findall(r'-?\d+', line))
            data.append([[x, y], [q, r]])

    return data

class AlignStars():
    def __init__(self, coords):
        self.coords = coords
        self.ticks = 0

        # Track our bounding box
        self.xmax = 0
        self.xmin = 0
        self.ymax = 0
        self.ymin = 0

    def tick(self, ticks=1, direction='forward'):
        # Move each coordinate based on its velocity
        for i in range(ticks):
            new_coords = []
            for pos, vel in self.coords:
                if direction == 'forward':
                    new_coords.append([[pos[0] + vel[0], pos[1] + vel[1]], vel])
                else:
                    new_coords.append([[pos[0] - vel[0], pos[1] - vel[1]], vel])
            self.coords = new_coords

            if direction == 'forward':
                self.ticks += 1
            else:
                self.ticks -= 1

        # Update our bounding box based on new coords
        xmax = 0
        ymax = 0
        xmin = 999999999
        ymin = 999999999

        for coord, vel in self.coords:
            if coord[0] > xmax:
                xmax = coord[0]
            elif coord[0] < xmin:
                xmin = coord[0]
            if coord[1] > ymax:
                ymax = coord[1]
            elif coord[1] < ymin:
                ymin = coord[1]

        self.xmax = xmax
        self.xmin = xmin
        self.ymax = ymax
        self.ymin = ymin


    def display(self):
        # print the grid representation of the stars
        grid = numpy.full(self.volume(), ' ', numpy.str)

        # fill the grid with our coords
        for coord, vel in self.coords:
            grid[coord[0]-self.xmin][coord[1]-self.ymin] = '#'

        # Much easier to read if we remove all the numpy delimiters
        for row in numpy.swapaxes(grid, 0, 1):
            print(''.join(row))

        # print(numpy.swapaxes(grid, 0, 1))


    def volume(self):
        return (self.xmax - self.xmin + 1, self.ymax - self.ymin + 1)


    def find_message(self):
        volume = sys.maxsize
        for i in range(1, 999999):
            self.tick()
            new_volume = self.volume()[0] * self.volume()[1]

            # if our bounding box reaches a minimum, that's probably our secret message
            if new_volume > volume:
                # we overshot! last tick must have been the answer. Rollback 1 tick!
                self.tick(ticks=1, direction='backward')
                break
            else:
                volume = new_volume

        self.display()


def solve():
    lights = parse_input()
    stars = AlignStars(lights)
    stars.find_message()
    print("ticks:", stars.ticks)


def example():
    lights = parse_input('day10.input_example')
    stars = AlignStars(lights)
    stars.find_message()
    print("ticks:", stars.ticks)


example()
solve()
