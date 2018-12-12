import string

# A faster Python solution using my same ideas, but appending/popping from a 2nd list
# https://www.reddit.com/r/adventofcode/comments/a3912m/2018_day_5_solutions/eb4jzni

with open('day05.input') as f:
    data = list(f.read().strip())


def part1(polymer):
    """
    React the polymer and return length
    """
    reduced = False

    while not reduced:
        i = 0
        reduced = True
        while i < len(polymer)-1:
            if polymer[i].lower() == polymer[i+1].lower() and polymer[i] != polymer[i+1]:
                polymer.pop(i+1)
                polymer.pop(i)
                reduced = False
            else:
                i += 1

    return len(polymer)


def part2():
    """
    Return shortest polymer with one unit type fully removed
    """
    smallest = 99999999
    for unit in string.ascii_lowercase:
        # Work on a copy of the input data
        polymer = data[:]
        reduced = [x for x in polymer if x not in (unit, unit.upper())]

        # Fully react resulting polymer
        reacted_size = part1(reduced)

        if reacted_size < smallest:
            # print(unit, reacted_size)
            smallest = reacted_size

    return smallest


print(part1(data[:]))
print(part2())
