with open('day02.input') as f:
    data = [int(x) for x in f.read().split(',')]

def part1(intcode, overrides={}):
    for k,v in overrides.items():
        intcode[k] = v

    # track position in intcode list
    pos = 0

    while intcode[pos] != 99:
        # take slice we're operating on
        s = intcode[pos:pos+4]

        output = 0
        if s[0] == 1:
            output = intcode[s[1]] + intcode[s[2]]
        elif s[0] == 2:
            output = intcode[s[1]] * intcode[s[2]]
        else:
            exit("Unknown opcode at pos {}: {}".format(pos, s[0]))

        # store new value at given position
        intcode[s[3]] = output

        # increment to new opcode
        pos += 4

    return intcode[0]

def part2(target):
    for noun in range(0,99):
        for verb in range(0,90):
            output = part1(data.copy(), overrides={1:noun, 2:verb})

            if output == target:
                result = 100 * noun + verb
                # print(f"noun: {noun} verb: {verb} result: {result}")
                return result;


def tests():
    intcode = [1,0,0,0,99]
    assert part1(intcode) == 2

    intcode = [1,1,1,4,99,5,6,0,99]
    assert part1(intcode) == 30

    intcode = [1,9,10,3,2,3,11,0,99,30,40,50]
    assert part1(intcode) == 3500

tests()
print(part1(data.copy(), overrides={1:12,2:2}))
print(part2(19690720))
