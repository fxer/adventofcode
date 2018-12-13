with open('day03.input') as f:
    data = [[int(x) for x in line.split()] for line in f]


def numvalid(triangles):
    valid = 0
    for x in triangles:
        t = sorted(x)
        if t[0] + t[1] > t[2]:
            valid += 1

    return valid

def part2():
    i = 0
    triangles = []
    while i < len(data):
        # zip is great for reformatting the input triangle lists!
        newdata = zip(data[i], data[i+1], data[i+2])

        for t in newdata:
            triangles.append(t)

        i = i+3

    return numvalid(triangles)

print(numvalid(data))
print(part2())
