import sys
from collections import defaultdict


def parse(line):
    game, groups = line.strip().split(": ")
    game = int(game.split(" ")[1])
    subgames = []
    for group in groups.split("; "):
        colours = defaultdict(int)
        for entry in group.split(", "):
            value, colour = entry.split(" ")
            colours[colour] = int(value)
        subgames.append(colours)
    return game, subgames


games = [parse(line) for line in sys.stdin]


def possible(subgames, red=12, green=13, blue=14):
    for subgame in subgames:
        if subgame["red"] > red or subgame["green"] > green or subgame["blue"] > blue:
            return False
    return True


def power(subgames):
    r = max(subgame["red"] for subgame in subgames)
    g = max(subgame["green"] for subgame in subgames)
    b = max(subgame["blue"] for subgame in subgames)
    return r * g * b


def part1():
    print(sum(i for i, subgames in games if possible(subgames)))


def part2():
    print(sum(power(subgames) for _, subgames in games))


part1()
part2()
