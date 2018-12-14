#!/usr/bin/env python3
#
# Awesome resource for working with hexagonal grids:
# https://www.redblobgames.com/grids/hexagons/
# https://www.redblobgames.com/grids/hexagons/implementation.html#hex-arithmetic


with open('day11.input') as f:
    data = [x for x in f.read().strip().split(',')]


class Wanderer():
    def __init__(self, path, start_location=(0,0)):
        self.path = path
        self.location = start_location
        self.max_distance_from_origin = 0

    def wander(self):
        # Follow your path where it may take you my child
        for step in self.path:
            self.hex_move(step)
            # Did we wander farther from home than ever before?
            if self.distance_from_origin() > self.max_distance_from_origin:
                self.max_distance_from_origin = self.distance_from_origin()

    def distance_from_origin(self):
        return max((self.location[0]), abs(self.location[1]))

    def hex_move(self, direction):
        if direction == 'n':
            self.location = (self.location[0], self.location[1]-1)
        elif direction == 'ne':
            self.location = (self.location[0]+1, self.location[1]-1)
        elif direction == 'se':
            self.location = (self.location[0]+1, self.location[1])
        elif direction == 's':
            self.location = (self.location[0], self.location[1]+1)
        elif direction == 'sw':
            self.location = (self.location[0]-1, self.location[1]+1)
        elif direction == 'nw':
            self.location = (self.location[0]-1, self.location[1])


def searchparty():
    w = Wanderer(path=data)
    w.wander()
    print("part1: wandered to:", w.location, "steps from origin:", w.distance_from_origin())
    print("part2: greatest distance:", w.max_distance_from_origin)


def example1():
    cases = [(('ne','ne','ne'), 3),
             (('ne','ne','sw','sw'), 0),
             (('ne','ne','s','s'), 2),
             (('se','sw','se','sw','sw'), 3)]

    for path, answer in cases:
        w = Wanderer(path=path)
        w.wander()
        print("example1: wandered to:", w.location, "steps from origin:", w.distance_from_origin())
        assert answer == w.distance_from_origin()



example1()
searchparty()
