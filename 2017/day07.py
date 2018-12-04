'''
Part 1 can actually be sovled with a fantastic bash one liner. All we
need to do is find the 'program name' which only appears once in the list.
Since no other program will reference it, it must be the bottom!

https://www.reddit.com/r/adventofcode/comments/7i44pg/2017_day_7_solutions/dqw40p0/
grep -o -E '[a-z]+' day07.input | sort | uniq -u
'''

import re
from collections import Counter
import pprint

with open('day07.input') as f:
    data = f.read()

def part1(programs):
    # regex to match all program names, dumping superflous data
    pattern = re.compile(r'[a-z]+')
    all_programs = re.findall(pattern, data)

    # whatever program is listed the fewest times is our 'base' program
    # which will be at the bottom [-1] of the .most_common() return list
    # as the first element in the tuple [0]
    return Counter(all_programs).most_common()[-1][0]

def part2(programs):
    weight = {}
    children = {}
    for line in programs.splitlines():
        # jettison all but regex 'words' for each line
        node, lbs, *supports = re.findall(r'\w+', line)
        # map nodes to their weight
        weight[node] = int(lbs)
        # map nodes to the children they support
        children[node] = tuple(supports)

    # recursively calculate the total weight of a node by summing its weight
    # plus walking all its children
    def total_weight(node):
        return weight[node] + sum(total_weight(child) for child in children[node])

    # take the set of all nodes and subtract the set of all children
    # build the children set via list comprehension from each row, then into each entry
    # the root will not appear in the child set, so there is our base program!
    # the comma after 'root' will unpack the return set to just give us the base program
    root, = set(weight) - {child for childset in children.values() for child in childset}

    # start from the root node
    parent = root
    # track the weight difference between the wrong and correct weights
    weight_diff = 0

    while True:
        # track total weight of each node on this tier
        nodeweight = {}
        for child in children[parent]:
            nodeweight[child] = total_weight(child)
        # print(parent, nodeweight)

        # reverse sort the number of unique child weights to find the bad one
        weights = sorted(Counter(nodeweight.values()),reverse=True)

        # if we found more than one unique weight value, one is bad!
        if len(weights) > 1:
            # store weight imbalance at this tier
            weight_diff = weights[0] - weights[1]
            for n, w in nodeweight.items():
                # the bad weight is the first index in our reverse sorted list
                if w == weights[0]:
                    parent = n
                    break
        else:
            # no incorrect weights among the children, so the parent is the problem!
            return weight[parent] - weight_diff

print(part1(data))
print(part2(data))
