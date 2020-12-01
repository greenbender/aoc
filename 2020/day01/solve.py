import sys
import itertools


report = list(map(int, sys.stdin))


def part1():
    for a, b in itertools.combinations(report, 2):
        if a + b == 2020:
            print(a * b)
            break


def part2():
    for a, b, c in itertools.combinations(report, 3):
        if a + b + c == 2020:
            print(a * b * c)
            break


part1()
part2()
