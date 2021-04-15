#!/usr/bin/env python3
import numpy

numpy.set_printoptions(threshold=numpy.nan, linewidth=numpy.nan)


def load_input(filename='day11.input'):
    with open(filename) as f:
        return int(f.read().strip())


class FuelCell():
    def __init__(self, serial_number, height=300, width=300):
        self.serial_number = serial_number
        self.height = height
        self.width = width
        # self.grid = self.compute_forloop()
        self.grid = numpy.fromfunction(self.compute_numpy, (height, width), dtype=numpy.int32)


    def compute_forloop(self):
        """
        Compute the power at each fuel cell location based on serial_number
        numpy.zeros and forloop is quite a bit slower than directly using numpy.fromfunction()
        """
        grid = numpy.zeros((self.height, self.width), numpy.int32)

        for x in range(self.width):
            for y in range(self.height):
                rackid = x + 10
                power = rackid * y
                power += self.serial_number
                power *= rackid
                power = f'{power:03}'               # Pad with zeroes to hundreds space at least
                power = int(list(str(power))[-3])   # Explode power value, extract hundreds, re-intify
                power -= 5

                grid[(x,y)] = power

        return grid


    def compute_numpy(self, x, y):
        """
        Let numpy populate its grid directly with a function callback
        """
        # Compute the power at each fuel cell location based on serial_number
        rackid = x + 10
        power = rackid * y
        power += self.serial_number
        power *= rackid
        return (power // 100 % 10) - 5


    def power_of_cell(self, coords):
        """
        Return power level of a single fuel cell
        """
        return self.grid[coords]


    def power_of_grid(self, coords, dimension=3):
        """
        return power of SIZExSIZE grid starting from top left of input coords
        """
        # behold the power of numpy grid slicing
        # *much* faster than double for loops over x,y coords
        return numpy.sum(self.grid[coords[0]:coords[0]+dimension, coords[1]:coords[1]+dimension])


def part1():
    """
    find 3x3 grid segment with the highest power level
    """
    fc = FuelCell(load_input())

    high_pow = 0
    high_coords = []

    for x in range(fc.width-2):
        for y in range(fc.height-2):
            power = fc.power_of_grid((x,y))
            if power > high_pow:
                high_pow = power
                high_coords = (x,y)

    print(f'part1: 3x3 highest power: {high_pow}, coords: {high_coords}')


def part2():
    """
    find square (NxN) segment grid with the most power for any segment size from: 1x1 to 300x300
    """
    fc = FuelCell(load_input())

    high_pow = -1
    high_dimension = -1
    high_coords = []

    # find size of grid square we'll be working with
    for dimension in range(300):
        # pick x,y so we don't go index out of bounds
        for x in range(fc.width - dimension):
            for y in range(fc.height - dimension):
                power = fc.power_of_grid(coords=(x,y), dimension=dimension)
                if power > high_pow:
                    high_pow = power
                    high_coords = (x,y)
                    high_dimension = dimension

        # print("current:", dimension, (x,y), "highest:", high_dimension, high_coords, high_pow)


    print(f'part2: NxN highest power: {high_pow}, coords: {high_coords}, dimension: {high_dimension}')


def example1():
    # format: fuel cell @ (x,y), grid serial number, power level
    # individual fuel cells
    fuel_cell = [
        [(3,5), 8, 4],
        [(122,79), 57, -5],
        [(217,196), 39, 0],
        [(101,153), 71, 4],
    ]

    # 3x3 fuel cell grids
    fuel_cell_grid = [
        [(21,61), 42, 30],
        [(33,45), 18, 29],
    ]

    for coords, serial, power in fuel_cell:
        fc = FuelCell(serial)
        result = fc.power_of_cell(coords)
        print(f'example1: single coord: {coords} serial#: {serial} power: {power} -> found power: {result}')
        assert result == power

    for coords, serial, power in fuel_cell_grid:
        fc = FuelCell(serial)
        result = fc.power_of_grid(coords)
        print(f'example1: 3x3 coord: {coords} serial#: {serial} power: {power} -> found power: {result}')
        assert result == power


def example2():
    # 3x3 fuel cell grids
    fuel_cell_grid = [
        [(90,269), 18, 113, 16],
        [(232,251), 42, 119, 12],
    ]

    for coords, serial, power, size in fuel_cell_grid:
        fc = FuelCell(serial)
        result = fc.power_of_grid(coords, size)
        print(f'example2: {size}x{size} coord: {coords} serial#: {serial} power: {power} -> found power: {result}')
        assert result == power



example1()
example2()
part1()
part2()
