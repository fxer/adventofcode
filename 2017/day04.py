import csv

input = 'day04.input'

def part1():
    valid = 0
    with open(input) as f:
        reader = csv.reader(f, delimiter=' ')
        for row in reader:
            if len(row) == len(set(row)):
                valid += 1
    return valid

def part2():
    valid = 0
    with open(input) as f:
        reader = csv.reader(f, delimiter=' ')
        for row in reader:
            invalid = False
            for index_p, passphrase in enumerate(row):
                for index_c, comparison in enumerate(row):
                    if index_p != index_c:
                        if sorted(passphrase) == sorted(comparison):
                            invalid = True
            if not invalid:
                valid += 1
    return valid

print(part1())
print(part2())
