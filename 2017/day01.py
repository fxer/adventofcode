# split number into list
with open('day01.input') as f:
    input = [int(x) for x in str(f.read().rstrip())]

def part1():
    code_sum = 0
    current_num = next_num = -1

    for next_num in input:
        if current_num == next_num:
            code_sum += current_num
        current_num = next_num

    # handle the circular number list requirement
    if current_num == input[0]:
        code_sum += current_num

    return code_sum

def part2():
    codesum = 0
    for index, current_num in enumerate(input):
        entangled_num = input[(index + int(len(input)/2)) % len(input)]

        if current_num == entangled_num:
            codesum += current_num

    return codesum

print(part1())
print(part2())
