with open('day10.input') as f:
    data = [int(x) for x in f.read().split(',')]


def part1(lengths=data, circle=list(range(0,256))):
    pos = 0
    skip = 0

    for length in lengths:
        print('pos:', pos, 'skip:', skip, 'length:', length)
        print('circle:',circle)

        # Find where our new position on the circle will be
        new_pos = (pos + length) % len(circle)

        if length > 0:
            # Take however much of the list is available from 'pos' to end of list
            circle_slice = circle[pos:pos+length]

            # If we looped around the circle, join beginning of the list to our slice
            if new_pos <= pos:
                circle_slice += circle[0:length-len(circle_slice)]

            # reverse slice
            circle_slice = circle_slice[::-1]

            # build the new circle list
            if new_pos > pos:
                circle[pos:pos+len(circle_slice)] = circle_slice
            else:
                circle[pos:] = circle_slice[:len(circle[pos:])]
                circle[0:new_pos] = circle_slice[len(circle[pos:]):]

        # Update position and skip size
        pos = (new_pos + skip) % len(circle)
        skip += 1

    return circle[0] * circle[1]



print(part1(lengths=[3,4,1,5], circle=list(range(0,5))))
# print(part1())
