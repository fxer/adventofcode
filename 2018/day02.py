from collections import Counter
from functools import reduce

with open('day02.input') as f:
    data = [x.strip() for x in f]

def part1():
    tally = {}
    for boxid in data:
        multiples = set(Counter(boxid).values())
        multiples.discard(1) # we don't care about multiples of 1

        for x in multiples:
            if x in tally:
                tally[x] += 1
            else:
                tally[x] = 1

    return reduce(lambda x, y: x*y, tally.values())


def part2():
    for boxid in data:
        for compareid in data:
            errors = 0
            idx = -1
            if boxid != compareid:
                for i in range(len(boxid)):
                    if boxid[i] != compareid[i]:
                        errors += 1
                        idx = i
                    if errors > 1:
                        break
            if errors == 1:
                # Found ids with 1 differing char, remove it
                return boxid[:idx] + boxid[idx+1:]

print(part1())
print(part2())
