with open('day08.input') as f:
    # create a list of lists
    # each line consists of 7 tokens in the format: e dec -568 if f != 0
    # convert numbers to ints, using an lstrip trick to handle negatives
    commands = [[int(x) if x.lstrip('-').isdigit() \
                else x for x in line.strip().split(' ') if x != 'if'] for line in f]


def resolver(cmd, registers):
    # unpack the command
    reg, op, val = cmd

    if op == '==':
        return True if registers[reg] == val else False
    elif op == '!=':
        return True if registers[reg] != val else False
    elif op == '>':
        return True if registers[reg] > val else False
    elif op == '>=':
        return True if registers[reg] >= val else False
    elif op == '<':
        return True if registers[reg] < val else False
    elif op == '<=':
        return True if registers[reg] <= val else False


def solve():
    # the first index of every command will be the register name
    # initalize it with value 0
    registers = { command[0]: 0 for command in commands }

    highest = 0

    for cmd in commands:
        # check if the specified 'if' statement is True
        if resolver(cmd[-3:], registers):
            # if was True, execute command
            reg, op, val = cmd[:3]
            if op == 'inc':
                registers[reg] += val
            else:
                registers[reg] -= val

        # track highest value ever seen
        if max(registers.values()) > highest:
            highest = max(registers.values())


    return max(registers.values()), highest

print(solve())
