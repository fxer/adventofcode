import math

with open('day01.input') as f:
    data = [int(x) for x in f]

def part1(in_data):
    total = 0
    for k in in_data:
        total += fuel_required(k)
    return total

def part2(in_data):
    total = 0
    for k in in_data:
        total += total_fuel_required(k)
    return total

def fuel_required(mass):
    return math.floor(mass / 3) - 2

def total_fuel_required(mass):
    fuel = math.floor(mass/3)-2
    if fuel > 0:
        return fuel + total_fuel_required(fuel)
    return 0

def tests():
    assert part1([12]) == 2
    assert part1([1969]) == 654
    assert part1([100756]) == 33583

    assert part2([12]) == 2
    assert part2([1969]) == 966
    assert part2([100756]) == 50346


tests()
print(part1(data))
print(part2(data))
