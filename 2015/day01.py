# split directions into list
with open('day01.input') as f:
    input = list(f.read().rstrip())

def part1():
    floor = 0

    for command in input:
        if command == "(":
            floor += 1
        else:
            floor -= 1

    return floor

def part2():
    floor = 0

    for index, command in enumerate(input):
        if command == "(":
            floor += 1
        else:
            floor -= 1

        # enumerate is 0 indexed but the question is 1 indexed
        if floor < 0:
            return index+1

print(part1())
print(part2())
