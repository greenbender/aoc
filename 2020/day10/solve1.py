'''Minimal version of solve.py'''
import sys
import itertools


adapters = list(sorted(map(int, sys.stdin)))
adapters.insert(0, 0)
adapters.append(adapters[-1] + 3)


diffs = [b - a for a, b in zip(adapters, adapters[1:])]


def combos(n):
    if n < 2:
        return 0
    c = ((n - 1) * n) // 2
    for i in range(2, n - 3):
        c += 2 * combos(i)
    return c


def part1():
    print(diffs.count(1) * diffs.count(3))


def part2():
    c = 1
    for v, g in itertools.groupby(diffs):
        if v == 1:
            c *= combos(len(list(g))) + 1
    print(c)


part1()
part2()
