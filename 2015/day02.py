import copy

with open('day02.input') as f:
    input = [[int(n) for n in line.strip().split('x')] for line in f]

def part1(boxes):
    # track total paper we'll need
    total = 0
    # loop over each box
    for box in boxes:
        # box indexes: 0 = L, 1 = W, 2 = H
        # surface area = 2*L*W + 2*W*H + 2*H*L
        total += 2*box[0]*box[1] + 2*box[1]*box[2] + 2*box[2]*box[0]

        # add slack for the smallest side
        box.remove(max(box))
        total += box[0]*box[1]

    return total

def part2(boxes):
    total = 0

    for box in boxes:
        # calculate bow size
        total += box[0]*box[1]*box[2]
        # to find the perimiter of the smallest face, remove the largest face
        box.remove(max(box))
        # calculate perimiter
        total += 2*box[0]+2*box[1]

    return total

# must use deepcopy since input is a list of lists, so a shallow copy would
# still retain refs to *original* (package dimensions) lists inside it
print(part1(copy.deepcopy(input)))
print(part2(copy.deepcopy(input)))
