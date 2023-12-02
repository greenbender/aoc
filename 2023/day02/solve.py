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
    for game in subgames:
        if game["red"] > red or game["green"] > green or game["blue"] > blue:
            return False
    return True


def power(subgames):
    r = max(subgames["red"] for subgames in subgames)
    g = max(subgames["green"] for subgames in subgames)
    b = max(subgames["blue"] for subgames in subgames)
    return r * g * b


def part1():
    print(sum(i for i, subgames in games if possible(subgames)))


def part2():
    print(sum(power(subgames) for _, subgames in games))


part1()
part2()
