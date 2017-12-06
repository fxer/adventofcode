with open('day05.input') as f:
    input = [int(x) for x in f]

def part1(jumps):
    steps = 0 # how many operations we have currently executed
    cursor = 0 # where in the list we are currently executing

    while cursor < len(jumps):
        found_value = jumps[cursor] # store jump value found at cursor
        jumps[cursor] = jumps[cursor] + 1 # increment value of cell we just found
        cursor += found_value # move cursor ahead to next jump location
        steps += 1

    return steps

def part2(jumps):
    steps = 0 # how many operations we have currently executed
    cursor = 0 # where in the list we are currently executing

    while cursor < len(jumps):
        found_value = jumps[cursor] # store jump value found at cursor
        if found_value >= 3:
            jumps[cursor] = jumps[cursor] - 1
        else:
            jumps[cursor] = jumps[cursor] + 1
        cursor += found_value # move cursor ahead to next jump location
        steps += 1

    return steps


print(part1(list(input)))
print(part2(list(input)))
