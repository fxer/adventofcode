with open('day09.input') as f:
    stream = list(f.read().strip())


def solve():
    stack = []
    score = garbageScore = 0
    cancel = False
    garbage = False

    for char in stream:
        # print('char:', char, 'garbage:', garbage, 'cancel:', cancel, 'stack:', stack)
        if cancel:
            # Check if this char should be canceled
            cancel = False
            continue

        if garbage:
            # If we are inside a garbage stream
            if char == '!':
                # Skip the next char in the stream
                cancel = True
            elif char == '>':
                # End of garbage stream
                garbage = False
            else:
                garbageScore += 1

        elif char == '<':
            # Begin discarding garbage
            garbage = True

        elif char == '{':
            # If it is a new group, add to stack
            stack.append(char)

        elif char == '}':
            # Add to score, remove opening bracket from stack
            score += len(stack)
            stack.pop()

    return score, garbageScore


print(solve())
