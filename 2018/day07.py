import re
import collections
from itertools import chain


with open('day07.input') as f:
    data = []
    for line in f:
        data.append(re.findall(r'\s([A-Z]{1})\s', line))

class Worker:
    def __init__(self, step, done_at):
        self.step = step
        self.done_at = done_at

def part1():
    # steps need to be worked with alphabetically
    requirements = get_requirements()

    completed = []
    while len(requirements) > 0:
        # Check (alphabetically) if each step has its requirements met
        for k, v in requirements.items():
            if set(v).issubset(completed):
                # requirement complete!
                completed.append(k)
                requirements.pop(k)
                break

    return ''.join(completed)


def part2(worker_limit, delay):
    requirements = get_requirements()

    # Track "seconds" for each iteration
    tick = 0

    # Track our worker elves
    workers = []

    completed = []
    while len(requirements) > 0 or len(workers) > 0:
        # As long as we have available workers, try to find them work
        found_work = True
        while len(workers) < worker_limit and found_work:
            found_work = False
            for k, v in requirements.items():
                if set(v).issubset(completed):
                    # Found a step ready to complete, assign it to a worker
                    w = Worker(k, tick+delay+ord(k)-65)
                    workers.append(w)
                    # print("tick:", tick, "worker starting:", w.step, "until: ", w.done_at)

                    # Found work, start from top of requirements again
                    requirements.pop(k)
                    found_work = True
                    break


        # Do any workers finish on this tick?
        for w in workers:
            if w.done_at == tick:
                # print("tick:", tick, "Worker finished:", w.step)
                completed.append(w.step)
                workers.remove(w)

        # increase clock
        tick += 1
        # print("tick:", tick, "completed:", completed)

    return tick


def get_requirements():
    # Build dictionary of requirements
    requirements = {}
    for k in set(chain(*data)):
        # initalize step with empty list of requirements
        requirements[k] = []
        for cmd in data:
            if cmd[1] == k:
                # found a new requirement
                requirements[k].append(cmd[0])

    # steps need to be worked with alphabetically
    return collections.OrderedDict(sorted(requirements.items()))


print(part1())
print(part2(5, 60))
