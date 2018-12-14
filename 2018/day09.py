#!/usr/bin/env python3

from collections import deque, defaultdict


class MarbleMania():
    def __init__(self, num_players, rounds):
        self.rounds = rounds

        # Initalize scoreboard as dict of player numbers
        self.scoreboard = dict(zip(range(1, num_players+1), [0]*num_players))

    def high_score(self):
        return max(self.scoreboard.values())

    def place_marbles(self):
        round = 0       # the current marble number, aka "round"
        circle = [0]    # list of marbles in the circle
        pos = 0         # the currently active marble position within the list
        while round < self.rounds:
            round += 1

            if round % 23 == 0:
                # YAHTZEE you scored!
                player = (round % len(self.scoreboard)) + 1

                # calculate new position, moving counterclockwise
                pos = (pos - 7) % len(circle)

                # You earned the value of your marble _plus_ one you popped!
                self.scoreboard[player] += round + circle.pop(pos)

            else:
                # Calculate the new position for this marble
                pos = (pos + 2) % len(circle)

                # If position is 0, you place at the end of the list instead of the beginning
                if pos == 0:
                    pos = len(circle)

                circle.insert(pos, round)

            # print("round:", round, "pos:", pos, "circle:", circle)
            # if round % 10000 == 0:
            #     print(f"round: {round}/{self.rounds}")


def deque_mania(num_players, rounds):
    # defaultdict will init all new keys to value 0
    scoreboard = defaultdict(int)
    circle = deque([0])

    for round in range(1, rounds+1):
        if round % 23 == 0:
            # like spinning a dial, deque rotates clockwise w/ positive ints
            # that effectively "backs up" or list, to pop a winning marble off of
            circle.rotate(7)
            scoreboard[round % num_players] += round + circle.pop()
            # Select marble "clockwise" (ie: to the right of) the one we just popped by rotating deque itself counter-clockwise
            circle.rotate(-1)

        else:
            # negative rotation backs our current element to one-away from end of list
            # then append creates a new element at the end of the list, so we're now 2 steps away from where we started! magic!
            circle.rotate(-1)
            circle.append(round)

    return max(scoreboard.values())


def part1():
    mm = MarbleMania(num_players=479, rounds=71035)
    mm.place_marbles()
    print("part1: high score:", mm.high_score())


def part2():
    # part 2 is intented to show you a naieve solution is too slow and you need to implement a linked-list type solution
    # This awesome solution shows how to use the python _deque_ "double-ended queue" container and is super elegant
    # https://www.reddit.com/r/adventofcode/comments/a4i97s/2018_day_9_solutions/ebepyc7

    # too slow, maybe would return (or crash?) if run overnight
    # mm = MarbleMania(num_players=479, rounds=71035*100)
    # mm.place_marbles()


    print("part2: high score:", deque_mania(num_players=479, rounds=71035*100))


def example1():
    # format is: # player, rounds, high score
    cases = [(9, 25, 32),
             (10, 1618, 8317),
             (13, 7999, 146373),
             (17, 1104, 2764),
             (21, 6111, 54718),
             (30, 5807, 37305)]

    for num_players, rounds, high_score in cases:
        mm = MarbleMania(num_players, rounds)
        mm.place_marbles()
        print("example1: high score:", mm.high_score())
        assert mm.high_score() == high_score


def example_deque():
    # format is: # player, rounds, high score
    cases = [(9, 25, 32),
             (10, 1618, 8317),
             (13, 7999, 146373),
             (17, 1104, 2764),
             (21, 6111, 54718),
             (30, 5807, 37305)]

    for num_players, rounds, high_score in cases:
        result = deque_mania(num_players, rounds)
        print("example_deque: high score:", result)
        assert result == high_score

example1()
example_deque()
part1()
part2()
