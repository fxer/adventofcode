import csv

input = 'day02.input'

def part1():
    checksum = 0
    with open(input) as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            row_ints = list(map(int, row))
            checksum += max(row_ints) - min(row_ints)
    return checksum

def part2():
    evens = 0
    with open(input) as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            row_ints = list(map(int, row))
            # loop through each entry
            for index_numerator, numerator in enumerate(row_ints):
                # loop over each divisor
                for index_denominator, denominator in enumerate(row_ints):
                    # don't divide numerator by itself, silly
                    if index_numerator != index_denominator:
                        # if there is no remainder we found the answer
                        if numerator % denominator == 0:
                            evens += int(numerator / denominator)
                            # don't bother looking further
                            break
    return evens

print(part1())
print(part2())
