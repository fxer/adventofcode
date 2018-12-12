import re
from collections import Counter

with open('day04.input') as f:
    data = []
    for line in f:
        data.append(line.strip())

    data.sort(key = lambda x: re.findall("\[(.*?)\]", x))

def part1():
    schedule = {}
    guard = -1
    alseep = -1
    for x in data:
        day = x[6:11]
        minute = int(x[15:17])
        event = x[19:]

        event_list = event.split()
        if event_list[0] == 'Guard':
            guard = int(event_list[1][1:])
        elif event_list[0] == 'falls':
            asleep = minute
        elif event_list[0] == 'wakes':
            for i in range(asleep, minute):
                schedule[(guard, day, i)] = True
                # print(guard, 'alseep at minute', i)

    sleepiest_guard = Counter([k[0] for k,v in schedule.items()]).most_common(1)[0][0]
    sleepiest_guard_minute = Counter([k[2] for k,v in schedule.items() if k[0] == sleepiest_guard]).most_common(1)[0][0]

    guards = {k[0] for k,v in schedule.items()}
    sleepiest_overall_guard = -1
    sleepiest_overall_minute = -1
    sleepiest_overall_times = -1
    for g in guards:
        min, times = Counter([k[2] for k,v in schedule.items() if k[0] == g]).most_common(1)[0]
        if times > sleepiest_overall_times:
            sleepiest_overall_guard = g
            sleepiest_overall_minute = min
            sleepiest_overall_times = times

    return (sleepiest_guard * sleepiest_guard_minute, sleepiest_overall_guard * sleepiest_overall_minute)

print(part1())
