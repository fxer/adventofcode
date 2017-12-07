with open('day03.input') as f:
    input = [str(x) for x in f.read().rstrip()]

def part1(route):
    # track all the houses visted and packages left there
    grid = {}

    # track starting location
    x = y = 0

    # prime grid with starting location
    grid[(x, y)] = 0

    for direction in route:
        # deliver present to starting location, which will always exist in grid already
        grid[(x, y)] += 1

        # Determine where you've moving, Cartesianally
        if direction == '^':
            y += 1
        elif direction == '>':
            x += 1
        elif direction == 'v':
            y -= 1
        else:
            x -= 1

        # Deliver present to current house
        if (x, y) in grid:
            grid[(x, y)] += 1
        else:
            grid[(x, y)] = 1

    # num of houses that houses that have been visited/gifted is grid size
    return len(grid)

def part2(route):
    # track all the houses visted and packages left there
    grid = {}

    # track starting location for Santa and Robosanta
    sx = sy = rx = ry = 0

    # prime grid with starting location
    grid[(sx, sy)] = 0

    for index, direction in enumerate(route):

        # we're moving Santa
        if index % 2 == 0:
            # deliver present to starting location, which will always exist in grid already
            grid[(sx, sy)] += 1

            # Determine where you've moving, Cartesianally
            if direction == '^':
                sy += 1
            elif direction == '>':
                sx += 1
            elif direction == 'v':
                sy -= 1
            else:
                sx -= 1

            # Deliver present to current house
            if (sx, sy) in grid:
                grid[(sx, sy)] += 1
            else:
                grid[(sx, sy)] = 1

        # we're moving Robosanta
        else:
            # deliver present to starting location, which will always exist in grid already
            grid[(rx, ry)] += 1

            # Determine where you've moving, Cartesianally
            if direction == '^':
                ry += 1
            elif direction == '>':
                rx += 1
            elif direction == 'v':
                ry -= 1
            else:
                rx -= 1

            # Deliver present to current house
            if (rx, ry) in grid:
                grid[(rx, ry)] += 1
            else:
                grid[(rx, ry)] = 1

    # num of houses that houses that have been visited/gifted is grid size
    return len(grid)


print(part1(list(input)))
print(part2(list(input)))
