with open('day05.input') as f:
    input = f.read().split()


def part1(l):
    # track the nice strings
    nice = []

    for s in l:
        # skip banned strings
        if 'ab' in s or 'cd' in s or 'pq' in s or 'xy' in s:
            continue

        # skip strings with too few vowels
        vowels = s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')
        if vowels < 3:
            continue

        # skip strings with no letter pairs
        prev_char = -1
        keep = False
        for char in s:
            # if we find a pair of characters, keep the string and escape loop
            if char == prev_char:
                keep = True
                break
            prev_char = char
        if keep:
            nice.append(s)

    return len(nice)

def part2(santaslist):
    # track the nice strings
    nice = []

    for s in santaslist:
        # skip strings where characters don't repeat with a lil' buddy in-between
        cursor = 0
        # track if we're keeping this string for now
        keep = False
        while cursor < len(s)-2:
            substring = s[cursor:cursor+3]
            # if the first and third letters match, it passed this test
            if substring[0] == substring[2]:
                keep = True
                break
            cursor += 1

        # Didn't pass the first test so move onto next string
        if not keep:
            continue

        # skip strings which don't contain two pairs of any letter
        cursor = 0
        while cursor < len(s)-3:
            substring = s[cursor:cursor+2]
            # if the substring matches somewhere else in the list, we win!
            if substring in s[cursor+2:]:
                nice.append(s)
                break
            cursor += 1

    return len(nice)

print(part1(list(input)))
print(part2(list(input)))
