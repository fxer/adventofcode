import copy

with open('day07.input') as f:
# with open('day07test.input') as f:
    data = []
    for line in f:
        row = []
        # reach each token in the row
        for token in line.strip().split(' '):
            # the last entry in a row list will always be the destination wire
            if token != '->':
                # parse ints as they are found
                if token.isdigit():
                    token = int(token)
                # add token to row
                row.append(token)
        # add row to overall list
        data.append(row)


def solve(instructions, override={}):
    # dict to hold the circuit, wires as keys
    circuit = {}

    # dict to hold the solutions, wires as keys
    solutions = {}

    # populate circuit dict with initial data
    for line in instructions:
        circuit[(line[-1])] = line[:-1]

    # loop until we solve for wire 'a'
    while 'a' not in solutions:
        # copy solved wires over to solutions dict
        for wire, connections in circuit.items():
            if len(connections) == 1 and isinstance(connections[0], int):
                solutions[wire] = connections[0]
                if wire in override:
                    solutions[wire] = override[wire]

        # now use solutions dict to fill placeholders in circuits dict
        for wire, connections in circuit.items():
            # look at each piece of a connection
            for item in connections:
                # if we know the value for a piece of a connection, fill it!
                if item in solutions:
                    circuit[wire][connections.index(item)] = solutions[item]

        # solve wires we have enough data for
        for wire, connections in circuit.items():
            # if there is only one string left in the 'connections', that's our bitwise operator!
            # ...unless it was a simple substitution line, such as: lx -> a
            # we can skip that latter instance since it will get placeholder filled eventually!
            if sum(isinstance(i, str) for i in connections) == 1 and len(connections) > 1:

                # two length connections are just NOTs aka the Bitwise Complement
                if len(connections) == 2:
                    circuit[wire] = [~connections[1]]
                else:
                    if connections[1] == 'RSHIFT':
                        circuit[wire] = [connections[0] >> connections[2]]
                    elif connections[1] == 'LSHIFT':
                        circuit[wire] = [connections[0] << connections[2]]
                    elif connections[1] == 'AND':
                        circuit[wire] = [connections[0] & connections[2]]
                    elif connections[1] == 'OR':
                        circuit[wire] = [connections[0] | connections[2]]

    return solutions['a']

# we can pass original instance of our data since we will take slices of it to build our circuit
# thus the original data will not be mutated
print(solve(data))
print(solve(data, {'b': 16076}))
