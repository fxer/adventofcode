with open('day08.input') as f:
    data = [int(x) for x in f.read().split()]


class Node:
    def __init__(self):
        self.metadata = []
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

    def set_metadata(self, obj):
        self.metadata = obj


def build_node(current_node, num_children, num_metadata, license):
    """
    initalize node with metadata and children based on "license" input
    """
    while num_children > 0:
        child = Node()
        current_node.add_child(child)

        license = build_node(child, license[0], license[1], license[2:])
        num_children -= 1

    current_node.set_metadata(license[:num_metadata])

    return license[num_metadata:]


def sum_metadata(current_node):
    """
    return sum of metadata values along this branch
    """
    total = 0
    for child in current_node.children:
        total += sum_metadata(child)

    return total + sum(current_node.metadata)


def node_value(current_node):
    """
    calculate value of node from its metadata and children
    """
    total = 0
    # If there are no child nodes, value is sum of metadata values
    if len(current_node.children) == 0:
        total += sum(current_node.metadata)

    # if there are child nodes, see if metadata references them
    else:
        for entry in current_node.metadata:
            # if metadata entry matches a child, calc child value
            if entry <= len(current_node.children):
                total += node_value(current_node.children[entry-1])

    return total


def part1():
    # init root node
    tree = Node()

    # walk data to populate tree
    build_node(tree, data[0], data[1], data[2:])

    return sum_metadata(tree)


def part2():
    tree = Node()
    build_node(tree, data[0], data[1], data[2:])

    return node_value(tree)

print(part1())
print(part2())
