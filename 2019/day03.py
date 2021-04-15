with open('day03.input') as f:
    data = {}
    lines = f.read().splitlines()
    data['a'] = [x for x in lines[0].split(',')]
    data['b'] = [x for x in lines[1].split(',')]

def part1(wireA, wireB):
    pointsA = get_points(wireA)
    pointsB = get_points(wireB)

    # find common points between sets with convenient '&' command
    crossings = pointsA & pointsB

    # map abs() function to all tuple elements, and sum each tuple, coverting into a list via comprehension
    return min([sum(map(abs,el)) for el in crossings])


def part2():
    pass

# return Set of tuples representing points the wire crossed through
def get_points(wire):
    points = set()

    # track current position
    pos = (0,0)
    for cmd in wire:
        if cmd[0] == 'R':
            # move positive along x axis
            for i in range(pos[0]+1, pos[0]+int(cmd[1:])+1):
                pos = (i, pos[1])
                # print("step: ", pos)
                points.add(pos)
        elif cmd[0] == 'L':
            # move negative along x axis
            for i in range(pos[0]-1, pos[0]-int(cmd[1:])-1, -1):
                pos = (i, pos[1])
                # print("step: ", pos)
                points.add(pos)
        elif cmd[0] == 'U':
            # move positive along y axis
            for i in range(pos[1]+1, pos[1]+int(cmd[1:])+1):
                pos = (pos[0], i)
                # print("step: ", pos)
                points.add(pos)
        elif cmd[0] == 'D':
            # move negative along y axis
            for i in range(pos[1]-1, pos[1]-int(cmd[1:])-1, -1):
                pos = (pos[0], i)
                # print("step: ", pos)
                points.add(pos)

    # print(points)
    return points

def tests():
    wireA = "R8,U5,L5,D3".split(',')
    wireB = "U7,R6,D4,L4".split(',')
    assert part1(wireA, wireB) == 6

    wireA = "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(',')
    wireB = "U62,R66,U55,R34,D71,R55,D58,R83".split(',')
    assert part1(wireA, wireB) == 159

    wireA = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(',')
    wireB = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(',')
    assert part1(wireA, wireB) == 135

tests()
print(part1(data['a'], data['b']))
print(part2())
