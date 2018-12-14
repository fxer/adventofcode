import itertools

with open('day01.input') as f:
    data = [int(x) for x in f]

def part1():
    return sum(data)

def part2():
    current = 0
    known_frequencies = {0}
    for offset in itertools.cycle(data):
        current = current + offset

        if current in known_frequencies:
            return current
        else:
            known_frequencies.add(current)

print(part1())
print(part2())
