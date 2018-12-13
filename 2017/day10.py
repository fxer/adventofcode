#!/usr/bin/env python3

from operator import xor
from functools import reduce

# "Standard Length Suffix" to append to input data if required
LENGTHS_SUFFIX = [17, 31, 73, 47, 23]

with open('day10.input') as f:
    data = f.read().strip()
    # get input as list of ints
    data_ints = [int(x) for x in data.split(',')]

    # get input as list of strings, converted to bytes via their ASCII code
    # then append the provided 5-byte suffix
    data_bytes = [ord(x) for x in list(data)]


def knot_hash(lengths, circle, pos, skip):
    """
    Run a single round of the Knot Hash algorithm
    return circle, the final position, and the final skip size
    """

    for length in lengths:
        if (pos + length) <= len(circle):
            segment = circle[pos:pos+length]

            # reverse-and-replace segment in circle
            circle = circle[0:pos] + segment[::-1] + circle[(pos + length):]

        # If we looped the circle, move front of the list to the end of the list!
        else:
            # take remaining part of circle/list
            segment = circle[pos:]
            # print("a", segment)

            # steal remainder from the front of the list
            stolen = circle[0:length-len(segment)]
            # print("b", stolen)

            # append stolen chunk from front of circle/list
            segment += stolen
            # print("c", segment)

            # flip it n' reverse it
            segment = segment[::-1]
            # print("d", segment)

            # rebuild the circle
            circle = segment[-len(stolen):] + circle[len(stolen):-(len(segment)-len(stolen))] + segment[:-len(stolen)]

        pos = (pos + length + skip) % len(circle)
        skip += 1

        # print('circle:', circle, 'pos:', pos, 'skip:', skip, 'length:', length)

    return circle, pos, skip


def get_hash(lengths, rounds):
    pos = 0
    skip = 0
    circle = list(range(256))
    sparse_hash = []

    # run knot hash for specified rounds, initializing each round with previous circle, position, and skip size
    for i in range(rounds):
        circle, pos, skip = knot_hash(lengths, circle, pos, skip)

    # calculate dense hash by XORing 16-number blocks
    dense_hash = []
    for i in range(int(len(circle)/16)):
        dense_hash.append(reduce(xor,circle[i*16:i*16+16]))

    # convert dense hash to hex hash
    hash = []
    for c in dense_hash:
        # pad hex prefix with zeroes
        hash.append(f"{c:0{2}x}")

    return ''.join(hash)


def part1():
    result = knot_hash(data_ints, list(range(256)), 0, 0)[0]
    print("part1:", result[0] * result[1])


def part2():
    print("part2:", get_hash(data_bytes + LENGTHS_SUFFIX, 64))


def example1():
    case = [3, 4, 1, 5]
    expected = 12
    circle = list(range(5))
    result = knot_hash(case, circle, 0, 0)[0]
    answer = result[0] * result[1]
    print("example1: result:", answer, "expected:", expected)
    assert answer == expected


def example2():
    examples = [("", 'a2582a3a0e66e6e86e3812dcb672a272'),
             ('AoC 2017', '33efeb34ea91902bb2f59c9920caa6cd'),
             ('1,2,3', '3efbe78a8d82f29979031a4aa0b16a9d'),
             ('1,2,4', '63960835bcdc130f0b66d7ff4f6a5a8e')]

    for in_string, expected in examples:
        in_bytes = [ord(ch) for ch in in_string]
        result = get_hash(in_bytes + LENGTHS_SUFFIX, rounds=64)
        print("example2: input:", in_string, "result:", result, "expected:", expected)
        assert result == expected


example1()
example2()
part1()
part2()
