with open('day06.input') as f:
    input = [int(x) for x in f.read().rstrip().split('\t')]

def solve_both_parts(memory):
    # track all the memory configurations we have seen
    history = []

    # Store the initial memory configuration
    history.append(list(memory))

    # track number of times we've redistributed memory
    cycles = 0

    while True:
        cycles += 1 # increment redistribution counter

        # find memory bank with largest value
        high_index = 0
        for i in range(len(memory)):
            if memory[i] > memory[high_index]:
                high_index = i

        # num of blocks we'll redistribute
        blocks = memory[high_index]

        # zero out memory bank we're redistributing from
        memory[high_index] = 0

        # redistribute
        current_index = high_index
        while blocks > 0:
            current_index += 1
            if current_index >= len(memory):
                current_index = 0

            # give 1 block to current memory bank
            memory[current_index] += 1
            blocks -= 1

        # If we've seen this configuration before, we're done!
        if memory in history:
            return cycles, len(history) - history.index(memory)

        # haven't seen it before, add config to history
        history.append(list(memory))

print(solve_both_parts(input))
