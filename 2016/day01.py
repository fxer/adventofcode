# create list of given directions
with open('day01.input') as f:
    input = [x.strip() for x in f.read().split(',')]

# 0 up, 1 right, 2 down, 3 left
def get_direction(current, new):
    if new == 'R':
        current += 1
    else:
        current -= 1

    if current < 0:
        return 3
    elif current > 3:
        return 0
    return current

def part1():
    # starting coordinates
    x = y = 0

    # start facing North, or Cartesianally, positive y
    direction = 0

    for command in input:
        # find the new direction you are facing
        direction = get_direction(direction, command[0])

        # move your x or y coordinate the distance given in the direction calculated
        blocks = int(command[1:])

        # use direction to determine how you'll move Cartesianally
        if direction == 0:
            y += blocks
        elif direction == 1:
            x += blocks
        elif direction == 2:
            y -= blocks
        else:
            x -= blocks

    return abs(x) + abs(y)

def part2():
    # keep a dict of all the locations we've visited
    locations = {}

    # starting coordinates, add to location list
    x = y = 0
    locations[(x, y)] = True

    # start facing North, or Cartesianally, positive y
    direction = 0

    for command in input:
        # find the new direction you are facing
        direction = get_direction(direction, command[0])

        # move your x or y coordinate the distance given in the direction calculated
        blocks = int(command[1:])

        # record each block you visit
        while blocks > 0:
            # use direction to determine how you'll move Cartesianally
            if direction == 0:
                y += 1
            elif direction == 1:
                x += 1
            elif direction == 2:
                y -= 1
            else:
                x -= 1
            blocks -= 1;

            # if the location already exists, we're done!
            if (x, y) in locations:
                return abs(x) + abs(y)
            else:
                locations[(x, y)] = True

print(part1())
print(part2())
